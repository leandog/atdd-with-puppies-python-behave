import re

from behave import step
from playwright.sync_api import expect

@when(u'I go to the LeanDog website')
def step_impl(context):
    context.page.goto("https://www.leandog.com/")


@step('I see "{expected_text}"')
def step_impl(context, expected_text):
    expect(context.page.get_by_text(expected_text)).to_be_visible()
