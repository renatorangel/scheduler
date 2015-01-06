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
        
def createScheduler(schedulerVariables, schedulerDomains, listPreProcessing = None, listConstraint = None):
    matches = []
    for schedulerVariable in schedulerVariables:
        matches.append((schedulerVariable,schedulerDomains[:]))

    problem = Problem()
    
    # pre-processing
    if listPreProcessing:
        for preProcessingObj in listPreProcessing:
            matches = preProcessing(preProcessingObj, matches)
        
    for var, domain in matches:
        # domains have been pre-processed, now add the variables to the problem
        problem.addVariable(var,domain)
    
    #add schedulerConstraint
    if listConstraint:
        for constraint in listConstraint:
            problem.addConstraint(addSchedulerConstraint(constraint))
            
    printResults(problem)
    
    scheduler =  Scheduler(matches, problem)
    
    return scheduler 

# if __name__ == "__main__":
#     createScheduler()
