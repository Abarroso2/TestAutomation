@api 
Feature: test api connection
    Test connection with api

Scenario: API connection
    Given connect with api
    When request /users
    Then the users must be displayed