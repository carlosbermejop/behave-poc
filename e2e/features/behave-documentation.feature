@online
Feature: Behave documentation website

  @smoke
  Scenario: Verify the landing page of the Behave documentation website
    Given The user navigates to the Behave documentation website
    Then They land on the welcome section

  Scenario Outline: Visit all menu items
    Given The user navigates to the Behave documentation website
    When They navigate to the <section_name> menu
    Then They are redirected to the correct page for <section_id> menu

    Examples:
      | section_name                | section_id                  |
      | Installation                | installation                |
      | Tutorial                    | tutorial                    |
      | Behavior Driven Development | behavior-driven-development |
      | Feature Testing Setup       | feature-testing-setup       |
      | Tag Expressions             | tag-expressions             |
      | Using behave                | using-behave                |
      | Behave API Reference        | behave-api-reference        |
      | Fixtures                    | fixtures                    |
      | Userdata                    | userdata                    |
