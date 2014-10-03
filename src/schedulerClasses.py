class VariableScheduler():
    """Define a variable."""
    
    def __init__(self, title, professor):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        title         string      'csc', 'phy'
        professor     string      'DrShade'
        
        """
        # String arguments are set to lowercase.
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
        # Building code should be the four letter code (CHEK/TEMP/etc) for standardization
		# times should be in military time for easier calculation
		
        # String arguments are set to lowercase.
        self.building = building.lower()
        self.room = room.lower()
        self.start_time = start_time
        self.end_time = end_time
        self.dayOfWeek = dayOfWeek.lower()
        self.isComputerLab = isInComputerLab
        
class ObjectScheduler(object):
    """Define a domain."""
    
    def __init__(self, variable, listDomains):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        
        
        """
        
        # String arguments are set to lowercase.
        self.variable = variable
        self.listDomains = listDomains


