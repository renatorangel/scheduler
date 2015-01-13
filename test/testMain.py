import unittest
from structures.scheduler import *
from main import create_scheduler
from constraint import Domain
from structures.course import Course
from structures.time_place import DomainTimePlace
from structures.scheduler_constraint import SchedulerConstraint


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.variables = []

        variable1 = Course("csc130", "sdfg")
        self.variables.append(variable1)

        variable2 = Course("csc220", "DrShade")
        self.variables.append(variable2)

        cheek_123 = DomainTimePlace("cheek", "123", 11, 12, "monday", True)
        cheek_124 = DomainTimePlace("cheek", "124", 10, 12, "monday", False)

        self.domain = Domain([cheek_123, cheek_124])

        self.listPreProcessing = []

        self.listConstraint = []
#         constraintAllDifferentConstraint = SchedulerConstraint(
#             SchedulerConstraint.allDiferentConstraint)
#         self.listConstraint.append(constraintAllDifferentConstraint)

        constraint_no_professor_same_time_local = SchedulerConstraint(SchedulerConstraint.instructor_same_time,
                                                                      [variable1, variable2])
        self.listConstraint.append(constraint_no_professor_same_time_local)

    def tearDown(self):
        pass

    def testCreateScheduler(self):

        scheduler = create_scheduler(
            self.variables,
            self.domain,
            None,
            self.listConstraint)

if __name__ == "__main__":
    unittest.main()

#
#     preProcessingTR = PreProcessing(variables, PreProcessing.specificDaysWeek, ["tr"])
#
#
#     preProcessing12AM = PreProcessing(variables, PreProcessing.specificHours, None, (0, 12))
#     matchs = excludeDomain(preProcessing12AM, matchs)
#
#
#     variables = []
#     variableScheduler = Course("csc-101", "DrIdontKnow")
#     variables.append(variableScheduler)
#     variableScheduler = Course("csc-201", "DrIdontKnow")
#     variables.append(variableScheduler)
#
#     preProcessingTRCheek201 = PreProcessing(variables, PreProcessing.partiallySpecified, ["tuesday", "thursday"], None, ("cheek", "201"))
#     matchs = excludeDomain(preProcessingTRCheek201, matchs)
#
#     variables = []
#     variableScheduler = Course("csc-301", "DrLloid")
#     variables.append(variableScheduler)
#
#     preProcessingNotInComputerLab = PreProcessing(variables, PreProcessing.notInComputerLab)
#     matchs = excludeDomain(preProcessingNotInComputerLab, matchs)
