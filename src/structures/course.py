from constraint import Variable


class Course(Variable):

    '''
        Course Object
    '''

    def __init__(self, title, professor):
        """.

        PARAMETERS      TYPE        Potential Arguments
        -----------------------------------------------
        title         string      'csc', 'phy'
        professor     string      'DrShade'

        """
        Variable.__init__(self, title)
        self.title = title
        self.professor = professor
