@api 
Feature: Company name
    company name must have less than 50 chars

Scenario: API mail
    Given connect with api
    When request /users
    Then the company name must be less than 50 chars