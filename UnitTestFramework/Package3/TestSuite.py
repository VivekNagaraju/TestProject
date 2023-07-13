import unittest
from Package1.LoginTest import TestLogin
from Package1.Navigation import TestNavigation
from Package2.ApplyLeave import TestLeave
from Package2.TimeSheet import TestTimesheet

# testCases=unittest.TestLoader.getTestCaseNames(TestLogin)
# print(testCases)

'''I'm loading test cases from all the modules'''
loader=unittest.TestLoader()
LoginTestCases=loader.loadTestsFromTestCase(TestLogin)
NavigationTestCases=loader.loadTestsFromTestCase(TestNavigation)
LeaveTestCases=loader.loadTestsFromTestCase(TestLeave)
TimeSheetTestCases=loader.loadTestsFromTestCase(TestTimesheet)

print("LoginTestCases",LoginTestCases)

'''Let's create test suites'''
sanityTestSuite=unittest.TestSuite()
sanityTestSuite.addTests(LoginTestCases)
sanityTestSuite.addTests(NavigationTestCases)

functionalTestSuite=unittest.TestSuite()
functionalTestSuite.addTests(LeaveTestCases)

regressionTestSuite=unittest.TestSuite()
regressionTestSuite.addTests(TimeSheetTestCases)


print("sanityTestSuite",sanityTestSuite)

'''Let's run a particular test suite'''
unittest.TextTestRunner().run(sanityTestSuite)