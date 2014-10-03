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
        self.start_time = start_time
        self.end_time = end_time
        self.dayOfWeek = dayOfWeek.lower()
        self.isComputerLab = isInComputerLab
        
class Scheduler(object):
    """Define a domain."""
    
    def __init__(self, variable, listDomains):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        
        
        """
        
        # String arguments are set to lowercase.
        self.variable = variable
        self.listDomains = listDomains
        
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
