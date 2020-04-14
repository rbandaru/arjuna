
from arjuna.tpi.guiauto.meta.formatter import GNSLabelFormatter
from arjuna.tpi.exceptions import *
from arjuna.core.exceptions import *
from arjuna.interact.gui.auto.finder import GuiEmdFinder, GuiElementEmdFinder

class GNS:
    '''
        Gui Namespace object associated with a `Gui` or `GuiElement`.

        Not meant to be directly created. Available as `gns` property of a `Gui`.

        Arguments:
            gui_or_element: `Gui` or `GuiElement` object.
            gui_def: Gui Definition

        Note:
            To locate a GUI Widget using GNS object, you can use the `.` notation. For example:

                .. code-block:: python

                    gui.gns.some_label
                    some_element.gns.some_label

            This will locate the GuiWidget using the GuiWidgetMetaData corresponding to following entry in GNS file:

                .. code-block:: YAML

                    labels:
                        some_label:
                            <metdata dictionary>

            `gui.gns` will locate it in the root GuiWidget of `Gui` if available and allowed.

            `some_element.gns.some_label` will do a nested locating inside `some_element`.
    '''

    def __init__(self, gui_or_element, gui_def):
        self.__container_type = None
        self.__gui = None
        self.__container = None
        self.__process_container(gui_or_element)
        self.__gui_def = gui_def
        if self.__container_type == "gui":
            self.__finder = GuiEmdFinder(self.__gui)
        else:
            self.__finder = GuiElementEmdFinder(self.__container)

    def _get_gui_def(self):
        return self.__gui_def

    def __process_container(self, gui_or_element):
        from .gui import Gui
        if isinstance(gui_or_element, Gui):
            if not gui_or_element._root_element:
                self.__container_type = "gui"
                self.__container = gui_or_element
                self.__gui = gui_or_element
            else:
                self.__container_type = "element"
                self.__container = gui_or_element._root_element
                self.__gui = gui_or_element
        else:
            self.__container_type = "element"
            self.__container = gui_or_element 
            self.__gui = gui_or_element.gui  
        self.__loaded = True         

    def formatter(self, **fargs) -> GNSLabelFormatter:
        '''
            Create a :class:`~arjuna.tpi.guiauto.meta.formatter.GNSLabelFormatter` object.

            Keyword Arguments:
                **fargs: Arbitrary key-value pairs to be used for formatting identifiers in `GuiWidgetLocator`.
        '''
        return GNSLabelFormatter(self, **fargs)

    def __get_wmd_for_label(self, label):
        wmd = self.__gui_def.get_wmd(label)
        return wmd.create_formatted_wmd() # Only globals will be processed.

    def wait_until_absent(self, *labels):
        '''
            Wait until `GuiWidget` corresponding to any of the GNS labels is present.

            Args:
                *labels: One or more GNS labels.

            Note:
                By default Wait is done until `ArjunaOption.GUIAUTO_MAX_WAIT` in the `Configuration` object associated with this `GuiAppContent`.

                You can provide `max_wait` key-value for GNS label(s) in GNS file to change this. Value is considered in seconds.
        '''
        waiter = getattr(self.__container, "_" + "wait_until_absent")
        for label in labels:
            wmd = self.__get_wmd_for_label(label)
            try:
                waiter(wmd)
            except GuiWidgetPresentError:
                raise GuiWidgetForLabelPresentError(self.__gui, label)    

    def contains(self, *labels):
        '''
            Check whether this `GuiAppContent` object contains a `GuiWidget` corresponding to any of the GNS labels. Includes dynamic waiting.

            Keyword Arguments:
                *labels: One or more GNS labels.

            Note:
                By default Wait is done until `ArjunaOption.GUIAUTO_MAX_WAIT` in the `Configuration` object associated with this `GuiAppContent`.

                You can provide `max_wait` key-value for GNS label(s) in GNS file to change this. Value is considered in seconds.
        '''
        for label in labels:
            try:
                getattr(self, label)
            except GuiWidgetForLabelNotPresentError:
                continue
            else:
                return True
        return False

    def _locate_with_wmd(self, wmd):
        factory = getattr(self.__finder, wmd.meta["type"].name.lower())
        return factory(wmd)

    def __getattr__(self, label):
        wmd = self.__get_wmd_for_label(label)
        from arjuna import log_debug
        log_debug("Finding element with label: {} and wmd: {}".format(label, wmd))
        try:
            return self._locate_with_wmd(wmd)
        except ArjunaTimeoutError:
            raise GuiWidgetForLabelNotPresentError(self.__gui, label)
