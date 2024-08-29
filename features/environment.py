from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import logger


def browser_init(context, browser='chrome'):
    """
    :param browser: Browser to use
    :param context: Behave context
    """
    if browser == 'chrome':
        driver_path = ChromeDriverManager().install()
        service = ChromeService(driver_path)
        context.driver = webdriver.Chrome(service=service)
    elif browser == 'safari':
        context.driver = webdriver.Safari()
    elif browser == 'edge':
        driver_path = '/Users/jkwak/Desktop/QA/python-selenium-automation/drivers/msedgedriver'
        service = EdgeService(executable_path=driver_path)
        context.driver = webdriver.Edge(service=service)
    elif browser == 'firefox':
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        context.driver = webdriver.Firefox(service=service)
    else:
        print(f'Browser {browser} not supported')

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 4)
    context.app = Application(context.driver)


def before_scenario(context, scenario, browser='chrome'):
    print('\nStarted scenario: ', scenario.name)
    logger.info('\n\n### {scenario} ###'.format(scenario=scenario.name))
    logger.info(f'Before scenario: {scenario.name}')
    browser_init(context, browser='chrome')


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
