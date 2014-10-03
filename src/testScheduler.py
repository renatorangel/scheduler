import unittest
from schedulerClasses import *
from scheduler import *
  
class TestScheduler(unittest.TestCase):
  
  
    def testCreateScheduler(self):
        variables = []
        variableScheduler = VariableScheduler("csc130", "DrShade")
        variables.append(variableScheduler)
        domains = []
        domain = DomainScheduler("building", "room", 11, 12, "dayOfWeek", True)
        domains.append(domain)
        results = createScheduler(variables, domains)
        obj_dict = {variableScheduler:domain}
        for result in results:
            self.assertEqual(result[variableScheduler], obj_dict[variableScheduler])
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

# 
# 
#     variables = []
#     variableScheduler = VariableScheduler("csc130", "DrShade")
#     variables.append(variableScheduler)
#     variableScheduler = VariableScheduler("csc232", "DrShade")
#     variables.append(variableScheduler)
# 
#     preProcessingTR = PreProcessing(variables, PreProcessing.specificDaysWeek, ["tr"])
# 
# #     
# #     preProcessing12AM = PreProcessing(variables, PreProcessing.specificHours, None, (0, 12))
# #     matchs = excludeDomain(preProcessing12AM, matchs)
# #     
# #     
# #     variables = []
# #     variableScheduler = VariableScheduler("csc-101", "DrIdontKnow")
# #     variables.append(variableScheduler)
# #     variableScheduler = VariableScheduler("csc-201", "DrIdontKnow")
# #     variables.append(variableScheduler)
# #     
# #     preProcessingTRCheek201 = PreProcessing(variables, PreProcessing.partiallySpecified, ["tuesday", "thursday"], None, ("cheek", "201"))
# #     matchs = excludeDomain(preProcessingTRCheek201, matchs)
#     
#     variables = []
#     variableScheduler = VariableScheduler("csc-301", "DrLloid")
#     variables.append(variableScheduler)
#     
#     preProcessingNotInComputerLab = PreProcessing(variables, PreProcessing.notInComputerLab)
#     matchs = excludeDomain(preProcessingNotInComputerLab, matchs)
