import logging
import os

from datetime import datetime
from playwright.sync_api import sync_playwright


# behave hook functions
def before_all(context):
    p = sync_playwright().start()

    if _environment_variable_as_bool("HEADLESS", "true"):
        browser = p.chromium.launch(headless=True, channel="chrome")
    else:
        slow_mo_delay = _environment_variable_as_int('SLOW_BY', "500")
        browser = p.chromium.launch(headless=False, slow_mo=slow_mo_delay, channel="chrome")

    context.page = browser.new_page()

    context.base_url = _environment_variable_as_str("BASE_URL", "http://localhost:5063")
    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = f'failure_screenshots/{scenario.name}_{timestamp}.png'
        context.page.screenshot(path=screenshot_path)


def after_all(context):
    context.page.close()


# Private helper functions
def _environment_variable_as_str(variable: str, default: str) -> str:
    return os.getenv(variable, default)


def _environment_variable_as_bool(variable: str, default: str) -> bool:
    raw_value = _environment_variable_as_str(variable, default)
    return raw_value.lower() in ('true', '1', 'yes', 'on')


def _environment_variable_as_int(variable: str, default: str) -> int:
    raw_value = _environment_variable_as_str(variable, default)

    try:
        return int(raw_value)
    except ValueError:
        raise ValueError(f"Invalid integer value for {variable}: {raw_value}")
