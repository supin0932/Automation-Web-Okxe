import pytest
import unittest


@pytest.mark.usefixtures("driver_class")
class MyTest(unittest.TestCase):
    def test_method1(self):
        assert self.login.username == 'tests@mail'

    def test_method2(self):
        assert self.login.password == 'password'

    def tearDown(self):
        self.login.driver.quit()


if __name__ == "__main__":
    unittest.main()
