import re

from behave import step
from playwright.sync_api import expect

from features.pages.home_page import HomePage


@step('I am on the home page')
def step_impl(context):
    context.home_page = HomePage(context.browser)
    context.last_page = context.home_page.goto()


@step('I click on the puppy "{puppy_name}"')
def step_impl(context, puppy_name):
    context.home_page.select_puppy_by_name(puppy_name)


@step('I click on "Home"')
def step_impl(context):
    context.last_page = context.home_page.navigate_home()


@step('I see the profile page')
def step_impl(context):
    expect(context.last_page).to_have_title(re.compile('Profile'))


@step('I see the home page')
def step_impl(context):
    expect(context.last_page).to_have_title(re.compile('ATDD Puppy Adoption'))
