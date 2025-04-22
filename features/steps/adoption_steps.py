import re
import time

from behave import step
from playwright.sync_api import expect



@step('I am on the home page')
def step_impl(context):
    context.home_page.goto()


@step('I click on the puppy "{puppy_name}"')
def step_impl(context, puppy_name):
    context.home_page.select_puppy_by_name(puppy_name)


@step('I click on "Home"')
def step_impl(context):
    context.last_page = context.home_page.navigate_home()


@step('I see the profile page')
def step_impl(context):
    expect(context.page).to_have_title(re.compile('Profile'))


@step('I see the home page')
def step_impl(context):
    expect(context.last_page).to_have_title(re.compile('ATDD Puppy Adoption'))


@step('I am on the adoption page')
def step_impl(context):
    context.adoption_page.goto()


@step('I fill the form in with the following values')
def step_impl(context):
    for row in context.table:
        context.page.get_by_label(row['label']).fill(row['value'])


@step('I click on "{button_label}"')
def step_impl(context, button_label):
    context.page.get_by_text(button_label).click()


@step('I see the following form values')
def step_impl(context):
    for row in context.table:
        expect(context.page.get_by_label(row['label'])).to_have_value(
            row['expected_value']
        )
