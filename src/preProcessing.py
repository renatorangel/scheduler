from schedulerClasses import *

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

def preProcessing(matchs, preProcessing):
    
    return excludeDomain(preProcessing, matchs)