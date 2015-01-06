from schedulerClasses import SchedulerConstraint
from constraint import *

def addSchedulerConstraint(constraint):
    if constraint.constraintType == SchedulerConstraint.allDiferentConstraint:
        #two different courses can't be at same room and time and day 
        return AllDifferentConstraint()
    
#problem.addConstraint(same_prof_same_time, variables)
    #problem.addConstraint(csc131_specific, "csc131")
    
    # #classes that cant take concurrently
    ######## this is taken care of with the AllDifferentConstraint()
    # def constraintR(a, b):
    #     if((a == "Cheek201-11am" or a == "Cheek202-11am") and (b == "Cheek201-11am" or b == "Cheek202-11am")):
    #         return False
    #     elif((a == "Cheek201-12pm" or a == "Cheek202-12pm") and (b == "Cheek201-12pm" or b == "Cheek202-12pm")):
    #         return False
    #     elif((a == "Cheek201-1pm" or a == "Cheek202-1pm") and (b == "Cheek201-1pm" or b == "Cheek202-1pm")):
    #         return False
    #     else:
    #         return True
    # 
    #problem.getSolutions()