Feature: Registration Feature

  Scenario Outline: Validating the Registration Feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<Phone number>"
    And I enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the submit button

    Examples:
      | name    | Phone number | email                | country | city   | username  | password  |
      | Arjun   |   9711111558 | test1@automation.com | India   | Delhi  | asdsds343 | asdfsdfdf |
      | Miryala |   9711911558 | test2@automation.com | Germany | Berlin | adfc3434c | werwerwer |

# pip freeze >requirements.txt
# pip install -r requirements.txt  
# to run this feature in terminal run  --> behave features/myFeature.feature
# to generate allure report run --> behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features
# to see reports run --> allure serve allure_reports