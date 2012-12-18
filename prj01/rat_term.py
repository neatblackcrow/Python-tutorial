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
        pass
    
    def is_nan(self):
        """Check if the term is not a number.
        That is, check if the coefficient is not a number.
        
        @rtype: boolean"""
        pass
    
    def is_zero(self):
        """Check if the term is zero.
        That is, check if the coefficient is zero.
        
        @rtype: boolean"""
        pass
    
    def eval(self, x):
        """Evaluate the monomial at the given x.
        
        @param x:
        @type x: number
        @rtype: number
        """
        pass
    
    def __eq__(self, other):
        """Equality operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: boolean
        """
        pass
    
    def __ne__(self, other):
        """Inequality operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: boolean
        """
        pass
    
    @classmethod
    def from_str(klass, s):
        """Convert a string representation of C{RatTerm}
        to a C{RatTerm}
        
        @param s:
        @type s: string
        @rtype: C{RatTerm}
        """
        pass
    
    @classmethod
    def nan(klass):
        """Return an instance of C{RatTerm} that is not a number.
        
        @rtype: C{RatTerm}
        """
        pass
    
    @classmethod
    def zero(klass):
        """Return an instance of C{RatTerm} that is equal to zero.
        
        @rtype: C{RatTerm}
        """
        pass
    
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
        pass
    
    def __add__(self, other):
        """Addition operator.
        
        @raise C{ValueError}: if C{other's} exponent does not 
            equal C{self}'s
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        pass
    
    def __neg__(self):
        """Negation operator.
        
        @rtype: C{RatTerm}
        """
        pass
    
    def __sub__(self, other):
        """Subtraction operator.
        
        @raise C{ValueError}: if C{other's} exponent does not 
            equal C{self}'s
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        pass

    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        pass
    
    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatTerm}
        @rtype: C{RatTerm}
        """
        pass
    
    def differentiate(self):
        """Return the derivative of C{self}.
        
        Recall that the derivative of C*x^E is (C*E)*x^(E-1).
        
        @rtype: C{RatTerm}
        """        
        pass
    
    def anti_differentiate(self):
        """Return an anti-derivative of C{self} with constant 0.
        
        Recall that the anti-derivative of C*x^E is C/(E+1)*x^(E+1) + c,
        where c is a constant. Here, we use c = 0 in our output.
        
        @rtype: C{RatTerm}
        """
        pass
