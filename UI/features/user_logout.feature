Feature: Test logout successfully

  Scenario: Successful Logout
    Given the user logged
    When click to logout
    Then Should be redirection to login page

