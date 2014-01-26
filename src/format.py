import argparse
import AssignmentFormat.config as config
from AssignmentFormat.assignmentManager import AssignmentManager

def main():
    parser = argparse.ArgumentParser(description="Arguemtns for formating assignments")
    parser.add_argument("-z", "--zipFile", action="store", dest="submissionZipFile")
    parser.add_argument("-r", "--rubric", action="store", dest="rubricFile")
    results = parser.parse_args()

    if not results.submissionZipFile:
        print ("The submission zip  file was not given")
        exit(1)
    if not results.rubricFile:
        print("A rubric needs to be given")
        exit(1)

    config.SUBMISSION_ZIP_LOCATION = results.submissionZipFile 
    config.DUE_DATE = "2014-01-24-00-00-00"
    config.ATTEMPT_TYPE = config.GRADE_ATTEMPT_BEFORE_SUBMISSON
    config.RUBRIC_PATH = results.rubricFile

    assignmentManager = AssignmentManager()
    assignmentManager.format()

    
if __name__ == '__main__':
    main()
