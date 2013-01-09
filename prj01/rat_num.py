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
        # Add attributes to the object
        self.nominator = int(nom)
        self.denominator = int(denom)
        
        # convert to the lowest fraction
        if self.is_nan() == False :
            a, b = self.nominator, self.denominator
            while b:
                a, b = b, a%b
            self.nominator /= a
            self.denominator /= a
        
        # if fraction was negative then move the sign to the nominator
        if self.is_negative() == True :
            a, b = str(self.nominator).replace("-",""), str(self.denominator).replace("-","")
            a = "-" + a
            self.nominator = int(a)
            self.denominator = int(b)
    
    @classmethod
    def from_str(klass, s):
        """Convert a string to a rational number.
        
        @param s: string representation of a rational number
        @type s: string
        @rtype: RatNum
        """
        if s == "nan" :
            return RatNum(1,0)
        elif "/" in s :
            a, b = s.split("/")
            return RatNum(int(a),int(b))
        else :
            return RatNum(int(s))

    def is_nan(self):
        """Returns True when self is not a number (nan).
        That is, when the denominator is zero.
        
        @rtype: boolean
        """
        try :
            a = self.nominator / self.denominator
        except ZeroDivisionError :
            return True
        return False
    
    def is_positive(self):
        """Check if C{self} is positive.
        
        @rtype: boolean
        """
        return self.is_nan() == False and self.__float__() > 0
    
    def is_negative(self):
        """Check if C{self} is negative.
        
        @rtype: boolean
        """
        return self.is_nan() == False and self.__float__() < 0
    
    def __float__(self):
        """Convert C{self} to a self.__float__ing point number.
        Must output C{self.__float__('nan')} when C{self} is nan.
        
        @rtype: self.__float__
        """
        if self.is_nan() == True :
            return "nan"
        else :
            return float(self.nominator)/self.denominator
    
    def __int__(self):
        """Convert C{self} to an integer.
        
            - If C{self} is positive, we round the number up.
            - If C{self} is negative, we round the number down.
        
        @rtype: integer
        """
        if self.__float__() > 0 :
            return int(math.ceil(self.__float__()))
        else :
            return int(math.floor(self.__float__()))
    
    def __eq__(self, other):
        """Equality operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: boolean
        """
        if other.__class__ == str :
            return str(self) == other
        return self.__float__() == other.__float__()
    
    def __ne__(self, other):
        """Inequality operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: boolean
        """
        return self.__float__() != other.__float__()
        
        
    def __add__(self, other):
        """Addition operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        if self.is_nan() == False and other.is_nan() == False :
            if self.denominator == other.denominator :
                return RatNum(self.nominator + other.nominator,self.denominator)
            else :
                lcf = self.denominator * other.denominator
                a = lcf / self.denominator
                b = lcf / other.denominator
                self.nominator *= a
                other.nominator *= b
                return RatNum(self.nominator + other.nominator,lcf)
        else :
            return RatNum(1, 0)
        
    def __sub__(self, other):
        """Subtraction operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        if self.is_nan() == False and other.is_nan() == False :
            if self.denominator == other.denominator :
                return RatNum(self.nominator - other.nominator,self.denominator)
            else :
                lcf = self.denominator * other.denominator
                a = lcf / self.denominator
                b = lcf / other.denominator
                self.nominator *= a
                other.nominator *= b
                return RatNum(self.nominator - other.nominator,lcf)
        else :
            return RatNum(1, 0)
        
    
    def __mul__(self, other):
        """Multiplication operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        if self.is_nan() == False and other.is_nan() == False :
            return RatNum(self.nominator * other.nominator,self.denominator * other.denominator)
        else :
            return RatNum(1, 0)
        
    def __div__(self, other):
        """Division operator.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: C{RatNum}
        """
        if self.is_nan() == False and other.is_nan() == False :
            return RatNum(self.nominator * other.denominator,self.denominator * other.nominator)
        else :
            return RatNum(1, 0)
        
    
    def __str__(self):
        """Return the string representation of C{self}
        
            - The string shows the fraction in the
              lowest terms.
        
            - The string will not show the denominator if it is 1.
        
            - Returns C{'nan'} if C{self} is not a number.
        
        @rtype: string
        """
        if self.is_nan() == True :
            return "nan"
        elif self.denominator == 1 :
            return str(self.nominator)
        else :
            a = self.nominator
            b = self.denominator
            while b:
                a, b = b, a%b
            self.nominator /= a
            self.denominator /= a
            return "{}/{}".format(self.nominator,self.denominator)
    
    def __neg__(self):
        """Negation operator.
        
        @rtype: C{RatNum}
        """
        if self.is_nan() == True :
            return "nan"
        else :
            return RatNum(self.nominator * -1,self.denominator)
    
    def __cmp__(self, other):
        """Comparision operator.
        
            - Return 1 if C{self} > C{other}.
            - Return -1 if C{self} < C{other}.
            - Return 0 if C{self} = C{other}.
        
        @param other:
        @type other: C{RatNum} 
        @rtype: integer
        """
        m,n = self.__float__(),other.__float__()
        if m > n :
            return 1
        elif m < n :
            return -1
        else :
            return 0