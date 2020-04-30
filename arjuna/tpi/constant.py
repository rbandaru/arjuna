# This file is a part of Arjuna
# Copyright 2015-2020 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum, auto

class ArjunaOption(Enum):
    '''
        Represents all built-in configuration options for Arjuna.

        Any option name which is does not correspond to ArjunaOption enum constant is treated as a user defined option.
    '''
    
    ARJUNA_ROOT_DIR = auto()
    '''Root Directory of Arjuna Installed/Imported in a session'''

    ARJUNA_EXTERNAL_IMPORTS_DIR = auto()
    '''Directory of third party libs directly included in Arjuna.'''

    LOG_NAME = auto()
    '''Name of Arjuna's log file'''

    RUN_ID = auto()
    '''An alnum string representing current test run. Default is **mrun**'''

    RUN_SESSION_NAME = auto()
    '''Current session name.'''

    RUN_HOST_OS = auto()
    '''Host Operating System type: Windows/Mac/Linux.'''

    LOG_FILE_LEVEL = auto()
    '''Minimum level for a message to be logged to log file.'''

    LOG_CONSOLE_LEVEL = auto()
    '''Minimum level for a message to be displayed on console'''

    LOG_ALLOWED_CONTEXTS = auto()
    '''Allowed context strings for logging (file as well as display). Messages without contexts always get logged.'''

    L10N_LOCALE = auto()
    '''Default Locale type to be used for Localization call. Values as per arjuna.tpi.constant.Locale'''

    L10N_STRICT = auto()
    '''Sets Localization mode to strict. Default is False.'''

    L10N_DIR = auto()
    '''Directory containing Localization files.'''

    L10N_EXCEL_DIR = auto()
    '''Directory containing Excel based Localization files.'''

    L10N_JSON_DIR = auto()
    '''Directory containing Json based Localization files.'''

    PROJECT_NAME = auto()
    '''Test Project Name'''

    PROJECT_ROOT_DIR = auto()
    '''Test Project Root Directory'''

    CONF_PROJECT_FILE = auto()
    '''Project conf file path.'''

    TESTS_DIR = auto()
    '''Directory containing test modules.'''

    HOOKS_DIR = auto()
    '''Arjuna Hooks directory.'''

    REPORTS_DIR = auto()
    '''Root directory for test reports.'''

    REPORT_FORMATS = auto()
    '''Formats for Report Generation. XML/HTML'''

    REPORT_DIR = auto()
    '''Reporting directory for current test run under REPORTS_DIR. Name is generated with RUN_ID and Current Timestamp. With --static-rid CLI switch, timestamp is not appended.'''

    REPORT_XML_DIR = auto()
    '''Directory containing report.xml for current test run.'''

    REPORT_HTML_DIR = auto()
    '''Directory containing report.html for current test run.'''

    LOG_DIR = auto()
    '''Directory containing arjuna.log for current test run.'''

    SCREENSHOTS_DIR = auto()
    '''Directory containing screenshots for current test run.'''

    CONF_DIR = auto()
    '''Test Project configuration directory'''

    CONF_DATA_FILE = auto()
    '''Directory that contains all data configurations.'''

    CONF_ENVS_FILE = auto()
    '''File that contains all environment configurations.'''

    CONF_SESSIONS_FILE = auto()
    '''File that contains all test session definitions.'''

    CONF_STAGES_FILE = auto()
    '''Directory that contains all test stage definitions.'''

    CONF_GROUPS_FILE = auto()
    '''Directory that contains all test group definitions.'''

    CONF_WITHX_FILE = auto()
    '''Path of withx.yaml file used for writing custom locators for Gui Automation.'''

    DATA_DIR = auto()
    '''Directory containing data files in test project.'''

    DATA_SRC_DIR = auto()
    '''Directory containing data source files in test project.'''

    DATA_REF_DIR = auto()
    '''Directory containing contextual data reference files in test project.'''

    DATA_REF_COLUMN_DIR = auto()
    '''Directory containing contextual column data reference Excel files in test project.'''

    DATA_REF_ROW_DIR = auto()
    '''Directory containing contextual row data reference Excel files in test project.'''

    APP_URL = auto()
    '''Base URL for a Web App. Used by launch() method if url is not specified for GuiApp.'''

    BROWSER_NAME = auto()
    '''Browser Name for Gui Automation. Chrome/Firefox. Default is Chrome'''

    BROWSER_HEADLESS = auto()
    '''Sets headless mode for browser for GUI Automation. Default is False.'''

    BROWSER_VERSION = auto()
    '''Browser Version for GUI Automation.'''

    BROWSER_MAXIMIZE = auto()
    '''Browser is maximized in GUI Automation after launch. Default is False.'''

    BROWSER_DIM_HEIGHT = auto()
    '''Browser Height for GUI Automation. If not set, Arjuna does not change the height of browser.'''

    BROWSER_DIM_WIDTH = auto()
    '''Browser Width for GUI Automation. If not set, Arjuna does not change the width of browser.'''

    BROWSER_BIN_PATH = auto()
    '''Path of the Browser binary on test system.'''

    GUIAUTO_NAME = auto()
    '''Engine name. Currently set to Selenium which is the only supported engine.'''

    GUIAUTO_DIR = auto()
    '''Root directory of all Gui automation relation directories and files'''

    GUIAUTO_NAMESPACE_DIR = auto()
    '''Root directory of all Gui Namespace (GNS) files.'''

    GUIAUTO_DEF_MULTICONTEXT = auto()
    '''Sets multi context mode for GNS files. Currently not processed.'''

    GUIAUTO_CONTEXT = auto()
    '''Gui Automation Context. Currently not processed.'''

    SCROLL_PIXELS = auto()
    '''Number of pixels for each scroll call in Gui Automation. Default is 100.'''

    GUIAUTO_MAX_WAIT = auto()
    '''Maximum time for a Gui element locating or waitable interaction to occur. Uses Dynamic Wait. Expressed in seconds. Default is 60.'''

    GUIAUTO_SLOMO_ON = auto()
    '''Sets slow motion mode for Gui Automation. Default is False.'''

    GUIAUTO_SLOMO_INTERVAL = auto()
    '''Time Interval between successive Gui Automation actions when Slow Motion mode is ON. Expressed in seconds. Default is 2'''

    MOBILE_OS_NAME = auto()
    '''Mobile OS Name. iOs/Android. Default is Android.'''

    MOBILE_OS_VERSION = auto()
    '''Mobile OS Version. No default set.'''
    
    MOBILE_DEVICE_NAME = auto()
    '''Mobile Device name. No default set.'''

    MOBILE_DEVICE_UDID = auto()
    '''Mobile Device UDID. No default set.'''

    MOBILE_APP_FILE_PATH = auto()
    '''Mobile App path on test system. No default set.'''

    SELENIUM_DRIVER_PROP = auto()
    '''Selenium Environment variable for browser driver as per chosen browser. Automatically set as per chosen browser. Default is webdriver.chrome.driver'''

    SELENIUM_DRIVERS_DIR = auto()
    '''Root Directory containing OS specific browser drivers for Selenium. Has an impact only if SELENIUM_DRIVER_DOWNLOAD is set to False.'''

    SELENIUM_DRIVER_PATH = auto()
    '''Absolute path of Selenium browser driver. Automatically set to WebDriverManager's downloaded driver if SELENIUM_DRIVER_DOWNLOAD is True, else automatically set as per the test project structure, OS and browser.'''

    SELENIUM_DRIVER_DOWNLOAD = auto()
    '''Instructs Arjuna to automatically download Selenium browser driver for chosen browser. Default is True.'''

    SELENIUM_SERVICE_URL = auto()
    '''Selenium's Service URL. If set, Arjuna does not launch the browser service and uses this URL as the service URL.'''

    APPIUM_SERVICE_URL = auto()
    '''Appium Service URL. Currently not processed.'''

    APPIUM_AUTO_LAUNCH = auto()
    '''Instructs Arjuna to launch Appium programmatically. Default is True. Currently not processed.'''

    IMG_COMP_MIN_SCORE = auto()
    '''A fraction that represents minimum image comparison score to decide on an image match. Default is 0.7. Currently not processed.'''

class TimeUnit(Enum):
    '''
        Allowed time unit types.
    '''

    MILLI_SECONDS = auto()
    SECONDS = auto()
    MINUTES = auto()

class BrowserName(Enum):
    '''
        Allowed browser names for Gui Automation.
    '''

    CHROME = auto()
    FIREFOX = auto()

import locale
import re
__locales = [i.upper() for i in locale.locale_alias.keys() if re.match('^[\w_]+$', i)]

Locale = Enum('Locale', dict(zip(__locales, range(len(__locales)))))
Locale.__doc__ = '''Allowed locale names in Arjuna.'''