import re
import time

from behave import step
from playwright.sync_api import expect

from features.pages.home_page import HomePage
from features.pages.adoption_page import AdoptionPage


@step('I am on the home page')
def step_impl(context):
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


@step('I am on the adoption page')
def step_impl(context):
    context.last_page = context.adoption_page.goto()


@step('I fill the form in with the following values')
def step_impl(context):
    print(context)
    for row in context.table:
        print(row)
    time.sleep(2)
    raise NotImplementedError(
        'STEP: Given I fill the form in with the following values'
    )


@step('I click on "Place Order"')
def step_impl(context):
    raise NotImplementedError('STEP: Given I click on "Place Order"')


@step('I see the following form values')
def step_impl(context):
    raise NotImplementedError('STEP: Then I see the following form values')
