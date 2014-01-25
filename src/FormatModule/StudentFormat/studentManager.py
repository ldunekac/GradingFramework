from os import chdir, listdir
from FormatModule.StudentFormat.student import Student

class StudentManager:

    def __init__(self,projectDirectory):
        self.projectDirectory = projectDirectory

    def formatStudents(self):
        chdir(self.projectDirectory)
        self.getUserNames()
        self.studentList = []

        for studentUserName in self.studentUserNames:
            studentFiles = [f for f in listdir('.') if studentUserName in f]
            self.studentList.append(Student(studentUserName, studentFiles))

        for student in self.studentList:
            student.formatStudent()

    def getUserNames(self):
        self.studentUserNames = set([f.split('_')[1] for f in listdir('.')]) 
        