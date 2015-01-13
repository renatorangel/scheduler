class Scheduler(object):

    """Define a domain."""

    def __init__(self, matches, problem):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------


        """

        self.matches = matches
        schedule = []
        self.allSchedules = []
        for result in problem.getSolutions():
            for k in result.keys():
                course = k
                local = result[k]
                schedule.append((course, local))
            self.allSchedules.append(schedule.pop())
