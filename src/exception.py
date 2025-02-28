import sys
import logging

# Configure logging to print messages
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def error_message_detail(error, error_detail: sys):
    """Extracts file name, line number, and error message."""
    _, _, exc_tb = error_detail.exc_info()  # Get traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract filename

    error_message = "Error occurred in python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

