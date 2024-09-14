# Bash exit codes

This is a list of exit codes that can be used in Bash scripts. The list is not exhaustive, but it covers the most common exit codes.

## What Are Exit Codes on Linux?

Exit codes are a number between `0` and `255` that are returned by a script or command. They are used to indicate the outcome of a script or command. By convention, an exit code of `0` indicates success, and any other value indicates failure. Exit codes are used to indicate the success or failure of a script or command. They are a way to communicate the outcome of a script or command to the caller.

## Why Are Exit Codes Important?

Exit codes are a way to communicate the outcome of a script or command to the caller. They are a way to indicate success or failure of a script or command. By convention, an exit code of `0` indicates success, and any other value indicates failure. This allows the caller to take appropriate action based on the exit code.

## Exit Codes

| Exit Code Number | Meaning                        | Comments                                                                                                    |
| ---------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| 1                | Catchall for general errors    | Miscellaneous errors, such as "divide by zero" and other impermissible operations                           |
| 2                | Misuse of shell builtins       | Missing keyword or command, or permission problem (and diff return code on a failed binary file comparison) |
| _124_            | You need to be root            | System script started as a non-root user                                                                    |
| _125_            | Unconfigured                   | Missing configuration file or value                                                                         |
| 126              | Command invoked cannot execute | Permission problem or command is not an executable                                                          |
| 127              | "command not found"            | Possible problem with `$PATH` or a typo                                                                     |
| 128              | Invalid argument to exit       | exit takes only integer args in the range 0 - 255                                                           |
| 128+n            | Fatal error signal "n"         | `$?` returns 137 (128 + 9)                                                                                  |
| 130              | Script terminated by Control-C | Control-C is fatal error signal 2, (130 = 128 + 2, see above)                                               |
| 255              | Exit status out of range       | exit takes only integer args in the range 0 - 255                                                           |

## How the Exit Codes help us?

- **Debugging**: Exit codes can be used to debug scripts. If a script is not working as expected, you can use the exit code to determine where the problem is.

- **Error Handling**: Exit codes can be used to handle errors in scripts. If a command fails, you can use the exit code to take appropriate action.

- **Automation**: Exit codes can be used to automate tasks. For example, you can use the exit code to determine if a script was successful and take appropriate action based on the exit code.

- **Logging**: Exit codes can be used to log the outcome of a script. You can use the exit code to determine if a script was successful and log the outcome.

- **Monitoring**: Exit codes can be used to monitor scripts. You can use the exit code to determine if a script was successful and take appropriate action based on the exit code.

- **Reporting**: Exit codes can be used to report the outcome of a script. You can use the exit code to determine if a script was successful and report the outcome.

## Conclusion

> Exit codes are a way to communicate the outcome of a script or command to the caller.

- They are a way to indicate success or failure of a script or command. By convention, an exit code of `0` indicates success, and any other value indicates failure.

- Exit codes are used to indicate the success or failure of a script or command. They are a way to communicate the outcome of a script or command to the caller.

## References

Source: [Advanced Bash-Scripting Guide Appendix E.](https://www.tldp.org/LDP/abs/html/exitcodes.html)

---

## Python-Unittest

### How to run tests

1. install `unittest` by command

    ```bash
    pip install unittest
    ```

2. run test by command

    ```bash
    python3 -m unittest -vvvv test/test_exitcodes.py test/test_mock_exitcodes.py
    ```
