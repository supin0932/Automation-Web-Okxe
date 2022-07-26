import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    value = request.config.getoption("--browser")
    if value is None:
        value = "Chrome"
    return value


@pytest.fixture(scope="class")
def driver_class(request, browser):
    class Driver:
        def __init__(self):
            self.browser = browser

    # set a class attribute on the invoking tests context
    request.cls.login = Driver()
