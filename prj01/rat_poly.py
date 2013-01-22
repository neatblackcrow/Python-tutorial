# ID: 5510405791
# Name: Voravut Nateluercha

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
        self.terms = []
        for i in range(expt) :
            self.terms += [RatTerm(RatNum(0, 1), i)]
        self.terms += [RatTerm(coeff, expt)]
        
        
    def coeff(self, expt):
        """Return the coefficient of the term 
        with the given exponent.
        
        @param expt: the exponent
        @type expt: integer
        @rtype: C{RatNum}
        """
        for item in self.terms :
            if item.expt == expt :
                return item.coeff
    
    def degree(self):
        """Return the degree of the polynomial.
        
            - The zero polynomial has degree 0.
            - The degree of a polynomial which is not
              a number is unspecified.
        
        @rtype: integer
        """
        return self.terms[0].expt
    
    def is_zero(self):
        """Check if the polynomial is the zero polynomial.
        
        @rtype: boolean
        """
        return self.terms[0].is_zero()
    
    def is_nan(self):
        """Check if the polynomial is not a number.
        That is, check whether any coefficient is not a number.
        
        @rtype: boolean
        """
        for item in self.terms :
            if item.coeff.is_nan() :
                return True
        return False
    
    def __eq__(self, other):
        """Equality operator.
        
        @rtype: boolean
        """
        if self.__class__ == int and other.__class__ == int :
            return self == other
        else :
            return self.terms == other.terms
        
    def __ne__(self, other):
        """Inequality operator.
        
        @rtype: boolean
        """
        return self.terms != other.terms
    
    @classmethod
    def zero(klass):
        """Return the zero polynomial.
        
        @rtype: C{RatPoly}
        """
        return RatPoly(RatNum(0, 1), 1)
    
    @classmethod
    def nan(klass):
        """Return a polynomial that is not a number.
        
        @rtype: C{RatPoly}
        """
        return RatPoly(RatNum(1, 0), 1)
    
    @classmethod
    def from_str(klass, s):
        """Convert a string representation of a C{RatPoly} to
        a C{RatPoly}
        
        @param s:
        @type s: string
        """
        if s == "nan" :
            return RatPoly(RatNum(1, 0), 0)
        temp_list = []
        
        # Prevent the first negative sign from being seperated.
        temp_list += s[0]
        
        i = 0
        for sub_str in s[1:] :
            if sub_str == "-" :
                temp_list += "-"
                i += 1
            elif sub_str == "+" :
                temp_list.append("")
                i += 1
            else :
                temp_list[i] += sub_str
                
        li = []
        for sub_item in temp_list :
            li.append([RatTerm.from_str(sub_item).coeff, RatTerm.from_str(sub_item).expt])

        poly = RatPoly()
        poly.terms = []
        degree = max(i[1] for i in li)
        i = degree
        while i >= 0 :
            for coeff, expt in li :
                if i == expt :
                    poly.terms += [RatTerm(coeff, expt)]
                    break
            else :
                poly.terms += [RatTerm(RatNum(0, 1), i)]
            i -= 1
            
        return poly
        
    def __str__(self):
        """Return a string representation of the polynomial.
        
        The string representation is basically a sum of terms
        from one with the highest exponent to the lowest exponent.
        
        @rtype: string
        """
        temp_str = ""
        
        for k in self.terms:
            if str(k) == "x" :
                temp_str += "+1"
            elif str(k) == "-x" :
                temp_str += "-1"
            elif not str(k).startswith("-") and k != self.terms[0] :
                temp_str += "+" + str(k)
            else :
                temp_str += str(k)
            
        return temp_str
    
    def __add__(self, other):
        """Addition operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
    def __sub__(self, other):
        """Subtraction operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatPoly}
        @rtype: C{RatPoly}
        """
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
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
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
    def anti_differentiate(self):
        """Return an anti-derivative of C{self} with constant 0.
        
        Recall that an anti-derivative of a polynomial
        can be computed by computing the sum of an anti-derivatives 
        of its terms. Here, we use the constant 0 for all the terms.
        
        @rtype: C{RatPoly}
        """
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
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
        if not self.is_nan() and not other.is_nan() :
            pass
        else :
            return RatPoly(RatNum(1, 0), 0)
    
