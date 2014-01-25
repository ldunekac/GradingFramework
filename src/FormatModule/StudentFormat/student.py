from os import mkdir, chdir, listdir, remove
from shutil import move
from zipfile import ZipFile


class Student:

    def __init__(self, studentUsername, studentFiles):
        self.studentFiles = studentFiles
        self.studentUsername = studentUsername

    def formatStudent(self):
        mkdir(self.studentUsername)
        for studentFile in self.studentFiles:
            move(studentFile, self.studentUsername)

        chdir(self.studentUsername)

        self.unzipAllFiles(True)
        
        chdir('..')

    def unzipAllFiles(self, blackboardFormat=False):
        """ """

       
        
