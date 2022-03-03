@api
Feature: Post
    post a new name at the id 1

 Scenario: Post
    Given connect with api
    When request /users
    Then post the new name and verify the match