# CIandT


Welcome to the CI&T QA's Challenge
Deadline: 02/02




Hey there! We are very proud to have you here!

First, congratulations to be elected for this challenge. It's important to mention that we have created this project to assess your level
 of comprehension in software testing and automation. Keep in mind that our evaluation goes beyond the 'working code'. We want to see how well you organize yourself, your code and your time.
Important notes:


Do not worry about writing too much
 code. Sometimes, less is more.



We'll evaluate your code even if it's
 not totally running.



Feel free to contact us in case of questions.



Read with attention to all the instructions
 in the section Instructions
 below before pushing it.


What do we expect to see?


QA mindset! Do as you do in your day:
 identify tests cases!



Tests in English features and steps based
 on BDD. You can use plain text if you are not comfortable with the Gherkin structure.
You don't need to be an automation expert,
 we want to check how much you already know or can find out how to do.



Even if you don't have enough time, or
 if you don't know how to do all the challenges, we will analyze anything
 that you deliver.



Try to use the Cucumber framework.



Suggested languages: Java, Python, Ruby,
 PHP, Javascript, Typescript



Suggested frameworks: Robot, Rest Assured,
 Newman, Selenium, Cypress, Nightwatch



Maybe you can find some strange behavior
 or bugs, use them to show how you usually deal with them (registering, analysing, following the fix, measuring, …).


So good luck! We are looking forward to having you
 here with us!

Instructions

Create a repository with the following
 structure on GitHub, GitLab or BitBucket:





Make your changes as requested in section
Challenges.



Share your repository with us (don’t
 worry about problems involving github, gitlab or bitbucket, share your code on zip if necessary).


Breath, relax first and good work!


Challenges
UI Tests
In the "ui_tests" folder, include one or more files
 documenting 10 possible test cases to verify this page http://automationpractice.com/index.php.
 Try automate some of them.


API Tests
On "api_tests" folder, using Cucumber on any language
 you want, include your source code to test JSON Place Holder API, considering:

Host:
https://jsonplaceholder.typicode.com/

Feel free to include other validations.

GET /users

1. All users must have a name, username, and
 email.


2. Their Email must be valid.

    

3. Their Company catchphrase must have less
 than 50 characters.


POST /posts

1. Save a new post using a userId got by "GET
 /users" API.


2. When trying to save a new post without the
 title, API must return an error.


Extra Tests
If you want, create a new folder on this repository
 and include a SoapUI project or a Postman project doing the same tests done on "Automated Tests" session.

