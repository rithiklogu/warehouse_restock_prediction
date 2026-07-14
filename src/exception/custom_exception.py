"""
Custom exception class.
"""

import sys


class CustomException(Exception):

    def __init__(self, error: Exception, error_detail: sys):

        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename

        line_number = exc_tb.tb_lineno

        message = (
            f"\nFile : {file_name}"
            f"\nLine : {line_number}"
            f"\nError : {error}"
        )

        super().__init__(message)