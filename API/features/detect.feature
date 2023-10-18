Feature: Detect Language for Translation

  Scenario: Detect language successfully
    Given the Translate API endpoint
    When a POST request is sent with correct parameters
    Then the response status should be 200
    And the correct language is detected

  Scenario: Different languages
    Given the Translate API endpoint
    When a POST request is sent in different languages to translate
    Then the response status should be 200
    And the PT language is detected

  Scenario: Post with incorrect parameters on header
    Given the Translate API endpoint
    When a POST request is sent with incorrect header parameters
    Then the response status should be 403

  Scenario: Post without key on header
    Given the Translate API endpoint
    When a POST request is sent without a key in the header
    Then the response status should be 401

  Scenario: Post with more parameters than expected on headers
    Given the Translate API endpoint
    When a POST request is sent with more parameters than expected in the header
    Then the response status should be 500

  Scenario: Post request without payload
    Given the Translate API endpoint
    When a POST request is sent without a payload
    Then the response status should be 502

  Scenario: Post request with special character
    Given the Translate API endpoint
    When a POST request is sent with text containing special characters
    Then the response status should be 200
    And the correct language is detected

  Scenario: Stress Post
    Given the Translate API endpoint
    When a lot of POST requests are sent
    Then the response status should be 200
