from CourseID import CourseID

"""
Courses in the JHU system have optional area designators
"""

class Course:
    """
    Hold and manipulate core information for a course.
    """

    def __init__(self, cnum, name, areas="E", creds=3):
        """
        Initialize from course number/ID string (cnum), name, 
        area designators, and credits.
        """
        if type(cnum) is str:
            self._number = CourseID(cnum)
        elif isinstance(cnum, CourseID):
            self._number = cnum
        else:
            print "ERROR - invalid course number"
            self._number = CourseID("DV.###.###")
        self._areas = areas   # validate?!
        self._title = name
        self._credits = float(creds)
        self._description = "(needs description)"   # update later


    def __str__(self):
        """
        Return string representation of course, minus description.
        >>> print Course("EN.600.112", "IPSE", "E", 4.0)
        EN.600.112 [E] IPSE (4.0)
        >>> print Course(CourseID("e.60.30"), "blah", "EQ", 3)
        E.060.030 [EQ] blah (3.0)
        >>> print Course("en.600.107", "Intro Java")
        EN.600.107 [E] Intro Java (3.0)
        """
        astr = ""
        if len(self._areas) > 0:
            astr = "[" + self._areas + "] "
        return str(self._number) + " " + astr + self._title + \
            " (" + "%0.1f"%float(self._credits) + ")"


    def listing(self):
        """
        Full course information, including description.
        """
        return str(self) + "\n" + "\t" + self.getDescription()


    def __eq__(self, other):
        return self._number == other._number


    def __ne__(self, other):
        return self._number != other._number


    def __cmp__(self, other):
        """
        Compare courses based on number.
        >>> Course("en.060.112", "what", 'E', 3) < Course("py.300.492", "blah", 'E', 3.5)
        True
        >>> Course("en.60.112", "what") > Course("en.300.492", "blah")
        False
        """
        return self._number.__cmp__(other._number)


    def getID(self):
        """
        Return course ID as string
        >>> print Course("en.600.112", "IPSE").getID()
        EN.600.112
        """
        return str(self._number)


    def setDescription(self, desc):
        self._description = desc.strip()  # strip to be safe


    def getDescription(self):
        return self._description


    def name(self):
        """
        >>> Course("en.600.112", "IPSE", "E").name()
        'IPSE'
        """
        return self._title


    def credits(self):
        """
        >>> Course("en.600.112", "IPSE", "E", 4).credits()
        4.0
        """
        return self._credits
