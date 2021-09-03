import unittest
import readFiles


class TestReadFiles(unittest.TestCase):
    """
    Class to test the functions on the readFiles modules
    :param unittest.TestCase: Class from the unittest module to create unit tests.
    """
    def test_get_data(self):
        """
        Test case to confirm that are getting data from the file.
        :param self:
        :return: bool True
        """
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data,readFiles.read_file("test.txt"))


if __name__ == '__main__':
    unittest.main()
