from schedulerConstraint import *
from preProcessing import *
from schedulerClasses import *
from constraint import *

def printResults(problem):
    for result in problem.getSolutions():
        print "------------------------------------"
        for k in result.keys():
            print "Course: ", k.title
            print "Building: ", result[k].building
            print "Room: ", result[k].room
            print "Day: ", result[k].dayOfWeek, "Hour: ", result[k].startTime  
        
def createScheduler(schedulerVariables, schedulerDomains, listPreProcessing = None, listConstraints = None):
    matches = []
    for schedulerVariable in schedulerVariables:
        matches.append(Scheduler(schedulerVariable,schedulerDomains[:]))

    problem = Problem()
    
    # pre-processing
    if listPreProcessing:
        for preProcessingObj in listPreProcessing:
            matches = preProcessing(preProcessingObj, matches)
        
    for obj in matches:
        # domains have been pre-processed, now add the variables to the problem
        problem.addVariable(obj.variable,obj.listDomains)
    
    #add schedulerConstraint
    if listConstraints:
        for constraint in listConstraints:
            problem.addConstraint(addSchedulerConstraint(constraint))
            
    printResults(problem)
    return problem.getSolutions()  

if __name__ == "__main__":
    createScheduler()
