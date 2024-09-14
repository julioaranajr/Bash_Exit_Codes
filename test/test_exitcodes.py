"""Unit tests for main.py"""


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

import subprocess
import unittest
from exitcodes import OutputCodes


class TestOutputCodes(unittest.TestCase):
    """Class to test OutputCodes"""

    def test_get_output_code_0(self):
        """Test the get_output_code Code 0"""
        returncode = 0
        result = OutputCodes('exit 0').get_output_code()
        self.assertNotEqual(result, 'Code: 0 (Success)')

    def test_get_output_code_1(self):
        """Test the get_output_code Code 257"""
        returncode = 257
        result = OutputCodes('exit 257').get_output_code()
        self.assertNotEqual(result, 'Code: ? - (Unknown Code)')


    def test_get_output_code_2(self):
        """Test the get_output_code Code 2"""
        returncode = 2
        result = OutputCodes('exit 2').get_output_code()
        self.assertNotEqual(result, 'Code: 2 (Misuse of shell builtins)')


    def test_get_output_code_13(self):
        """Test the get_output_code Code 13"""
        returncode = 13
        result = OutputCodes('exit 13').get_output_code()
        self.assertNotEqual(result, 'Code: 13 (Check the permissions)')


    def test_get_output_code_100(self):
        """Test the get_output_code Code 100"""
        returncode = 100
        result = OutputCodes('exit 100').get_output_code()
        self.assertNotEqual(result, 'Code: 100 (Command not found)')


    def test_get_output_code_126(self):
        """Test the get_output_code Code 126"""
        returncode = 126
        result = OutputCodes('exit 126').get_output_code()
        self.assertNotEqual(result, 'Code: 126 (Command invoked cannot execute)')


    def test_get_output_code_127(self):
        """Test the get_output_code Code 127"""
        returncode = 127
        result = OutputCodes('exit 127').get_output_code()
        self.assertNotEqual(result, 'Code: 127 (Command not found)')


    def test_get_output_code_128(self):
        """Test the get_output_code Code 128"""
        returncode = 128
        result = OutputCodes('exit 128').get_output_code()
        self.assertNotEqual(result, 'Code: 128 (Invalid exit argument)')


    def test_get_output_code_130(self):
        """Test the get_output_code Code 130"""
        returncode = 130
        result = OutputCodes('exit 130').get_output_code()
        self.assertNotEqual(result, 'Code: 130 (Script terminated by Control-C)')


    def test_get_output_code_255(self):
        """Test the get_output_code Code 255"""
        returncode = 255
        result = OutputCodes('exit 255').get_output_code()
        self.assertNotEqual(result, 'Code: 255 (Exit status out of range)')

    def test_get_output_code_256(self):
        """Test the get_output_code Code 255"""
        returncode = 256
        result = OutputCodes('exit 256').get_output_code()
        self.assertNotEqual(result, 'Code: 255 (Exit status out of range)')

if __name__ == '__main__':
    unittest.main(verbosity=4)
