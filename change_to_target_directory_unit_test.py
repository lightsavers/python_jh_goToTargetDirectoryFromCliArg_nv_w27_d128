'''***********************************
*
* Document: change directory to target directory, unit tests.
* Author: lightsavers
* Last update: 05/25/2022
*
***********************************'''
# import python native unit test library
import unittest

# import function from separate py file to run unit tests on
from change_to_target_directory import directoryFileOperation


class TestInputs(unittest.TestCase):

    # Test case 1
    def test_directory_entry(self):
        newDir = "C:\\Users\\Me"
        expectedDir = "C:\\Users\\Me"
        obj = directoryFileOperation()
        obj.changeDirectory(newDir)
        self.assertEqual(obj.newDir, expectedDir)


if __name__ == '__main__':
    unittest.main()