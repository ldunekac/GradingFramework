import argparse
from FormatModule.projectManager import ProjectManager
from FormatModule.config import Config

def main():
    parser = argparse.ArgumentParser(description="Arguemtns for formating assignments")
    parser.add_argument("-z", "--zipFile", action="store", dest="submissionZipFile")

    results = parser.parse_args()

    if not results.submissionZipFile:
        print ("The submission zip  file was not given")
        exit(1)

    dueDate = "2014-01-24-11-59-59"

    Config.submissionZipFileLocation = results.submissionZipFile 
    Config.dueDate = dueDate
    Config.attemptToGrade = Config.GRADE_LAST_ATTEMPT

    projectManager = ProjectManager()
    projectManager.formatProjet()


if __name__ == '__main__':
    main()


"""
Types of formats

grade last atempt
grade attempt before the submission date 

"""