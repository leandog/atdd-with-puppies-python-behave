from behave import given, when, then
from features import environment

@given(u'I am on the home page')
def step_impl(context):
    context.page.goto("http://localhost:5063")

@when(u'I click on the puppy "Brook"')
def step_impl(context):
    context.page.get_by_role("link", name="Brook").click()

@then(u'I am on the profile page')
def step_impl(context):
    # raise NotImplementedError(u'STEP: I am on the profile page')
    assert (context.page.get_by_role("heading", name="Sign up")).to_be_visible()


# @when(u'I click on "Return to List"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Return to List"')
#
#
# @then(u'I see the home page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see the home page')
#
#
# @when(u'I click on "Adopt Me!"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Adopt Me!"')
#
#
# @then(u'I see the puppy "Brook" is in my litter')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see the puppy "Brook" is in my litter')
#
#
# @given(u'I have added a puppy to my litter')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I have added a puppy to my litter')
#
#
# @when(u'I click on "Change Your Mind"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Change Your Mind"')
#
#
# @when(u'I click on "Adopt Another Puppy"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Adopt Another Puppy"')
#
#
# @when(u'I click on the puppy "Ruby Sue"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on the puppy "Ruby Sue"')
#
#
# @then(u'I see the puppy "Ruby Sue" is in my litter')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see the puppy "Ruby Sue" is in my litter')
#
#
# @given(u'I click on "Adopt Another Puppy"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I click on "Adopt Another Puppy"')
#
#
# @given(u'I click on the puppy "Ruby Sue"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I click on the puppy "Ruby Sue"')
#
#
# @given(u'I click on "Adopt Me!"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I click on "Adopt Me!"')
#
#
# @then(u'I see "Your cart is currently empty"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Your cart is currently empty"')
#
#
# @when(u'I add a Collar & Leash to my order')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I add a Collar & Leash to my order')
#
#
# @when(u'I add a Chew Toy to my order')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I add a Chew Toy to my order')
#
#
# @then(u'I see "$63.93"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "$63.93"')
#
#
# @when(u'I click on "Complete the Adoption"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Complete the Adoption"')
#
#
# @when(u'I fill the form in with the following values')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I fill the form in with the following values')
#
#
# @when(u'I click on "Place Order"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Place Order"')
#
#
# @then(u'I see "Thank you for adopting a puppy!"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Thank you for adopting a puppy!"')
#
#
# @when(u'the order form is completely filled in')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When the order form is completely filled in')
#
#
# @when(u'I blank out "order_name"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I blank out "order_name"')
#
#
# @then(u'I see "Name can\'t be blank"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Name can\'t be blank"')
#
#
# @when(u'I blank out "order_address"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I blank out "order_address"')
#
#
# @then(u'I see "Address can\'t be blank"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Address can\'t be blank"')
#
#
# @when(u'I blank out "order_email"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I blank out "order_email"')
#
#
# @then(u'I see "Email can\'t be blank"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Email can\'t be blank"')
#
#
# @when(u'I blank out "order_pay_type"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I blank out "order_pay_type"')
#
#
# @then(u'I see "Pay type can\'t be blank"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Pay type can\'t be blank"')
#
#
# @when(u'I click on the email icon')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on the email icon')
#
#
# @then(u'I see the heading "Contact"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see the heading "Contact"')
#
#
# @when(u'I click on "Send"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I click on "Send"')
#
#
# @then(u'I see "Thank you for contacting us!"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Thank you for contacting us!"')
#
#
# @when(u'the contact form is completely filled in')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When the contact form is completely filled in')
#
#
# @when(u'I blank out "contact_message_name"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When I blank out "contact_message_name"')
#
#
# @then(u'I see "Name cannot be blank"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then I see "Name can\'t be blank"')


@when(u'I blank out "contact_message_email"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I blank out "contact_message_email"')


@then(u'I see "Email can\'t be blank"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see "Email can\'t be blank"')


@when(u'I blank out "contact_message_body"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I blank out "contact_message_body"')


@then(u'I see "Body can\'t be blank"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see "Body can\'t be blank"')


@given(u'I click on "Message Boards"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I click on "Message Boards"')


@then(u'I see the heading "Message Boards"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see the heading "Message Boards"')


@when(u'I click on "Post a Message"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "Post a Message"')


@when(u'I click on "Post"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "Post"')


@then(u'I see a post with the message "Goldens are the best!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see a post with the message "Goldens are the best!"')


@given(u'I have an existing thread')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have an existing thread')


@when(u'I click on "Reply"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "Reply"')


@then(u'I see a post with the message "+1 They are so mild mannered."')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see a post with the message "+1 They are so mild mannered."')
