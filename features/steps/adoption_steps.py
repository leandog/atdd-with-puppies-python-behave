import re

from behave import step
from playwright.sync_api import expect


@step("I am on the home page")
def step_impl(context):
    context.page.goto(context.base_url)


@step('I click on the puppy "Brook"')
def step_impl(context):
    context.page.get_by_role("link", name="Brook").click()


@step('I click on "Home"')
def step_impl(context):
    context.page.get_by_role("link", name="Home").click()


@step("I see the profile page")
def step_impl(context):
    expect(context.page).to_have_title(re.compile("Profile"))


@step("I see the home page")
def step_impl(context):
    expect(context.page).to_have_title(re.compile("ATDD Puppy Adoption"))
