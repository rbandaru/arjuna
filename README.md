# Arjuna

Arjuna is a Python based test automation framework developed by Rahul Verma (www.rahulverma.net). Rahul has implemented smaller variants of features in Arjuna across frameworks and organizations, or given advise around it. However Arjuna being a generic library has the most complete implementation of his ideas, away from project specific contexts and constraints.

Arjuna uses **[pytest](https://docs.pytest.org/en/latest/)** as its recommended test engine. Arjuna also provides its markup for some common use cases on top of pytest. If you like, you can make use of Arjuna with any other test engine or custom frameworks as well.

You'd need Python 3.5+ to make use of Arjuna.

Note: On Linux, the built-in Python3 build has issues with the Python's built-in enum module which is heavily used in Arjuna. One alternative is to install ActiveState Python on linux. Advanced users can go for installing a custom Python build.

## Tutorial

### 1. Arjuna Installation

1. Download and install latest Python (3.5+) from https://python.org
    * If you are insterested to learn python Following are links for tutorials and docs.
    + https://docs.python.org/3.7/tutorial/index.html
    + https://docs.python.org/3.7/index.html
2. Confirm the python version installed by running the command `python --version`. If expected version in not shown, fix this by looking into PATH variables and/or to see whether you have multiple versions of Python installed.
3. Install Arjuna using the following command
    * `pip install arjuna`

### 2. Arjuna's Core Features

You can find the example code used on this section in [arjuna_core_features project](https://github.com/rahul-verma/arjuna/tree/master/arjuna-samples/arjex_core_features/tests/modules).

1. [Project Structure](https://github.com/rahul-verma/arjuna/blob/master/docs/core/ProjectStructure.md)
2. [Writing Your First Test](https://github.com/rahul-verma/arjuna/blob/master/docs/core/WritingFirstTest.md)
3. [Configuration](https://github.com/rahul-verma/arjuna/blob/master/docs/core/Configuration.md)
4. [Data Driven Testing](https://github.com/rahul-verma/arjuna/blob/master/docs/core/DataDrivenTesting.md)

### 3. Basic Web UI Automation

You can find the example code used on this section in [arjuna_webui_basics project](https://github.com/rahul-verma/arjuna//tree/master/arjuna-samples/arjex_webui_basics/tests/modules).

1. [Getting Started with WebApp](https://github.com/rahul-verma/arjuna/blob/master/docs//webui_basics/WebApp.md)
2. [GuiElement - Identification and Interactions](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_basics/GuiElement.md)
2. [Creating Reusable Module](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_basics/ReusableModule.md)
3. [GuiMultiElement](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_basics/GuiMultiElement.md)
4. [Dropdown and RadioGroup](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_basics/DropDownRadioGroup.md)

### 4. Advanced Web UI Automation
1. [Finding Nested Elements](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/FindingNestedElements.md)
2. [Alternative and Dynamic Identifiers](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/AlternativeDynamicIdentifiers.md)
3. [Executing JavaScript](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/ExecutingJavaScript.md)
4. [Alerts, Windows, Frames](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/AlertsWindowsFrames.md)
5. [Configuraing Interactions with GuiInteractionConfig](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/GuiInteractionConfig.md)
6. [Handling Custom DropDowns](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/HandlingCustomDropDowns.md)
7. [Retrieving Source code with GuiSource](https://github.com/rahul-verma/arjuna/blob/master/docs/webui_adv/GuiSource.md)

### 5. Gui Abstraction - GNS, App, Page, Widget and Gui Elements
The following tutorial sub-sections have multiple example projects corresponding to them. Please refer the pages for respective example projects.

1. [Gui Namespace (GNS) - Externalized Identifiers](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/GuiNamespace.md)
2. [Creating App Class](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/AppClass.md)
3. [Gui and Its Loading Model in Arjuna](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/GuiLoadingModel.md)
3. [App Object Model](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/AppObjectModel.md)
4. [App-Page Object Model](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/AppPageObjectModel.md)
5. [App-Page-Widget Object Model](https://github.com/rahul-verma/arjuna/blob/master/docs/gui_abstraction/AppPageWidgetObjectModel.md)

## Reference
1. [Command Line Options](https://github.com/rahul-verma/arjuna/blob/master/docs/core/CommandLineOptions.md)

### Miscellaneous
1. Using Arjuna With Your Test Framework
