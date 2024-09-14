"""Module to test exit codes in bash commands."""


import subprocess

from stringcolor import cs


class OutputCodes:
    """
    Class to test exit codes in bash commands.

    Attributes:
        command (str): The command to run in the bash shell.

    Methods:
        get_output_code: Get the output code of the command.

    Exceptions:
        CalledProcessError: If the command is not found.
        TimeoutExpired: If the command takes too long to execute.

    Returns:
        The exit code of the command.
    """

    def __init__(self, command):
        """Initialize the command."""
        self.command = command


    def get_output_code(self):
        """Output the exit codes."""
        codes = {
            0: 'Success',
            1: 'General error',
            2: 'Misuse of shell builtins',
            13: 'Check the permissions',
            100: 'Command not found',
            126: 'Command invoked cannot execute',
            127: 'Command not found',
            128: 'Invalid exit argument',
            130: 'Script terminated by Control-C',
            255: 'Exit status out of range',
        }

        for code in range(1):
            try:
                subprocess.run(self.command, shell=True, check=True)
                print(cs(f'Code: {code} ({codes[code]})', 'green'))
            except subprocess.CalledProcessError as e:
                print(cs(
                    f'Code: {e.returncode} ({codes[e.returncode]})', 'red'))


try:
    OutputCodes('exit 0').get_output_code()
    OutputCodes('exit 257').get_output_code()
    OutputCodes('exit 2').get_output_code()
    OutputCodes('exit 13').get_output_code()
    OutputCodes('exit 100').get_output_code()
    OutputCodes('exit 126').get_output_code()
    OutputCodes('exit 127').get_output_code()
    OutputCodes('exit 128').get_output_code()
    OutputCodes('exit 130').get_output_code()
    OutputCodes('exit 255').get_output_code()
    OutputCodes('exit 256').get_output_code()
except TypeError as e:
    print(cs(f'Error: {e}', 'red'))
except subprocess.CalledProcessError as e:
    print(cs(f'Error: {e}', 'red'))
except subprocess.TimeoutExpired as e:
    print(cs(f'Error: {e}', 'red'))
