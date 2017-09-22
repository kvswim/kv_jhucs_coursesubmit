"""
Menu-driven program to manipulate course listings and a central catalog.
"""
from CourseID import CourseID
from Course import Course
from CourseListing import CourseListing
from SemesterListing import SemesterListing
import urllib
import traceback
import os

def menu():
    """
    Print main menu and get user choice.
    """
    print "0) Quit program"
    print "1) Go to course menu"
    print "2) Go to semester menu"
    choice = int(input("enter choice # "))
    return choice

def menuC():
    """
    Print course menu and get user choice.
    """
    print "0) Return to main menu"
    print "1) Create new course"
    print "2) Find course details"
    print "5) List all courses (unsorted, no descript)"
    print "7) Add courses to catalog from text file"
    print "8) Save catalog"
    choice = int(input("enter choice # "))
    return choice

def menuS():
    """
    Print semester menu and get user choice.
    """
    print "0) Return to main menu"
    print "1) List all semesters"
    print "2) Select semester, make current"
    print "3) Create new semester, make current"
    print "4) Process current semester"
    choice = int(input("enter choice # "))
    return choice

def menuCS():
    """
    Work with current semester operations.
    """
    print "0) Return to semesters menu"
    print "1) List current semester courses"
    print "2) Load current semester from file"
    print "3) Add course to current semester"
    print "4) Edit course listing"
    print "5) Remove course from current semester"
    print "6) Save semester to file"
    print "7) Write html table for current semester"
    print "8) Write semester timetable"
    choice = int(input("enter choice # "))
    return choice

def newCourse(catalog, cid):
    """
    Add new course to catalog, given course number object (cid).
    Get course details from user input.
    """
    cstr = str(cid)
    if cstr not in catalog:
        name = raw_input("course title? ")
        areas = raw_input("area designators? ").upper()
        crds = input("credits? ")
        # update to include description
        print "enter description with blank line between paragraphs and # at end:"
        descr = " "
        line = raw_input()
        while line[-1] != "#":
            if line == ' ':
                descr = descr.strip() + '\n'
            else:
                descr += line.strip() + ' '
            line = raw_input()
            if len(line) == 0:
                line = ' '
        if len(line) > 1:  # add last line without #
            descr += line.strip()[:-1]
        descr = descr.strip() + '\n'
        crse = Course(cid, name, areas, crds)
        crse.setDescription(descr)
        catalog[cstr] = crse
        return crse
    else:
        return catalog[cstr]


def readCourseNum():
    """
    Read course number information, returning CourseID object.
    """
    cnum = raw_input("enter full course number in format DV.###.### ")
    return CourseID(cnum)
    

def readSemester():
    """
    Read semester information from keyboard.
    """
    season = raw_input("Season (Fall, Spring, Summer): ").lower().capitalize()
    year = int(input("Year (4 digits): "))
    semCode = season.upper()[:2] + str(year)[-2:]
    return season, year, semCode


def newSemester(semesters):
    season, year, semCode = readSemester()
    if semCode in semesters:
        print "ERROR: " + semCode + " already exists"
        return ""
    else: # add it
        sem = SemesterListing(season, year)
        semesters[semCode] = sem
        return semCode


def saveCatalog(filename, catalog):
    """
    Save catalog to plain text file
    """
    dbfile = open(filename, 'w')

    for key in sorted(catalog.keys()):  # do we want sort???
        dbfile.write(str(catalog[key]) + '\n')
        dbfile.write(catalog[key].getDescription() + '\n' + '\n')
    dbfile.close()


def loadCatalog(filename, catalog):
    """
    Add courses to catalog from text file (local or URL), named filename.  
    If course already exists, update its information.
    UPDATED for area designators and descriptions
    """
    try:
        if 'http' in filename:
            cfile = urllib.urlopen(filename)
        else:  # local text file
            cfile = open(filename, 'rb')
    except Exception as ioe:
        print "ERROR: " + filename + " could not be opened"
        print ioe
        # traceback.print_last()
    else:  # file open was successful, continue
        print "ADDING COURSES..."
        line = cfile.readline()
        while line != "":  # empty only at end of file
            # read title data
            where = line.find(' ')
            cnum = line[0:where]  # course number string
            line = line[where+1:]  # rest of the line
            left = line.find('[')
            right = line.find(']')
            if left >= 0:
                areas = line[left+1:right].strip().upper()
                line = line[right+1:]
            else:
                areas = ""   # no area designators
            left = line.find('(')
            right = line.find(')')
            cname = line[0:left].strip()
            creds = line[left+1:right].strip()
            crse = Course(cnum, cname, areas, creds)

            # read description until blank line
            descript = ""
            line = cfile.readline()

