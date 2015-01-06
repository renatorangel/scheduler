class VariableScheduler():
    """Define a variable."""
    
    def __init__(self, title, professor):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        title         string      'csc', 'phy'
        professor     string      'DrShade'
        
        """
        self.title = title.lower()
        self.professor = professor.lower()
 

class DomainScheduler():
    """Define a domain."""
    
    def __init__(self, building, room, start_time, end_time, dayOfWeek, isInComputerLab):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        building        string      'CHEK'   
        room            string      '201'
        time            string      '11:00', '13:30'
		professor		string		'Shade'
        dayOfWeek       string      'Monday'
        isComputerLab   boolean   	False
        """
        
        self.building = building.lower()
        self.room = room.lower()
        self.startTime = start_time
        self.endTime = end_time
        self.dayOfWeek = dayOfWeek.lower()
        self.isInComputerLab = isInComputerLab
        
class Scheduler(object):
    """Define a domain."""
    
    def __init__(self, matches, problem):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        
        
        """
        
        self.matches = matches
        schedule = []
        self.allSchedules = []
        for result in problem.getSolutions():
            for k in result.keys():
                course =  k
                local = result[k]
                schedule.append((course,local))
            self.allSchedules.append(schedule.pop())

class SchedulerPreProcessing():
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
        if typeP == SchedulerPreProcessing.specificDaysWeek:
            self.days = days
        if typeP == SchedulerPreProcessing.specificHours:
            self.start, self.end = hours
        if typeP == SchedulerPreProcessing.partiallySpecified:
            self.days = days
            self.building, self.room = localization

class SchedulerConstraint():
    allDiferentConstraint = 1
    
    def __init__(self, constraintType):
        self.constraintType = constraintType