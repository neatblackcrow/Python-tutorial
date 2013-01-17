# ID: 5510405791
# Name: Voravut Nateluercha
from rat_num import RatNum

class RatTerm:
    """Represent a monomial whose coefficient is a rational number.
    The term has the form C*x^E where C (the coefficient)
    is a rational number, and E (the exponent) is an integer.
    
    @ivar coeff: the coefficient
    @type coeff: C{RatNum}
    @ivar expt: the exponent
    @type expt: integer
    """
    
    def __init__(self, coeff, expt):
        """Initialize the coefficient and the exponent
        with the given values.
        
        @param coeff: the coefficient
        @type coeff: C{RatNum}
        @param expt: the exponent
        @type expt: integer
        """
        # assign a attribute to the object.
        
        self.coeff = coeff
        
        if self.coeff.is_nan() :
            self.expt = 0
        elif self.is_zero() == False :
            self.expt = int(expt)
        else :
            self.expt = 0
    
    def is_nan(self):
        """Check if the term is not a number.
        That is, check if the coefficient is not a number.
        
        @rtype: boolean"""
        
        return self.coeff.is_nan()
    
    def is_zero(self):
        """Check if the term is zero.
        That is, check if the coefficient is zero.
        
        @rtype: boolean"""
        return float(self.coeff.nominator) / self.coeff.denominator == 0.0
    
    def eval(self, x):
        """Evaluate the monomial at the given x.
        
        @param x:
        @type x: number
        @rtype: number
        """
        return ( float(self.coeff.nominator) / self.coeff.denominator ) * ( x ** self.expt )
    
    def __eq__(self, other):
        """Equality operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: boolean
        """
        if self.is_nan() and other.is_nan() :
            return True
        elif self.is_zero() and other.is_zero() :
            return True        
        elif int(self.coeff) == int(other.coeff) :
            return True
    
    def __ne__(self, other):
        """Inequality operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: boolean
        """
        if (self.is_nan() and not other.is_nan()) or (not self.is_nan() and other.is_nan()) :
            return True
        elif (self.is_zero() and not other.is_zero()) or (not self.is_zero() and other.is_zero()) :
            return True        
        elif int(self.coeff) != int(other.coeff) :
            return True
        
    @classmethod
    def from_str(klass, s):
        """Convert a string representation of C{RatTerm}
        to a C{RatTerm}
        
        @param s:
        @type s: string
        @rtype: C{RatTerm}
        """
        # Special cases
        if s == "nan" :
            return RatTerm(RatNum(1, 0), 0)
        elif s == "0" :
            return RatTerm(RatNum(0, 1), 0)
        elif s == "x" :
            return RatTerm(RatNum(1, 1), 0)
        elif s == "-x" :
            return RatTerm(RatNum(-1, 1), 0)
        
        # Exponent
        if "^" in s :
            expo = int(s.split("^")[1])
        else :
            expo = 1
           
        # Rational coefficient 
        co = s.split("*")[0]
        if "/" in co :
            nom, sep, denom = s.partition("/")
            nom = int(nom)
            denom = int(denom.split("*")[0])
        # coefficient = 1
        elif s.startswith("x") :
            nom = 1
            denom = 1
        # coefficient = -1
        elif s.startswith("-x") :
            nom = -1
            denom = 1
        else :
            nom = int(s.split("*")[0])
            denom = 1
            
        
        return RatTerm(RatNum(nom, denom), expo)
    
    @classmethod
    def nan(klass):
        """Return an instance of C{RatTerm} that is not a number.
        
        @rtype: C{RatTerm}
        """
        return RatTerm(RatNum(1, 0), 0)
    
    @classmethod
    def zero(klass):
        """Return an instance of C{RatTerm} that is equal to zero.
        
        @rtype: C{RatTerm}
        """
        return RatTerm(RatNum(0, 1), 0)
    
    def __str__(self):
        """Return a string representation of C{self}.
        
            - The string does not show the exponentiation sign
              and the exponent if the exponent is 1.
            - The string does not show the variable x if
              the exponent is 0.
            - The string does not show the coefficient if the
              exponent is at least one, and the coefficient is
              1 or -1.
            - Return C{'-x'} if the coefficient is -1 and 
              the exponent is 1.
            - Return C{'nan'} if the monomial is not a number.
        
        @rtype: string
        """
        # special cases
        if self.is_nan() :
            return "nan"
        elif self.coeff == 1 :
            if self.expt == 1 :
                return "x"
            else :
                return "x^" + str(self.expt)
        elif self.coeff == -1 :
            if self.expt == 1 :
                return "-x"
            else :
                return "-x^" + str(self.expt)
        
        # str_builder
        if self.expt == 0 :
            if self.coeff.denominator == 1 :
                return str(self.coeff.nominator)
            else :
                return "{}/{}".format(str(self.coeff.nominator), str(self.coeff.denominator))
        elif self.expt == 1 :
            if self.coeff.denominator == 1 :
                return str(self.coeff.nominator) + "*x"
            else :
                return "{}/{}".format(str(self.coeff.nominator), str(self.coeff.denominator)) + "*x"
        else :
            if self.coeff.denominator == 1 :
                return str(self.coeff.nominator) + "*x^" + str(self.expt)
            else :
                return "{}/{}".format(str(self.coeff.nominator), str(self.coeff.denominator)) + "*x^" + str(self.expt)
    
    def __add__(self, other):
        """Addition operator.
        
        @raise C{ValueError}: if C{other's} exponent does not 
            equal C{self}'s
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        # Operation on nan
        if self.is_nan() or other.is_nan() :
            return RatTerm(RatNum(1, 0), 0)
        
        # Operation on zero
        if self.is_zero() :
            return other
        elif other.is_zero() :
            return self
        
        # Normal operation
        if self.expt == other.expt :
            return RatTerm(self.coeff + other.coeff, self.expt)
        else :
            raise ValueError
    
    def __neg__(self):
        """Negation operator.
        
        @rtype: C{RatTerm}
        """
        return RatTerm(-self.coeff, self.expt)
    
    def __sub__(self, other):
        """Subtraction operator.
        
        @raise C{ValueError}: if C{other's} exponent does not 
            equal C{self}'s
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        # Operation on nan
        if self.is_nan() or other.is_nan() :
            return RatTerm(RatNum(1, 0), 0)
        
        # Operation on zero
        if self.is_zero() :
            return RatTerm(-other.coeff, self.expt)
        elif other.is_zero() :
            return self
        
        # Normal operation
        if self.expt == other.expt :
            return RatTerm(self.coeff - other.coeff, self.expt)
        else :
            raise ValueError
        
    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        # Operation on nan
        if self.is_nan() or other.is_nan() :
            return RatTerm(RatNum(1, 0), 0)
        
        # Operation on zero
        if self.is_zero() or other.is_zero() :
            return RatTerm(RatNum(0, 1), 0)
        
        # Normal operation
        return RatTerm(self.coeff * other.coeff, self.expt + other.expt)
    
    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        # Operation on nan
        if self.is_nan() or other.is_nan() :
            return RatTerm(RatNum(1, 0), 0)
        
        # Operation on zero
        if self.is_zero() :
            return RatTerm(RatNum(0, 1), 0)
        elif other.is_zero() :
            return RatTerm(RatNum(1, 0), 0)
        
        # Normal operation
        return RatTerm(self.coeff / other.coeff, self.expt - other.expt)
    
    def differentiate(self):
        """Return the derivative of C{self}.
        
        Recall that the derivative of C*x^E is (C*E)*x^(E-1).
        
        @rtype: C{RatTerm}
        """        
        if not self.is_nan() :
            return RatTerm(RatNum(self.coeff * self.expt), (self.expt - 1))
        else :
            return RatTerm(RatNum(1, 0), 0)
        
    def anti_differentiate(self):
        """Return an anti-derivative of C{self} with constant 0.
        
        Recall that the anti-derivative of C*x^E is C/(E+1)*x^(E+1) + c,
        where c is a constant. Here, we use c = 0 in our output.
        
        @rtype: C{RatTerm}
        """
        if not self.is_nan() :
            return RatTerm(RatNum(self.coeff.nominator,self.expt + 1), self.expt + 1)
        else :
            return RatTerm(RatNum(1, 0), 0)
