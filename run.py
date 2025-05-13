import pytest
import os

if __name__ == "__main__":
    pytest.main(['-s', '-v', '--alluredir=reports/allure_report', 'testcase/'])
    os.system('allure generate reports/allure_report -o reports/allure_report/html --clean')