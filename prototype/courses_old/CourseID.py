class CourseID:
    """
    Class to hold and validate data for a (JHU) course ID
    """

    def __init__(self, cnstr):
        """
        Initialize a course number from a valid string (cnstr).
        >>> CourseID("en.6000.-23")
        >>> CourseID("en.as.py")
        """
        parts = cnstr.upper().strip().split('.')  # separate by .
        assert len(parts) == 3
        self.__div = parts[0]
#        print "checking dept..."
        try:
            self.__dept = int(parts[1])
            if self.__dept not in range(1000):
                raise ValueError
        except ValueError:
            print "ERROR: invalid course dept code"
            self.__dept = 0
#        print "checking num..."
        try:
            self.__num = int(parts[2])
            if self.__num not in range(1000):
                raise ValueError
        except ValueError:
            print "ERROR: invalid course number"
            self.__num = 0


    def __str__(self):
        """
        Return formatted string representation.
        >>> print CourseID("EN.600.112")
        EN.600.112
        >>> print CourseID("P.50.4")
        P.050.004
        """
        return self.__div + "." + '%03d' % self.__dept + "." + '%03d' % self.__num


    def __cmp__(self, other):
        """
        Compare courses based on all parts using string rep.
        >>> CourseID("EN.50.32") < CourseID("en.050.320")
        True
        >>> CourseID("EN.50.32") > CourseID("en.050.320")
        False
        """
        ss = str(self)
        so = str(other)
        if (ss < so):
            return -1
        elif (ss > so):
            return 1
        else:
            return 0


    def __eq__(self, other):
        """
        Test for equality by parts and return.
        >>> CourseID("EN.50.32") == CourseID("en.050.032")
        True
        >>> CourseID("EN.500.231") == CourseID("PY.500.231")
        False
        """
        return self.__cmp__(other) == 0


    def __ne__(self, other):
        return not self == other


    def department(self):
        return self.__dept

    def division(self):
        return self.__div

    def number(self):
        return self.__num
