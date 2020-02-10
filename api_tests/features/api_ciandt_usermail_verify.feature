@api 
Feature: verify mail of users
    verify if all users mail are valid mails

Scenario: API mail
    Given connect with api
    When request /users
    Then the users mails must be valid