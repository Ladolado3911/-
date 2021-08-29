import sys
import os
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_main_page_title import Store_Main_Page
from Test.Scripts.test_main_page import TestMainPage
import testtools as testtools

sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())

if __name__ == "__main__":

    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Store_Main_Page),
        test_loader.loadTestsFromTestCase(TestMainPage),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    try:
        parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
        parallel_suite.run(testtools.StreamResult())
    except:
        quit()
