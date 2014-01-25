from os import mkdir, remove
from shutil import copy
from zipfile import ZipFile
from FormatModule.config import Config
from FormatModule.StudentFormat.studentManager import StudentManager

class ProjectManager:

    def __init__(self):
        self.rubricFileName = 'rubric.txt'

    def formatProjet(self):
        self.makeProjectDirectory()
        self.unzipSubmissionFileInProjectDictory()
        self.formatStudents()

    def makeProjectDirectory(self):
        self.submissionZipFile = Config.submissionZipFileLocation.split("/")[-1]
        self.projectDirectory = self.submissionZipFile.split("_")[2]
        mkdir(self.projectDirectory)

    def unzipSubmissionFileInProjectDictory(self):
        copy(Config.submissionZipFileLocation, self.projectDirectory)
        with ZipFile(Config.submissionZipFileLocation) as zf:
            zf.extractall(self.projectDirectory)
        #removes the zip file in the project directory
        remove(self.projectDirectory + "/" + self.submissionZipFile.split("/")[-1])

    def formatStudents(self):
        self.studentManager = StudentManager(self.projectDirectory)
        self.studentManager.formatStudents()
        
