

class Student:

    def __init__(self):
        self.lastname        = None
        self.firstName       = None
        self.username        = None
        self.studentID       = None
        self.lastAccess      = None
        self.availability    = None
        self.assignment      = None
        self.gradingNotes    = None
        self.notesFormat     = None
        self.feedbackToUser  = None
        self.feedbackFormat  = None

    def addAttributes(self):
        """ populates the class variables with the default settings 
            from the csv file
        """

    def getGrade(self):
        """Student goes into their directory and finds the grade in the 
            grading rubic and add the grade to self.assignment

        """
        
    def getNotes(self):
        """Student goes into their directory and addes the notes from their
            assignent to the self.feedbackToUse
        """

    def makeString(self):
        """returns the csv string needed to upload the students information"""

