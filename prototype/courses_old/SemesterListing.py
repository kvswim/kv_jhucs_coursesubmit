from CourseListing import CourseListing
from Course import Course

class SemesterListing:
    """
    Class to represent a collection of CourseListings for a particular semester, 
    mapped with unique CourseIDs to a map of sections to the actual 
    CourseListings. The sections map is for multiple sections, many courses 
    may only have one.
    """

    def __init__(self, when, year):
        """
        Create a semester listing based on when (Fall/Spring) and year, with
        an empty mapping of CourseIDs to a list of CourseListings
        """
        self._season = when.lower().capitalize()
        self._year = year
        self._courses = {}  # empty dictionary


    def __str__(self):
        """
        Return string representation which is semester info.
        """
        result = self._season + " " + str(self._year)
        result += " (" + self.code() + ")"
        return result


    def listing(self, catalog):
        """
        Return string representation which is semester info, followed by the
        full course information ordered by number, one per line.
        """
        print "making listing..."
        result = str(self) + "\n"
        keysort = sorted(self._courses.keys())
        for cidstr in keysort:
            cldict = self._courses[cidstr]  # map of sections to CourseListings
            crse = catalog[cidstr]
            result += str(crse) + "\n"
            for sect in sorted(cldict.keys()):
                clist = cldict[sect]
                result += "%02d" % sect
                result += " " + clist.getWho() + " [" + clist.getWhen() + "]\n"
            result += "\t" + crse.getDescription() + "\n\n"
        return result


    def courseIDs(self):
        """
        Return sorted list of course IDs for semester.
        """
        return sorted(self._courses.keys())


    def code(self):
        """
        Return short-cut semester code.
        >>> SemesterListing("fall", 2015).code()
        'FA15'
        """
        return self._season[:2].upper() + str(self._year)[-2:]


    def add(self, clist):
        """
        Add course (listing) with section to semester.
        Return True if added, False otherwise
        >>> sem = SemesterListing("fall", 2015)
        >>> cl = CourseListing("en.600.107", "Selinski", "MWF 3")
        >>> sem.add(cl)
        True
        >>> print cl
        EN.600.107.01 Selinski [MWF 3]
        """
        if isinstance(clist, Course):
            # create course listing, rename as clist
            # get instructor and time info
            cnum = clist.getID()
            instr = raw_input("Instructor? ")
            time = raw_input("Time Block? ")
            clist = CourseListing(cnum, instr, time, 0)

        elif not isinstance(clist, CourseListing):
            print "ERROR: " + clist + " is not a Course or CourseListing object"
            return False

        # now we process CourseListing parameter
        cnum = clist.getCourse()
        sect = clist.getSect()
        if cnum in self._courses:  # already at least one section
            # check and add section
            cldict = self._courses[cnum]
            if sect == 0 or sect in cldict:
                print "These sections already exist: " + str(cldict.keys())
                sect = int(raw_input("Enter new section # or existing to overwrite: "))
                clist.setSect(sect)
            self._courses[cnum][sect] = clist
        else:
            # create empty dictionary of course listings for this course number
            self._courses[cnum] = {}  
            self._courses[cnum][1] = clist  # assume section 1 for first
        return True


    def delete(self, cid):
        """
        Remove course from listing if it's there, based on course num (cid)
        and section.  Return True if deleted, False otherwise.  
        """
        cnum = str(cid)
        if cnum in self._courses:
            # delete entry with cid as the key, based on sect
            cldict = self._courses[cnum]
            if len(cldict) == 1:
                del self._courses[cnum]
                return True
            else:
                print "Multiple sections exist: " + str(cldict.keys())
                sect = int(raw_input("enter section to delete: "))
                if sect in cldict:
                    del cldict[sect]
                    return True
        print "ERROR: " + cnum + "." + "%02d"%sect + " not in semester"
        return False

