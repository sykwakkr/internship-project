from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import logger
import os


# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def browser_init(context, browser='chrome'):
    """
    :param context: Behave context
    :param browser: Browser to use
    :param os: Operating System (window, OS X)
    :param osVersion: Operating System version (11, sonoma)
    """
    bs_user = 'j*****'
    bs_key = 'X*****'
    bs_url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.browser_mode = browser

    desired_cap = {
        'os': os.getenv('bs_os', 'windows'),
        'osVersion': os.getenv('bs_osVersion', '11'),
        'browserName': browser.split('_')[0],
        'sessionName': 'Internship-Project Features',
    }

    if browser.startswith('chrome'):
        driver_path = ChromeDriverManager().install()
        service = ChromeService(driver_path)
        options = ChromeOptions()
        if 'headless' in browser:
            options.add_argument('--headless')
            context.driver = webdriver.Chrome(service=service, options=options)
        elif 'cloud' in browser:
            options.set_capability('bstack:options', desired_cap)
            context.driver = webdriver.Remote(command_executor=bs_url, options=options)
        elif 'mobile' in browser:
            mobile_emulation = {'deviceName': 'Nexus 5'}
            options.add_experimental_option('mobileEmulation', mobile_emulation)
            if 'bstack' in browser:
                options.set_capability('bstack:options', desired_cap)
                context.driver = webdriver.Remote(command_executor=bs_url, options=options)
            else:
                context.driver = webdriver.Chrome(service=service, options=options)
        else:
            context.driver = webdriver.Chrome(service=service)
    elif browser == 'safari':
        context.driver = webdriver.Safari()
    elif browser == 'edge':
        driver_path = '/Users/jkwak/Desktop/QA/python-selenium-automation/drivers/msedgedriver'
        service = EdgeService(executable_path=driver_path)
        context.driver = webdriver.Edge(service=service)
    elif browser.startswith('firefox'):
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        options = FirefoxOptions()
        if 'headless' in browser:
            options.add_argument('--headless')
            context.driver = webdriver.Firefox(service=service, options=options)
        elif 'cloud' in browser:
            options.set_capability('bstack:options', desired_cap)
            context.driver = webdriver.Remote(command_executor=bs_url, options=options)
        else:
            context.driver = webdriver.Firefox(service=service)
    else:
        print(f'Browser {browser} not supported')

    if 'mobile' not in browser: context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    browser = context.config.userdata.get('browser', 'chrome_mobile_bstack')
    print('\nStarted scenario: ', scenario.name)
    logger.info('\n\n### {scenario} ###'.format(scenario=scenario.name))
    logger.info(f'Before scenario: {scenario.name}')
    browser_init(context, browser)


def before_step(context, step):
    logger.info(f'    Before step: {step.name}')
    print('\nStarted step: ', step)


def after_step(context, step):
    logger.info(f'    After step: {step.name}')
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    logger.info(f'After scenario: {feature.name}')
    print('\nFinished scenario: ', feature.name)
    context.driver.quit()
