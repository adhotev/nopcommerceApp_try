import pytest
from selenium import webdriver


# this will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption('--browser')


# this will return browser value to 'setup' method
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def setup():
    if browser == 'firefox':
        driver = webdriver.Firefox()
        print('Firefox Browser')
    else:
        driver = webdriver.Chrome()
        print('Chrome Browser')

    return driver


# ################ pyTest HTML reports ################


# It is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata = {'Project Name':'nop Commerce',
                        'Module Name': 'Customer',
                        'Tester':'Vijay'}


# It is a hook for delete/Modify environment info to HTML Report
# changed marker from @pytest.mark.optionalhook to @pytest.hookimpl(optionalhook=True)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
