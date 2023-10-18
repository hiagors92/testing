Feature: consulting the available language

  Scenario: Get all language
    Given the translate API endpoint
    When a GET request is sent with correct parameters
    Then the response status should be 200
    And all languages available to translate

  Scenario: Consulting language without key on header
    Given the translate API endpoint
    When a GET request is sent without key
    Then the response status should be 401

  Scenario: Post with more parameters than expected on headers
    Given the translate API endpoint
    When a GET request is sent with more parameters than expected on headers
    Then the response status should be 429

  Scenario: Post with optional parameters field
    Given the translate API endpoint
    When a GET request is sent optional parameters field
    Then the response status should be 200

    Scenario: Stress GET
    Given the translate API endpoint
    When a lot of GET request is sent it
    Then the response status should be 200
