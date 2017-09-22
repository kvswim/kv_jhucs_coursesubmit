from CourseID import CourseID
from Course import Course

class CourseListing:
    """
    Semester-specific course information.
    """
    
    def __init__(self, cid, instr, times, sect=1):
        """
        Initialize with course ID string, instructor, meeting times, section.
        (Had semester and year.)  (Need to add validity checks!)
        """
        if type(cid) == str:
            self._cidstr = str(CourseID(cid))
        elif isinstance(cid, CourseID):
            self._cidstr = str(cid)
        elif isinstance(cid, Course):
            self._cidstr = cid.getID()
        else:
            print "ERROR: invalid course ID " + str(cid)
        self._instr = instr
        self._when = times
        self._sect = sect
#        self._semester = sem.lower().capitalize()  # Fall or Spring
#        self._year = year


    def __str__(self):
        """
        >>> print CourseListing(CourseID("en.600.112"), "Selinski", "MWF 12", "FALL", 2015)
        EN.600.112 Selinski [MWF 12]
        >>> print CourseListing(CourseID("en.600.112"), "Selinski", "MWF 12")
        EN.600.112.01 Selinski [MWF 12]
        """
        return self.getID() + " " + self._instr + " [" + self._when + "]"


    def getID(self):
        """
        >>> cl = CourseListing("en.600.112", "staff", "MWF 12", 2)
        >>> cl.getID()
        'EN.600.112.02'
        """
        return self._cidstr + "." + "%02d" % self._sect
        

    def getCourse(self):
        """
        >>> cl = CourseListing("en.600.112", "staff", "MWF 12", 2)
        >>> cl.getCourse()
        'EN.600.112'
        """
        return self._cidstr
        

    def getWho(self):
        """
        >>> cl = CourseListing("en.600.112", "Selinski", "MWF 12")
        >>> print cl.getWho()
        Selinski
        """
        return self._instr


    def getWhen(self):
        """
        >>> print CourseListing("en.600.112", "Selinski", "MWF 12").getWhen()
        MWF 12
        """
        return self._when 


    def getSect(self):
        """
        >>> print CourseListing("en.600.112", "Selinski", "MWF 12").getSect()
        1
        >>> print CourseListing("en.600.112", "Selinski", "MWF 12", 10).getSect()
        10
        """
        return self._sect


    def setSect(self, sect):
        assert type(sect) == int
        self._sect = sect


    def __eq__(self, other):
        """
        """
        return self._cidstr == other._cidstr and self._instr == other._instr and \
            self._sect == other._sect and self._when == other._when


    def __ne__(self, other):
        return not self == other


    def __cmp__(self, other):
        """
        Compare CourseListings by course ID.
        """
        return self.getID().__cmp__(other.getID())
