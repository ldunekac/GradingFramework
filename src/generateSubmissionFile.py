import sys

def main():
    """Assums that the directory you are in is the assignment directory"""
    if not len(sys.argv) == 2:
        print("Requires the csv file for this assignment")

    gradeCSV = sys.argv[1]

    


if __name__ == '__main__':
    main()