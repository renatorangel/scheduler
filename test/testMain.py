import unittest
from schedulerClasses import *
from main import *
  
class TestScheduler(unittest.TestCase):
    
    def setUp(self):
        self.variables = []
        
        self.variable1 = VariableScheduler("csc130", "DrShade")
        self.variables.append(self.variable1)
        
        self.variable2 = VariableScheduler("csc220", "DrSmith")
        self.variables.append(self.variable2)
        
        self.domains = []
        self.domain1 = DomainScheduler("cheek", "123", 11, 12, "monday", True)
        self.domains.append(self.domain1)
        
        self.domain2 = DomainScheduler("cheek", "124", 11, 12, "monday", False)
        self.domains.append(self.domain2)
    
        self.listPreProcessing = []
        
        self.listConstraint = []
        constraint1 = SchedulerConstraint(SchedulerConstraint.allDiferentConstraint)
        self.listConstraint.append(constraint1)
        
    def tearDown(self):
        pass
  
    def testCreateScheduler(self):

        scheduler = createScheduler(self.variables, self.domains, None, self.listConstraint)
        self.obj_dict = [  [(self.variable2, self.domain2), (self.variable1, self.domain1)] , 
                          [ (self.variable2, self.domain1), (self.variable1, self.domain2) ]  ]
        
        for schedules in scheduler.allSchedules:
            for schedule in schedules:
                print "asdf"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

 
 
#     variables = []
#     variableScheduler = VariableScheduler("csc130", "DrShade")
#     variables.append(variableScheduler)
#     variableScheduler = VariableScheduler("csc232", "DrShade")
#     variables.append(variableScheduler)
#  
#     preProcessingTR = PreProcessing(variables, PreProcessing.specificDaysWeek, ["tr"])
#  
#      
#     preProcessing12AM = PreProcessing(variables, PreProcessing.specificHours, None, (0, 12))
#     matchs = excludeDomain(preProcessing12AM, matchs)
#      
#      
#     variables = []
#     variableScheduler = VariableScheduler("csc-101", "DrIdontKnow")
#     variables.append(variableScheduler)
#     variableScheduler = VariableScheduler("csc-201", "DrIdontKnow")
#     variables.append(variableScheduler)
#      
#     preProcessingTRCheek201 = PreProcessing(variables, PreProcessing.partiallySpecified, ["tuesday", "thursday"], None, ("cheek", "201"))
#     matchs = excludeDomain(preProcessingTRCheek201, matchs)
#      
#     variables = []
#     variableScheduler = VariableScheduler("csc-301", "DrLloid")
#     variables.append(variableScheduler)
#      
#     preProcessingNotInComputerLab = PreProcessing(variables, PreProcessing.notInComputerLab)
#     matchs = excludeDomain(preProcessingNotInComputerLab, matchs)
