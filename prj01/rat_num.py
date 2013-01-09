# ID: 5510405791
# Name: Voravut Nateluercha

import math

class RatNum:
    """Represent a rational number.
    
    @ivar nom: the nominator
    @type nom: integer
    @ivar denom: the denominator
    @type denom: integer
    """
    def __init__(self, nom, denom=1):
        """Initialize the nominator and denominator
        with the given value.
        
        @param nom: the nominator
        @type nom: integer
        @param denom: the denominator. Defaulted to 1.
        @type denom: integer
        """
        self.nominator = nom
        self.denominator = denom
    
    @classmethod
    def from_str(klass, s):
        """Convert a string to a rational number.
        
        @param s: string representation of a rational number
        @type s: string
        @rtype: RatNum
        """
        pass
    
    def is_nan(self):
        """Returns True when self is not a number (nan).
        That is, when the denominator is zero.
        
        @rtype: boolean
        """
        pass
    
    def is_positive(self):
        """Check if C{self} is positive.
        
        @rtype: boolean
        """
        pass
    
    def is_negative(self):
        """Check if C{self} is negative.
        
        @rtype: boolean
        """
        pass
    
    def __float__(self):
        """Convert C{self} to a floating point number.
        Must output C{float('nan')} when C{self} is nan.
        
        @rtype: float
        """
        pass
    
    def __int__(self):
        """Convert C{self} to an integer.
        
            - If C{self} is positive, we round the number up.
            - If C{self} is negative, we round the number down.
        
        @rtype: integer
        """
        pass
    
    def __eq__(self, other):
        """Equality operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: boolean
        """
        pass
    
    def __ne__(self, other):
        """Inequality operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: boolean
        """
        pass
        
    def __add__(self, other):
        """Addition operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        pass
    
    def __sub__(self, other):
        """Subtraction operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        pass
    
    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        pass

    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        pass
    
    def __str__(self):
        """Return the string representation of C{self}
        
            - The string shows the fraction in the
              lowest terms.
        
            - The string will not show the denominator if it is 1.
        
            - Returns C{'nan'} if C{self} is not a number.
        
        @rtype: string
        """
        pass
    
    def __neg__(self):
        """Negation operator.
        
        @rtype: C{RatNum}
        """
        pass
    
    def __cmp__(self, other):
        """Comparision operator.
        
            - Return 1 if C{self} > C{other}.
            - Return -1 if C{self} < C{other}.
            - Return 0 if C{self} = C{other}.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: integer
        """
        pass
