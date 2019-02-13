"""Print Processed Schedule for different days """


class ScheduledSessionPrinter:
    """This Class has function to print conferences (Tracks)
    """
    def print_scheduled_sessions(self, scheduled_list):
        """function to print scheduled sessions"""
        if len(scheduled_list):
            counter = 1
            for each_session in scheduled_list:
                print("Track no:" +str(counter))
                counter += 1
                for i in each_session:
                    print(i)
        else:
            print "No Sessions were scheduled"