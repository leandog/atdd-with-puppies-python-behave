import logging
import os
from datetime import datetime

from playwright.sync_api import sync_playwright

from features.pages.home_page import HomePage
from features.pages.adoption_page import AdoptionPage


# behave hook functions
def before_all(context):
    p = sync_playwright().start()

    if _environment_variable_as_bool('HEADLESS', 'true'):
        browser = p.chromium.launch(headless=True, channel='chrome')
    else:
        slow_mo_delay = _environment_variable_as_int('SLOW_BY', '500')
        browser = p.chromium.launch(
            headless=False, slow_mo=slow_mo_delay, channel='chrome'
        )

    context.browser = browser

    context.logger = logging.getLogger('automation_tests')
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    if scenario.status == 'failed' and hasattr(context, 'page'):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = (
            f'failure_screenshots/{scenario.name}_{timestamp}.png'
        )
        context.page.screenshot(path=screenshot_path)

    if hasattr(context, 'page'):
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
        raise ValueError(f'Invalid integer value for {variable}: {raw_value}')
