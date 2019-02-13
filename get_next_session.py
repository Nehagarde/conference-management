class GetNextSession:
    """This Class has function to set title and time of the seminars
    """
    def get_session_time_and_title(self, session):
        """This method separates out the time and title of the event
        """
        for index, session_desc in enumerate(session):
            if index == 0:
                session_title = session_desc
            elif index == 1:
                session_time = session_desc

        if 5 == session_time :
            session_title = session_title+" Lightning"
        else:
            session_title = session_title
        return session_time, session_title
