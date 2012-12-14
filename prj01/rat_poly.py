from rat_num import RatNum
from rat_term import RatTerm

class RatPoly:
    """Represent a polynomial whose coefficient are rational numbers.
    
    Examples of C{RatPoly}s include "0", "x-10", and "x^3-2*x^2+5/3*x+3", and "nan".
    
    @ivar terms: list of terms
    @type terms: list of C{RatTerms}
    """
    
    def __init__(self, coeff=RatNum(0), expt=0):
        """Provide three options to initialize the polynomial.
        
            - If the user doesn't specify any arguments, initialize
              C{self} as the zero polynomial.
            - If the user specifies only C{coeff}, initialize 
              C{self} as a degree-0 polynomial whose value is C{coeff}
            - If the user specifies both C{coeff} and C{expt},
              then initialize C{self} as the polynomial C{coeff}*x^C{expt}.
        
        @param coeff: the coefficient
        @type coeff: C{RatNum}
        @param expt: the exponent
        @type expt: integer
        """
        pass
    
    def coeff(self, expt):
        """Return the coefficient of the term 
        with the given exponent.
        
        @param expt: the exponent
        @type expt: integer
        @rtype: C{RatNum}
        """
        pass
    
    def degree(self):
        """Return the degree of the polynomial.
        
            - The zero polynomial has degree 0.
            - The degree of a polynomial which is not
              a number is unspecified.
        
        @rtype: integer
        """
        pass
    
    def is_zero(self):
        """Check if the polynomial is the zero polynomial.
        
        @rtype: boolean
        """
        pass
    
    def is_nan(self):
        """Check if the polynomial is not a number.
        That is, check whether any coefficient is not a number.
        
        @rtype: boolean
        """
        pass
    
    def __eq__(self, other):
        """Equality operator.
        
        @rtype: boolean
        """
        pass
        
    def __ne__(self, other):
        """Inequality operator.
        
        @rtype: boolean
        """
        pass
    
    @classmethod
    def zero(klass):
        """Return the zero polynomial.
        
        @rtype: C{RatPoly}
        """
        pass
    
    @classmethod
    def nan(klass):
        """Return a polynomial that is not a number.
        
        @rtype: C{RatPoly}
        """
        pass
    
    @classmethod
    def from_str(klass, s):
        """Convert a string representation of a C{RatPoly} to
        a C{RatPoly}
        
        @param s:
        @type s: string
        """
        pass
    
    def __str__(self):
        """Return a string representation of the polynomial.
        
        The string representation is basically a sum of terms
        from one with the highest exponent to the lowest exponent.
        
        @rtype: string
        """
        pass
    
    def __add__(self, other):
        """Addition operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        pass
    
    def __sub__(self, other):
        """Subtraction operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        pass
    
    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        pass
    
    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        pass
    
    def __neg__(self):
        """Negation operator.
        
        @rtype: C{RatPoly}
        """
        pass
    
    def eval(self, x):
        """Evaluate the polynomial at x.
        
        @param x:
        @type x: number
        @rtype: number
        """
        pass
    
    def differentiate(self):
        """Return the derivative of C{self}.
        
        Recall that the derivative of a polynomial
        is the sum of the derivatives of its terms.
        
        @rtype: C{RatPoly}
        """
        pass
    
    def anti_differentiate(self):
        """Return an anti-derivative of C{self} with constant 0.
        
        Recall that an anti-derivative of a polynomial
        can be computed by computing the sum of an anti-derivatives 
        of its terms. Here, we use the constant 0 for all the terms.
        
        @rtype: C{RatPoly}
        """
        pass
    
    def integrate(self, a, b):
        """Compute the definite integral of the
        polynomial from a to b.
        
        Recall that the definite integral of polynomial p(x)
        from a to b is given by P(b) - P(a), where
        P is an anti-derivative of p.
        
        @param a:
        @type a: number
        @param b:
        @type b: number
        """
        pass
    