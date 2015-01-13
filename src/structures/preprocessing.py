from structures.scheduler import *


class SchedulerPreProcessing():
    # types of pre processing
    specificDaysWeek = 1
    specificHours = 2
    notInComputerLab = 3
    partiallySpecified = 4

    def __init__(self, variables, typeP, days=None, hours=None,
                 localization=None):
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
        if typeP == SchedulerPreProcessing.specificDaysWeek:
            self.days = days
        if typeP == SchedulerPreProcessing.specificHours:
            self.start, self.end = hours
        if typeP == SchedulerPreProcessing.partiallySpecified:
            self.days = days
            self.building, self.room = localization


def testTypeProcessing(domain, preProObj):
    if preProObj.type == SchedulerPreProcessing.specificDaysWeek:
        if domain.dayOfWeek in preProObj.days:
            return True

    elif preProObj.type == SchedulerPreProcessing.specificHours:
        if preProObj.start <= domain.time and preProObj.end >= domain.time:
            return True

    elif preProObj.type == SchedulerPreProcessing.partiallySpecified:
        if preProObj.room != domain.room or preProObj.building != domain.building\
                or not domain.dayOfWeek in preProObj.days:
            return True

    elif preProObj.type == SchedulerPreProcessing.notInComputerLab:
        return domain.isComputerLab
    return False


def excludeDomain(preProcessingObj, matchs):
    for var in preProcessingObj.variables:
        indexes = []
        for index, matchItem in enumerate(matchs):
            if matchItem.variable.title == var.title:
                for i, domainItem in enumerate(matchItem.listDomains):
                    if testTypeProcessing(domainItem, preProcessingObj):
                        indexes.append(i)
                for a in reversed(indexes):
                    matchs[index].listDomains.pop(a)
    return matchs


def preProcessing(matchs, preProcessing):

    return excludeDomain(preProcessing, matchs)
