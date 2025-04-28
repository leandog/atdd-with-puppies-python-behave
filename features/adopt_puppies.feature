Feature: As a dog lover
  I want to adopt a puppy
  So that I have a loyal companion

  Scenario Outline: Be able to view the details of a puppy
    Given I am on the home page
    When I click on the puppy "<puppy_name>"
    Then I see the profile page

    Examples:
    | puppy_name |
    | Brook |

#  Scenario:  BOB Team Scenario

  Scenario: Be able to return to the view of all available puppies
    Given I am on the home page
    When I click on the puppy "Brook"
    And I see the profile page
    And I navigate "Home"
    Then I see the home page

#  Scenario: #3 Be able to add the puppy to adopt later
#    Given I am on the home page
#    When I click on the puppy "Brook"
#    And I click on "Adopt Me!"
#    Then I see the puppy "Brook" is in my litter
#
#  Scenario: #4 Be able to change my mind about adopting a puppy
#    Given I have added a puppy to my litter
#    When I click on "Change Your Mind"
#    Then I see the home page
#
#  Scenario: #5 Be able to add another puppy to my litter
#    Given I have added a puppy to my litter
#    When I click on "Adopt Another Puppy"
#    And I click on the puppy "Ruby Sue"
#    And I click on "Adopt Me!"
#    Then I see the puppy "Ruby Sue" is in my litter
#
#  Scenario: #6 Be able to change my mind removes all puppies from my litter
#    Given I have added a puppy to my litter
#    And I click on "Adopt Another Puppy"
#    And I click on the puppy "Ruby Sue"
#    And I click on "Adopt Me!"
#    When I click on "Change Your Mind"
#    Then I see the home page
#    And I see "Your cart is currently empty"
#
#  @not_ready
#  Scenario: #7 Add accessories to a puppy and the price change is reflected
#    Given I have added a puppy to my litter
#    When I add a Collar & Leash to my order
#    And I add a Chew Toy to my order
#    Then I see "$63.93"

  Scenario: TEMP #8 Complete an adoption
    Given I am on the adoption page
    And I fill the form in with the following values:
      | label     | value           |
      | Name:     | Joe Sixpack     |
      | Address:  | 123 Main St.    |
      | Email:    | joe@sixpack.com |
    And I click on "Place Order"
    Then I see "Thank you for adopting a puppy!"



#  Scenario: #8 Complete an adoption
#    Given I have added a puppy to my litter
#    When I click on "Complete the Adoption"
#    And I fill the form in with the following values:
#      | element        | value           |
#      | order_name     | Joe Sixpack     |
#      | order_address  | 123 Main St.    |
#      | order_email    | joe@sixpack.com |
#      | order_pay_type | Check           |
#    And I click on "Place Order"
#    Then I see "Thank you for adopting a puppy!"
#
#  Scenario Outline: #9 All fields are required to complete an adoption
#    Given I have added a puppy to my litter
#    When I click on "Complete the Adoption"
#    And the order form is completely filled in
#    But I blank out "<element>"
#    And I click on "Place Order"
#    Then I see "<error>"
#
#    Examples:
#      | element        | error                   |
#      | order_name     | Name cannot be blank     |
#      | order_address  | Address cannot be blank  |
#      | order_email    | Email cant be blank    |
#      | order_pay_type | Pay type can't be blank |
