import unittest

from tests.Login.Login_with_username_pwd import *
from tests.Login.Login_with_link import *

if __name__ == '__main__':

    """ get all tests """
    login_usr_pw = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    login_link = unittest.TestLoader().loadTestsFromTestCase(LoginTest1)

    """ create a tests suite """
    test_suite_login_usr_pw = unittest.TestSuite([login_usr_pw])
    test_suite_login_link = unittest.TestSuite([login_link])

    """" run the suite """
    unittest.TextTestRunner().run(test_suite_login_usr_pw)
    unittest.TextTestRunner().run(test_suite_login_link)
