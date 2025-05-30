Feature: As a dog lover
  I want to adopt a puppy
  So that I have a loyal companion

  Scenario: #1 Be able to view the details of a puppy
    Given I am on the home page
    When I click on the puppy "Brook"
    Then I see "Adopt Me!"

  @future
  Scenario: #2 Be able to return to the view of all available puppies
    Given I am on the home page
    When I click on the puppy "Brook"
    And I click on "Return to List"
    Then I am on the home page

  @future
  Scenario: #3 Be able to add the puppy to adopt later
    Given I am on the home page
    When I click on the puppy "Brook"
    And I click on "Adopt Me!"
    Then I see the puppy "Brook" is in my litter

  @future
  Scenario: #4 Be able to change my mind about adopting a puppy
    Given I have added a puppy to my litter
    When I click on "Change Your Mind"
    Then I see the home page

  @future
  Scenario: #5 Be able to add another puppy to my litter
    Given I have added a puppy to my litter
    When I click on "Adopt Another Puppy"
    And I click on the puppy "Ruby Sue"
    And I click on "Adopt Me!"
    Then I see the puppy "Ruby Sue" is in my litter

  @future
  Scenario: #6 Be able to change my mind removes all puppies from my litter
    Given I have added a puppy to my litter
    And I click on "Adopt Another Puppy"
    And I click on the puppy "Ruby Sue"
    And I click on "Adopt Me!"
    When I click on "Change Your Mind"
    Then I see the home page
    And I see "Your litter has been cleared"

  @future
  Scenario: #7 Add accessories to a puppy and the price change is reflected
    Given I have added a puppy to my litter
    When I add a "Collar & Leash - $9.99" to my order
    And I add a "Chew Toy - $10.95" to my order
    Then I see "$55.89"

  @future
  Scenario: #8 Complete an adoption
    Given I have added a puppy to my litter
    When I click on "Complete the Adoption"
    And I fill the form in with the following values:
      | label        | value           |
      | Name         | Joe Sixpack     |
      | Address      | 123 Main St.    |
      | Email        | joe@sixpack.com |
      | Payment Type | Check           |
    And I click on "Place Order"
    Then I see "Thank you for adopting a puppy!"

  @future
  Scenario Outline: #9 All fields are required to complete an adoption
    Given I have added a puppy to my litter
    When I click on "Complete the Adoption"
    And the order form is completely filled in
    But I blank out "<label>"
    And I click on "Place Order"
    Then I see "<error>"

    Examples:
      | label        | error          |
      | Name         | can't be blank |
      | Address      | can't be blank |
      | Email        | can't be blank |
      | Payment Type | can't be blank |


