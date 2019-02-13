"""This file does the main processing"""

import datetime
from generate_new_track import NewTrack 
from get_next_session import GetNextSession

class ProcessSessions:
    """This Class Processes Sessions"""

    def add_new_session_to_morning( self, new_track, new_session_title, new_session_time):
        """add seminar to morning session
        """
        allotted_session_time = datetime.datetime.strftime(new_track.morning_start_time, '%H:%M')
        new_track.total_morning_time += new_session_time
        new_track.morning_start_time = new_track.morning_start_time+datetime.timedelta(minutes=new_session_time)
        new_track.morning_session_list.append(str(allotted_session_time)+" "+str(new_session_title))
        

    def add_new_session_to_noon( self, new_track, new_session_title, new_session_time):
        """add seminar to afternoon
        """
        allotted_session_time = datetime.datetime.strftime(new_track.noon_start_time, '%H:%M')
        new_track.total_noon_time += new_session_time
        new_track.noon_start_time = new_track.noon_start_time+datetime.timedelta(minutes=new_session_time)  
        new_track.noon_session_list.append(str(allotted_session_time)+" "+str(new_session_title))
        
    
    def add_lunch_session(self, new_track):
        """add lunch session
        """
        if False == new_track.is_set_lunch:
            new_track.noon_session_list.append("12:00 Lunch")
        new_track.is_set_lunch = True

    def add_networking_event(self, new_track):
        """add networking event to noon session
        """
        if new_track.total_noon_time <= new_track.NOON_TIME_LIMIT and new_track.total_noon_time >= new_track.MORNING_TIME_LIMIT:
            allotted_session_time = datetime.datetime.strftime(new_track.noon_start_time, '%H:%M')
            new_track.noon_session_list.append(str(allotted_session_time)+" Networking Event")
        
        return (new_track.morning_session_list+new_track.noon_session_list)

    def process_and_schedule_sessions( self, formatted_session_list):
        """process session list
        """
        final_scheduled_session_list = []
        new_track = NewTrack()

        for index, item in enumerate(formatted_session_list):
            new_session = GetNextSession()
            new_session_time, new_session_title = new_session.get_session_time_and_title(item)

            if new_track.MORNING_TIME_LIMIT >= ( new_track.total_morning_time + new_session_time ):
                self.add_new_session_to_morning( new_track, new_session_title, new_session_time )
                if index == len(formatted_session_list)-1:
                    final_scheduled_session_list.append( new_track.morning_session_list+new_track.noon_session_list)

            elif new_track.NOON_TIME_LIMIT >= ( new_track.total_noon_time + new_session_time):
                self.add_lunch_session( new_track )
                self.add_new_session_to_noon( new_track, new_session_title, new_session_time )
                if index == len(formatted_session_list)-1:
                    self.add_networking_event(new_track)
                    final_scheduled_session_list.append( new_track.morning_session_list+new_track.noon_session_list)

            else:
                self.add_networking_event(new_track)
                if new_session_time <= new_track.NOON_TIME_LIMIT:
                    final_scheduled_session_list.append( new_track.morning_session_list+new_track.noon_session_list)
                    new_track = NewTrack()
                
                    if new_track.MORNING_TIME_LIMIT >= ( new_track.total_morning_time + new_session_time ):
                        self.add_new_session_to_morning( new_track, new_session_title, new_session_time )
                        if index == len(formatted_session_list)-1:
                            final_scheduled_session_list.append( new_track.morning_session_list+new_track.noon_session_list)

                    elif new_track.NOON_TIME_LIMIT >= ( new_track.total_noon_time + new_session_time):
                        self.add_lunch_session( new_track )
                        self.add_new_session_to_noon( new_track, new_session_title, new_session_time )
                        if index == len(formatted_session_list)-1:
                            self.add_networking_event(new_track)
                            final_scheduled_session_list.append( new_track.morning_session_list+new_track.noon_session_list) 
                
        return final_scheduled_session_list              