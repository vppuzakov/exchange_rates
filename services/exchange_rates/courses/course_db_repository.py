__author__ = 'Vladimir I. Puzakov'


class CourseDBRepository:
    """
    Course repository
    """
    def __init__(self, host, port, dbname, user, password):
        self.host = host