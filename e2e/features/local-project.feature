@local
Feature: Tests against a local project

  @api
  Scenario:
    When The user calls /user/ with an username
    Then The response includes the username correctly

  @skip @api
  Scenario:
    Then This test should always be skipped