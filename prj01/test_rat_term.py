#import pytest
import unittest
from asserts import *
from rat_num import RatNum
from rat_term import RatTerm

def assert_eq_str(expected, s):
    assert expected == RatTerm.from_str(s)

def assert_str(term, expected):
    assert str(term) == expected

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def term(*args):
    if len(args) == 1:
        return RatTerm(RatNum(args[0]), 0)
    elif len(args) == 2:
        return RatTerm(RatNum(args[0]), args[1])
    elif len(args) == 3:
        return RatTerm(RatNum(args[0], args[1]), args[2])
    else:
        raise ArgumentError("term receives only one, two, or three arguments")

class TestRatTerm(unittest.TestCase):
    def setUp(self):
        self.nan_num = RatNum(1,0)
        self.nan_term = term(1,0,0)
            
    def test_constructor(self):
        term(1)
        term(2,3)
        term(4, 3, 0)
        term(-2, 7, 3)
    
    def test_constructor_zero_coeff(self):
        term(0,0)
        term(0,1)
    
    def test_ctor_nan(self):
        term(3,0,0)
    
    def test_coeff(self):
        assert term(3,1).coeff == RatNum(3)
        assert term(2,5,2).coeff == RatNum(2,5)
        assert term(0,0).coeff == RatNum(0)
        assert term(-2,3,2).coeff == RatNum(-2,3)
        assert term(3,0,4).coeff == self.nan_num
    
    def test_expt(self):
        assert term(2,4).expt == 4
        
    def test_expt_zero_coeff(self):
        assert term(0,0).expt == 0
        assert term(0,1).expt == 0
    
    def test_is_nan(self):
        assert term(5,0,0).is_nan()
        assert term(0,0,4).is_nan()
        assert not term(2,3,2).is_nan()
    
    def test_eval(self):
        assert_approx(0, term(0,0).eval(5.0))
        assert_approx(0.0, term(0, 5).eval(1.2))
        assert_approx(2.0, term(2, 0).eval(3.1))
        assert_approx(1.0, term(1, 0).eval(100.0))
        assert_approx(35.0, term(5, 1).eval(7.0))
        assert_approx(12.0, term(3, 2).eval(2.0))
        assert_approx(-16.0, term(-2, 3).eval(2.0))
        assert_approx(-3.0, term(3, 3).eval(-1.0))
        assert_approx(1.0, term(-1, 1).eval(-1.0))
        assert_approx(2.0, term(1, 2, 2).eval(2.0))
        assert_approx(.125, term(1, 2, 2).eval(.5))
    
    def test_eq(self):
        assert term(3,5) == term(3,5)
        assert term(1,2,4) == term(1,2,4)
        assert term(-2,4,2) == term(1,-2,2)
        assert term(4,6) != term(7,8)
        
    def test_eq_zero_coeff(self):
        assert term(0,0) == term(0,0)
        assert term(0,1) == term(0,0)
    
    def test_eq_nan_coeff(self):
        assert self.nan_term == term(19,0,0)
        assert self.nan_term == term(0,0,0)
        assert self.nan_term != term(3,5)
        assert term(0,3) != self.nan_term
    
    def test_from_str_simple(self):
        assert_eq_str(term(1,1), "x")
        assert_eq_str(term(-1,1), "-x")
    
    def test_from_str_const(self):
        assert_eq_str(term(2,0), "2")
        assert_eq_str(term(3,4,0), "3/4")
        assert_eq_str(term(-4,0), "-4")
        assert_eq_str(term(-7,5,0), "-7/5")
    
    def test_from_str_leading_coeff(self):
        assert_eq_str(term(2,1), "2*x")
        assert_eq_str(term(3,7,1), "3/7*x")
        assert_eq_str(term(-4,3,1), "-4/3*x")
    
    def test_from_str_pow(self):
        assert_eq_str(term(1,3), "x^3")
        assert_eq_str(term(-1,4), "-x^4")
    
    def test_from_str_full(self):
        assert_eq_str(term(4,2), "4*x^2")
        assert_eq_str(term(2,5,6), "2/5*x^6")
        assert_eq_str(term(-3,2,2), "-3/2*x^2")
    
    def test_from_str_nan(self):
        assert_eq_str(term(1,0,0), "nan")
    
    def test_from_str_zero(self):
        assert_eq_str(term(0,0), "0")

    def test_str_simple(self):
        assert_str(term(1,1), "x")
        assert_str(term(-1,1), "-x")

    def test_str_const(self):
        assert_str(term(2,0), "2")
        assert_str(term(3,4,0), "3/4")
        assert_str(term(-4,0), "-4")
        assert_str(term(-7,5,0), "-7/5")

    def test_str_leading_coeff(self):
        assert_str(term(2,1), "2*x")
        assert_str(term(3,7,1), "3/7*x")
        assert_str(term(-4,3,1), "-4/3*x")

    def test_str_pow(self):
        assert_str(term(1,3), "x^3")
        assert_str(term(-1,4), "-x^4")

    def test_str_full(self):
        assert_str(term(4,2), "4*x^2")
        assert_str(term(2,5,6), "2/5*x^6")
        assert_str(term(-3,2,2), "-3/2*x^2")

    def test_str_nan(self):
        assert_str(term(1,0,0), "nan")

    def test_from_str_zero(self):
        assert_str(term(0,0), "0")

    def test_add(self):
        assert term(3,0) == term(1,0) + term(2,0)
        assert term(4, 2) == term(3, 2) + term(1, 2)
        assert term(1, 2, 3) == term(1, 6, 3) + term(1, 3, 3)
        assert term(1, 8, 1) == term(1, 4, 1) + term(-1, 8, 1)
        assert term(-1, 8, 1) == term(-1, 4, 1) + term(1, 8, 1)
    
    def test_sub(self):
        assert term(1, 0) == term(2, 0) - term(1, 0)
        assert term(-1, 0) == term(1, 0) - term(2, 0)
        assert term(2, 2) == term(3, 2) - term(1, 2)
        assert term(-1, 6, 3) == term(1, 6, 3) - term(1, 3, 3)
        assert term(3, 8, 1) == term(1, 4, 1) - term(-1, 8, 1)
        assert term(-3, 8, 1) == term(-1, 4, 1) - term(1, 8, 1)

    def test_mul(self):
        assert term(2, 0) == term(1, 0) * term(2, 0)
        assert term(3, 4) == term(3, 2) * term(1, 2)
        assert term(1, 18, 6) == term(1, 6, 3) * term(1, 3, 3)
        assert term(-1, 32, 2) == term(1, 4, 1) * term(-1, 8, 1)
        assert term(2, 1) == term(2, 1) * term(1, 0)

    def test_div(self):
        assert term(1, 2, 0) == term(1, 0) / term(2, 0)
        assert term(3, 0) == term(3, 2) / term(1, 2)
        assert term(1, 2, 0) == term(1, 6, 3) / term(1, 3, 3)
        assert term(-2, 0) == term(1, 4, 1) / term(-1, 8, 1)
        assert term(2, 1) == term(2, 1) / term(1, 0)
        assert term(8, 3) == term(-16, 5) / term(-2, 2)

    def test_operation_on_nan(self):
        assert self.nan_term == self.nan_term + term(3, 4)
        assert self.nan_term == term(3, 4) + self.nan_term
        assert self.nan_term == self.nan_term - term(3, 4)
        assert self.nan_term == term(3, 4) - self.nan_term
        assert self.nan_term == self.nan_term * term(3, 4)
        assert self.nan_term == term(3, 4) * self.nan_term
        assert self.nan_term == self.nan_term / term(3, 4)
        assert self.nan_term == term(3, 4) / self.nan_term

    def test_operation_on_zero(self):
        t = term(-2, 3)
        zero = term(0, 0)
        
        assert t == zero + t
        assert t == t + zero
        assert term(2, 3) == zero - t
        assert t == t - zero
        assert zero == zero * t
        assert zero == t * zero
        assert zero == zero / t
        assert self.nan_term == t / zero
        assert 0 == (t - t).expt
    
    def add_different_expt(self, a, b):
        #with pytest.raises(ValueError):
        with self.assertRaises(ValueError):
            a + b
    
    def sub_different_expt(self, a, b):
        #with pytest.raises(ValueError):
        with self.assertRaises(ValueError):
            a - b
    
    def test_add_sub_different_expts(self):
        self.add_different_expt(term(1,2), term(1,4))
        self.add_different_expt(term(3,2,0), term(7,3,1))
        self.sub_different_expt(term(1,2), term(1,3))
        self.sub_different_expt(term(3,2,0), term(7,3,1))
    
    def test_differentiate(self):
        assert term(1, 0) == term(1, 1).differentiate()
        assert term(0, 0) == term(99, 0).differentiate()
        assert term(5, 0) == term(5, 1).differentiate()
        assert term(14, 1) == term(7, 2).differentiate()
        assert term(-2, 3) == term(-1, 2, 4).differentiate()
        assert self.nan_term == self.nan_term.differentiate()
        assert self.nan_term == RatTerm(RatNum(1,0), 0).differentiate()

    def test_anti_differentiate(self):
        assert term(1, 1) == term(1, 0).anti_differentiate()
        assert term(1, 2) == term(2, 1).anti_differentiate()
        assert term(4, 3, 3) == term(4, 2).anti_differentiate()
        assert self.nan_term == self.nan_term.anti_differentiate()

if __name__ == "__main__":
    #pytest.main("test_rat_term.py")
    unittest.main()
