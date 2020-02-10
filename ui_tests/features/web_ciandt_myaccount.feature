@web @ciandt
Feature: My account page

   As an user logged i want to navigate to My account page
   Acceptance criteria: the page My account should display the options 

    Scenario: My account page
        Given web address "http://automationpractice.com/index.php"
        Given login name "allan.barroso@outlook.com" and password newstar1541
        When i press the sing in button
        When i navigate to my account page
        Then i should see the page with the options to my account
    