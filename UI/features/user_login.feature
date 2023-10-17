Feature: Test login with correct credentials

  Scenario: Successful Login
    Given the user is on the login page
    When they fill in the credentials correctly
      | user                    | password      |   
      | standard_user            | secret_sauce  |
      | performance_glitch_user | secret_sauce  |
      | visual_user             | secret_sauce  |
      | problem_user            | secret_sauce  |
      | error_user              | secret_sauce  |
    Then they should be logged in

  Scenario: Login with error message
    Given the user is on the login page
    When they fill in the credentials correctly however is blocked
      | user                    | password      |
      | locked_out_user         | secret_sauce  |
    Then should displayed error message

  Scenario: Credentials entered in reverse format it should not be possible
    Given the user is on the login page
    When change the order of credentials
      | user                    | password      |
      | secret_sauce            | standard_user  |
    Then should be view error message