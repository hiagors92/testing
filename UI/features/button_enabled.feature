Feature: Button behaviour

  Scenario: Button not be enabled until username and password be fields
    Given the user is on the login page
    When not field username and password
    Then login button should be disabled

