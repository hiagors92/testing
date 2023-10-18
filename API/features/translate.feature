Feature: text translate

  Scenario: text translate successfully
    Given the translate API endpoint
    When a POST request is sent with text
    Then the response status should be 200
    And the text translated

  Scenario: Different languages
    Given the translate API endpoint
    When a POST request is sent in different languages of english
    Then the response status should be 200
    And the text translated

  Scenario: Post with incorrect parameters on header
    Given the translate API endpoint
    When a POST request is sent with incorrect header parameters
    Then the response status should be 403

  Scenario: Post without key on header
    Given the translate API endpoint
    When a POST request is sent without key
    Then the response status should be 401

  Scenario: Post with more parameters than expected on headers
    Given the translate API endpoint
    When a POST request is sent with more parameters than expected on headers
    Then the response status should be 429

  Scenario: Post request without payload
    Given the translate API endpoint
    When a POST request is sent without payload
    Then the response status should be 429

  Scenario: Post request with special character
    Given the translate API endpoint
    When a POST request is sent with text with special characters
    Then the response status should be 200
    And the text translated

  Scenario: Stress Post
    Given the translate API endpoint
    When a lot of POST request is sent it
    Then the response status should be 200
