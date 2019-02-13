"""Read and Format Input"""
import os
import re

class InputFormatter:
    """This class contains methods to read file and format the input sessions"""

    def __init__(self):
        """Init"""
        pass

    def read_input_file( self, input_file_path ):
        """Opens and reads a file"""
        file_object = open( input_file_path )
        return file_object

    def format_input_file( self, format_input_file):
        """Format input file"""
        session_list = []
        for each_session in format_input_file:
            if each_session not in ['\n', '\r\n']:
                if self.generate_session(each_session):
                    session_list.append(self.generate_session(each_session))

        return session_list
        
    def generate_session( self, each_session):
        """split session desc into title and time"""
        each_session=each_session.replace('lightning','5min')
        formatted_session = re.match(r'([a-zA-Z]+.*?\s)(\d+)',each_session)
        if formatted_session:
            session_titles_and_time = []
            session_titles_and_time = [formatted_session.group(1).strip(), int(formatted_session.group(2))]       
            return session_titles_and_time