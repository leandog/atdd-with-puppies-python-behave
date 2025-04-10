from datetime import datetime
import logging
from playwright.sync_api import sync_playwright


def before_all(context):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=1000, channel="chrome")
    context.page = browser.new_page()

def after_all(context):
    context.page.close()
    print("\nAfter all Features")

def before_feature(context, feature):
    # Create logger
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def after_feature(context, feature):
    print("\nAfter Feature")


def before_scenario(context, scenario):
    print("Before scenario\n")


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = f'failure_screenshots/{scenario.name}_{timestamp}.png'
        context.page.screenshot(path=screenshot_path)
    print("After scenario\n")


def before_step(context, step):
    print("After step\n")


def after_step(context, step):
    print("After step\n")
