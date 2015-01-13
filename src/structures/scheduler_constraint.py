import constraint


class SchedulerConstraint(constraint.Constraint):
    allDiferentConstraint = 1
    instructor_same_time = 2

    def __init__(self, constraint_type, list_course=None):
        self.constraint_type = constraint_type
        self.list_course = list_course

    def get_scheduler_constraint(self):
        if self.constraint_type == SchedulerConstraint.allDiferentConstraint:
            # two different courses can't be at same room and time and day
            return constraint.AllDifferentConstraint()

        if self.constraint_type == SchedulerConstraint.instructor_same_time:
            instance = constraint.FunctionConstraint(
                no_instructor_at_same_time)
            return instance, self.list_course


def no_instructor_at_same_time(time_place1, time_place2):
    if time_place1.startTime == time_place2.startTime\
            and time_place1.dayOfWeek == time_place2.dayOfWeek:
        return False
    return True
