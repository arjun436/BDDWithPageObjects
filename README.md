1. Freeze the requirements
 pip freeze >requirements.txt
2. Install the requirements
 pip install -r requirements.txt  
3. To run this feature in terminal run from terminal --> behave features/myFeature.feature
4. To generate allure report run from terminal --> behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features
5. To see reports run --> allure serve allure_reports
