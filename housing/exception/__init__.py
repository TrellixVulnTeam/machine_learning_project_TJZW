#from asyncore import file_dispatcher
import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message:Exception object
        error_detail:object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info()

        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in scrip: [{file_name}] at line number: [{try_block_line_number}] and exception block line number:[{exception_block_line_number}] error message:[{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self)-> str:
        return HousingException.__name__.str()
