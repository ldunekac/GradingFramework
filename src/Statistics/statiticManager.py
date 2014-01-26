

class statiticManager:

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

    def initializeHeaderInformation(self):
        """populates the class variables with the first line of 
            the csv file
        """

    def makeStudents(self):
        """Makes a list of students based on each line of the csv file
        """

    def gatherGradeInformatino(self):
        """calls the student class to get the grading information"""


    def makeString(self):
        """makes the stirng needed to upload the students information"""


    def makeCSV(self):
        """Makes the csv needed to upload the assignment to blackboard"""