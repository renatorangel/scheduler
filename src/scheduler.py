from constraint import *
from preProcessing import *
from schedulerClasses import *

#create variables


variables = []

#create test domains
domains = []


#match variable with domain
# do this so every course goes with the specific domain
matches = []
for var in variables:
    obj = ObjectScheduler(var, domains)
    matches.append(obj)

matches = preProcessing(matches)

problem = Problem()

for obj in matches:
    # domains have been pre-processed, now add the variables to the problem
    problem.addVariable(obj.variable,obj.listDomains)
    
#two different courses can't be at same room and time and day
problem.addConstraint(AllDifferentConstraint())


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

for result in problem.getSolutions():
    for k in result.keys():
        print k.title, result[k].building + result[k].room + result[k].dayOfWeek + str(result[k].start_time)
    print "------------------------------------"
