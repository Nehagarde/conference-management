"""Run Application from Here"""

from input_formatter import InputFormatter
from process_sessions import ProcessSessions
from scheduled_session_printer import ScheduledSessionPrinter

class ConferenceManagement:
    """This class performs all the operations and is the main executable
    """

    def __init__(self):
        pass

    def read_inputs_from_file(self, input_file_path):
        """opens and Reads inputs from input file
        """
        input_formatter_object = InputFormatter()
        return input_formatter_object.read_input_file( input_file_path )

    def format_inputs_to_list(self, read_file):
        """Format Input Sessions"""
        input_formatter_object = InputFormatter()
        return input_formatter_object.format_input_file( read_file )


#Main 
file_path = '/home/neha/NewConferenceManagement/test/bin/inputs/input_file_with_missing_mins.txt'

manage_conferences = ConferenceManagement()

read_file = manage_conferences.read_inputs_from_file( file_path )
formatted_input = manage_conferences.format_inputs_to_list( read_file )

if formatted_input:
    schedule_sessions = ProcessSessions()
    scheduled_sessions = schedule_sessions.process_and_schedule_sessions(formatted_input)

    print_sessions = ScheduledSessionPrinter()
    print_sessions.print_scheduled_sessions(scheduled_sessions)
else:
    print "No sessions found"