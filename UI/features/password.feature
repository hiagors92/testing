Feature: Password behaviour

    Scenario: When the user fill password's field then * is visible for each input
    Given the user is on the login page
    When fill password's field
        | password      |
        | 1234567       |
    Then each input should displayed *