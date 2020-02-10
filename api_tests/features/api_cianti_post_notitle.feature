@api
Feature: Post no title
    post a new name at the id 1 without title

 Scenario: Post
    Given connect with api
    When request /users
    Then post without title