from schedulerClasses import *

class PreProcessing():
    #types of pre processing
    specificDaysWeek = 1
    specificHours = 2
    notInComputerLab = 3
    partiallySpecified = 4

    def __init__(self, variables, typeP, days=None , hours = None, localization = None):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        variables
        typeP
        days 
        hours            tuple        (0,11)
        """
        self.variables = variables
        self.type = typeP
        if typeP == PreProcessing.specificDaysWeek:
            self.days = days
        if typeP == PreProcessing.specificHours:
            self.start, self.end = hours
        if typeP == PreProcessing.partiallySpecified:
            self.days = days
            self.building, self.room = localization

def testTypeProcessing(domain,preProObj):
    if preProObj.type == PreProcessing.specificDaysWeek:
        if domain.dayOfWeek in preProObj.days:
            return True

    elif preProObj.type == PreProcessing.specificHours:
        if preProObj.start <= domain.time and preProObj.end >= domain.time :
            return True

    elif preProObj.type == PreProcessing.partiallySpecified:
        if preProObj.room != domain.room or preProObj.building != domain.building\
            or not domain.dayOfWeek in preProObj.days:
            return True

    elif preProObj.type == PreProcessing.notInComputerLab:
        return domain.isComputerLab    
    return False

def excludeDomain(preProcessingObj, matchs):
    for var in preProcessingObj.variables:
        indexes = []
        for index, matchItem in enumerate(matchs):
            if matchItem.variable.title == var.title:
                for i, domainItem in enumerate(matchItem.listDomains):
                    if testTypeProcessing(domainItem,preProcessingObj):
                        indexes.append(i)
                for a in reversed(indexes):
                    matchs[index].listDomains.pop(a)       
    return matchs

def preProcessing(matchs):
    variables = []
    variableScheduler = VariableScheduler("csc130", "DrShade")
    variables.append(variableScheduler)
    variableScheduler = VariableScheduler("csc232", "DrShade")
    variables.append(variableScheduler)

    preProcessingTR = PreProcessing(variables, PreProcessing.specificDaysWeek, ["tr"])
    matchs = excludeDomain(preProcessingTR, matchs)
    
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
    
    variables = []
    variableScheduler = VariableScheduler("csc-301", "DrLloid")
    variables.append(variableScheduler)
    
    preProcessingNotInComputerLab = PreProcessing(variables, PreProcessing.notInComputerLab)
    matchs = excludeDomain(preProcessingNotInComputerLab, matchs)
    
    
    return matchs
