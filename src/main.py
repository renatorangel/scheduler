from structures.preprocessing import *
from structures.scheduler import *
from constraint import *


def printResults(problem):
    for result in problem.getSolutions():
        for k in result.keys():
            print "----------"
            print "Course: ", k.title, "Professor: ", k.professor
            print
            print "Building: ", result[k].building, "Room: ",\
                result[k].room, "Day: ", result[k].dayOfWeek,\
                "Hour: ", result[k].startTime

        print "------------------------------------"


def create_scheduler(schedulerVariables,
                     schedulerDomains,
                     listPreProcessing=None,
                     list_constraint=None):
    matches = []
    for schedulerVariable in schedulerVariables:
        matches.append((schedulerVariable, schedulerDomains[:]))

    problem = Problem()

    # pre-processing
    if listPreProcessing:
        for preProcessingObj in listPreProcessing:
            matches = preProcessing(preProcessingObj, matches)

    for var, domain in matches:
        # domains have been pre-processed, now add the variables to the problem
        problem.addVariable(var, domain)

    # add schedulerConstraint
    if list_constraint:
        for constraint in list_constraint:
            print constraint.get_scheduler_constraint()
            constraint_asdf, list_asdf = constraint.get_scheduler_constraint()
            problem.addConstraint(constraint_asdf, list_asdf)

    printResults(problem)

    scheduler = Scheduler(matches, problem)

    return scheduler

if __name__ == "__main__":
    pass
