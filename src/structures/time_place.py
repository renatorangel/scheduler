from constraint import Domain


class DomainTimePlace():

    """Define a domain."""

    def __init__(
            self, building, room, start_time, end_time, dayOfWeek, isInComputerLab):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        building        string      'CHEK'
        room            string      '201'
        time            string      '11:00', '13:30'
        dayOfWeek       string      'Monday'
        isComputerLab   boolean       False
        """

        self.building = building
        self.room = room
        self.startTime = start_time
        self.endTime = end_time
        self.dayOfWeek = dayOfWeek
        self.isInComputerLab = isInComputerLab
