"""Mocking subprocess.run() to test bash_exit_codes.py"""


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

import subprocess
import unittest
from unittest.mock import patch
from bash_exit_codes import test_exit_codes


class TestBashExitCodes(unittest.TestCase):

    @patch('subprocess.run')
    def test_success_exit_code(self, mock_run):
        mock_run.return_value.returncode = 0
        with patch('builtins.print') as mocked_print:
            test_exit_codes('echo "Hello World"')
            mocked_print.assert_any_call('Exit code: 0 (Success)')

    @patch('subprocess.run')
    def test_general_error_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('exit 1')
            mocked_print.assert_any_call('Exit code: 1 (General error)')

    @patch('subprocess.run')
    def test_command_not_found_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(127, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('illegal_command')
            mocked_print.assert_any_call('Exit code: 127 (Command not found)')

    @patch('subprocess.run')
    def test_invalid_exit_argument_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(128, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('exit 128')
            mocked_print.assert_any_call('Exit code: 128 (Invalid exit argument)')

    @patch('subprocess.run')
    def test_script_terminated_by_control_c_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(130, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('exit 130')
            mocked_print.assert_any_call('Exit code: 130 (Script terminated by Control-C)')

    @patch('subprocess.run')
    def test_exit_status_out_of_range_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(255, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('exit 255')
            mocked_print.assert_any_call('Exit code: 255 (Exit status out of range)')

    @patch('subprocess.run')
    def test_unknown_exit_code(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(999, 'cmd')
        with patch('builtins.print') as mocked_print:
            test_exit_codes('exit 999')
            mocked_print.assert_any_call('Exit code: 999 (Unknown exit code)')

if __name__ == '__main__':
    unittest.main(verbosity=4)