# can't get this to work with "" or "\n" or os.linesep    WHY????
            while len(line) > 2:  # until it's a blank line or end
                descript += line
                line = cfile.readline()
            descript = descript.strip()
            # print "DD-> " + descript   # for debugging
            crse.setDescription(descript)

            # put course in dictionary and get next line
            # print crse
            catalog[crse.getID()] = crse
            line = cfile.readline()
        print "DONE ADDING COURSES FROM FILE: " + filename
        cfile.close()


def main():
    catalog = {}   # central catalog of all courses
    print "trying to load courses from Courses.db file..."
    loadCatalog("Courses.db", catalog)
    semesters = {}  # central collection of all semester listings
    choice = 1
    while choice != 0:
        choice = menu()
        if choice == 0:
            print "Good-bye"
        elif choice == 1:
            doMenuC(catalog)
        elif choice == 2:
            doMenuS(catalog, semesters)
        else:
            print "ERROR: invalid menu option, try again"


def doMenuC(catalog):
    choice = 1
    while choice != 0:
        choice = menuC()
        if choice == 0:
            print "returning to main menu"
            return
        elif choice == 1:
            cid = readCourseNum()
            newCourse(catalog, cid)
        elif choice == 2: # find course details
            cid = str(readCourseNum())
            if cid in catalog:
                print catalog[cid].listing()
            else:
                print "ERROR: course does not exist in catalog"
        elif choice == 5:
            # list all courses
            for k in catalog:
                print catalog[k]
        elif choice == 7:
            # add courses to catalog from text file
            filename = raw_input("filename? ")
            loadCatalog(filename, catalog)
        elif choice == 8:
            print "saving courses to Courses.db file"
            saveCatalog("Courses.db", catalog)
        else:
            print "ERROR: invalid menu option, try again"

def doMenuS(catalog, semesters):
    choice = 1
    scode = ""   # current semester code, seed to something invalid
    while choice != 0:
        choice = menuS()
        if choice == 0:
            print "returning to main menu"
            return
        elif choice == 1:
            # list all semesters
            for k in semesters:
                print semesters[k]
        elif choice == 2: # find semester, make current
            sem, yr, scode = readSemester()
            if scode not in semesters:
                print "ERROR: " + scode + " doesn't exist, please add first"
                scode = ""
            else:
                print semesters[scode]
        elif choice == 3: # create new semester, make current
            scode = newSemester(semesters)
        elif choice == 4: # process current semester
            if scode not in semesters:
                print "ERROR: " + scode + " doesn't exist, please add first"
                scode = ""
            else:
                doMenuCS(semesters[scode], catalog)
        else:
            print "ERROR: invalid menu option, try again"

            
def doMenuCS(semlist, catalog):
    """
    Process current semester listing (semlist), using catalog data
    """
    choice = 1
    print "processing semester: " + str(semlist)
    while choice != 0:
        choice = menuCS()
        if choice == 0:
            print "returning to semesters menu"
            return
        elif choice == 1:
            # list current semester courses
            print semlist.listing(catalog)
        elif choice == 2:
            # load current semester from file
            print "not yet implemented"
        elif choice == 3:
            # add course to current semester
            cid = str(readCourseNum())
            if cid in catalog:
                print "course found in catalog, adding..."
                semlist.add(catalog[cid])
            else:
                print "ERROR: " + cid + " not in catalog yet"
        elif choice == 4:
            # edit course listing
            cid = str(readCourseNum())
            # need to implement: semlist.edit(cid)
            print "not yet implemented"
        elif choice == 5:
            # remove course from semester
            cid = str(readCourseNum())
            semlist.delete(cid)
        elif choice == 6:
            # save semester to file
            print "not yet implemented"
        elif choice == 7:
            # write semester html table
            print "not yet implemented"
        elif choice == 8:
            # write semester timetable
            print "not yet implemented"
        else:
            print "ERROR: invalid menu option, try again"


main()
