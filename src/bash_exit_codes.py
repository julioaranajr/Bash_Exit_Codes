"""Test exit codes in bash commands."""


import subprocess


def test_exit_codes(command):
    """Test exit codes in bash commands."""
    exit_codes = {
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
            result = subprocess.run(command, shell=True, check=True)
            exit_code = result.returncode
        except subprocess.CalledProcessError as e:
            exit_code = e.returncode

        review_you_code = 'Unknown exit code'
        meaning = exit_codes.get(exit_code, review_you_code)
        print(f'Exit code: {exit_code} ({meaning})')


try:
    print('\n')
    print('Testing exit codes')
    print('=' * 79)
    test_exit_codes('echo "Hello, World!"')
    print('-' * 79)
    test_exit_codes('exit 257')
    print('-' * 79)
    test_exit_codes('exit 3.1416')
    print('-' * 79)
    test_exit_codes('exit 31245')
    print('-' * 79)
    test_exit_codes('apt update')
    print('-' * 79)
    test_exit_codes('/dev/null')
    print('-' * 79)
    test_exit_codes('illegal_command')
    print('-' * 79)
    test_exit_codes('exit 128')
    print('-' * 79)
    test_exit_codes('exit 130')
    print('-' * 79)
    test_exit_codes('exit 999')
    print('-' * 79)
    test_exit_codes('exit 255')
    print('-' * 79)
except OSError as e:
    print(f'Error: {e}')
