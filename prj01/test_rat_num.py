from rat_num import RatNum
from asserts import *
import pytest

def assert_positive(x):
    assert x.is_positive()
    assert not x.is_negative()

def assert_negative(x):
    assert not x.is_positive()
    assert x.is_negative()

def assert_not_positive_negative(x):
    assert not x.is_positive()
    assert not x.is_negative()

def assert_eq_str(expected, s):
    assert expected == RatNum.from_str(s)

class TestRatNum:
    def setup_method(self, method):
        self.zero           = RatNum(0)
        self.one            = RatNum(1)
        self.neg_one        = RatNum(-1)
        self.two            = RatNum(2)
        self.three          = RatNum(3)
        
        self.one_I_two      = RatNum(1, 2)
        self.one_I_three    = RatNum(1, 3)
        self.one_I_four     = RatNum(1, 4)
        self.two_I_three    = RatNum(2, 3)
        self.three_I_four   = RatNum(3, 4)
        self.neg_one_I_two  = RatNum(-1, 2)
        self.three_I_two    = RatNum(3, 2)
        
        self.one_I_zero     = RatNum(1, 0)
        self.neg_one_I_zero = RatNum(-1, 0)
        self.hundred_I_zero = RatNum(100, 0)
        
        self.rat_nums       = [self.zero,
                               self.one,
                               self.neg_one,
                               self.two,
                               self.one_I_two,
                               self.neg_one_I_two,
                               self.three_I_two,
                               self.one_I_zero,
                               self.neg_one_I_zero,
                               self.hundred_I_zero]
        
        self.rat_nans       = [self.one_I_zero, 
                               self.neg_one_I_zero,
                               self.hundred_I_zero]
                               
        self.rat_non_nans   = [self.zero,
                               self.one,
                               self.neg_one,
                               self.two,
                               self.one_I_two,
                               self.three_I_two]

    def test_one_arg_constructor(self):
        RatNum(0)
        RatNum(1)
        RatNum(-1)
        RatNum(2)
        RatNum(3)
    
    def test_two_args_constructor(self):
        RatNum(1, 2)
        RatNum(1, 3)
        RatNum(1, 4)
        RatNum(2, 3)
        RatNum(3, 4)
    
    def test_is_nan(self):
        for x in self.rat_nans:
            assert x.is_nan()
        for x in self.rat_non_nans:
            assert x.is_nan() == False
    
    def test_is_positive_negative(self):
        assert_not_positive_negative(self.zero)
        
        assert_positive(self.one)
        assert_negative(self.neg_one)
        assert_positive(self.two)
        assert_positive(self.three)
        
        assert_positive(self.one_I_two)
        assert_positive(self.one_I_three)
        assert_positive(self.one_I_four)
        assert_positive(self.two_I_three)
        assert_positive(self.three_I_four)
        
        assert_negative(self.neg_one_I_two)
        
        assert_positive(self.three_I_two)
        
        assert_not_positive_negative(self.one_I_zero)
        assert_not_positive_negative(self.neg_one_I_zero)
        assert_not_positive_negative(self.hundred_I_zero)
    
    def test_float_value(self):
        assert_approx(0,  float(self.zero))
        assert_approx(1,  float(self.one))
        assert_approx(-1, float(self.neg_one))
        assert_approx(2,  float(self.two))
        assert_approx(0.5,  float(self.one_I_two))
        assert_approx(2.0/3,float(self.two_I_three))
        assert_approx(0.75, float(self.three_I_four))
        
        one_I_two_to_thirty = RatNum(1, 2**30)
        assert_approx(1.0 / 2**30, float(one_I_two_to_thirty))
    
    def test_int_value(self):
        assert 0    == int(self.zero)
        assert 1    == int(self.one)
        assert -1   == int(self.neg_one)
        
        assert 1    == int(self.one_I_two)
        assert 1    == int(self.two_I_three)
        assert 1    == int(self.three_I_four)
        
        assert -1   == int(RatNum(-1,2))
        assert -1   == int(RatNum(-2,3))
        assert -1   == int(RatNum(-3,4))
    
    def test_eq_reflective(self):
        for x in self.rat_nums:
            assert x == x
    
    def test_eq(self):
        assert self.one == self.one
        assert self.one + self.one == self.two
        assert self.neg_one == self.neg_one
        
        assert RatNum(1,1) == RatNum(1,1)
        assert RatNum(1,2) == RatNum(1,2)
        
        assert self.one == RatNum(2,2)
        assert RatNum(2,2) == self.one
        assert self.neg_one == RatNum(-9,9)
        assert RatNum(-9,9) == self.neg_one
        assert self.one_I_two == RatNum(-13, -26)
        assert RatNum(-13, -26) == self.one_I_two
        
        assert self.one_I_zero == self.one_I_zero
        assert self.one_I_zero == self.neg_one_I_zero
        assert self.one_I_zero == self.hundred_I_zero
        
    def test_neq(self):
        assert self.one != self.zero
        assert self.zero != self.one
        assert self.one != self.two
        assert self.two != self.one
        
        assert self.one != self.neg_one
        assert self.neg_one != self.one
        
        assert self.one != self.one_I_two
        assert self.one_I_two != self.one
        assert self.one != self.three_I_four
        assert self.three_I_four != self.one
    
    def test_str_simple(self):
        assert_str("0", self.zero)
        assert_str("1", self.one)
        assert_str("4", RatNum(4))
        assert_str("-1", self.neg_one)
        assert_str("-5", RatNum(-5))
        assert_str("0", RatNum(-0))

    def test_str_fractions(self):
        assert_str("1/2", self.one_I_two)
        assert_str("3/2", RatNum(3,2))
        assert_str("-1/13", RatNum(1,-13))
        assert_str("53/7", RatNum(53,7))
    
    def test_str_lowest_fraction(self):
        assert_str("1/2", RatNum(3,6))
        assert_str("5/3", RatNum(10,6))
        assert_str("-3/4", RatNum(-9,12))
        assert_str("2", RatNum(2,1))
        assert_str("0", RatNum(0,1))
        assert_str("1", RatNum(-100, -100))
    
    def test_to_string_nan(self):
        assert_str("nan", self.one_I_zero)
        assert_str("nan", RatNum(2,0))
        assert_str("nan", RatNum(-1,0))
        assert_str("nan", RatNum(0,0))
        assert_str("nan", RatNum(-100,0))
        
    def test_from_str(self):
        assert_eq_str(self.zero, "0")
        
        assert_eq_str(self.one, "1")
        assert_eq_str(self.one, "1/1")
        assert_eq_str(self.one, "2/2")
        assert_eq_str(self.one, "-1/-1")
        
        assert_eq_str(self.neg_one, "-1")
        assert_eq_str(self.neg_one, "1/-1")
        assert_eq_str(self.neg_one, "-3/3")
        
        assert_eq_str(self.two, "2")
        assert_eq_str(self.two, "2/1")
        assert_eq_str(self.two, "-4/-2")
        
        assert_eq_str(self.one_I_two, "1/2")
        assert_eq_str(self.one_I_two, "2/4")
        
        assert_eq_str(self.three_I_two, "3/2")
        assert_eq_str(self.three_I_two, "-6/-4")
        
        assert_eq_str(self.one_I_zero, "nan")
        assert_eq_str(self.neg_one_I_zero, "nan")
    
    def test_negate(self):
        assert_eq_str(-self.zero, "0")
        assert_eq_str(-self.one, "-1")
        assert_eq_str(-self.neg_one, "1")
        assert_eq_str(-self.two, "-2")
        assert_eq_str(-self.three, "-3")
        
        assert_eq_str(-self.one_I_two, "-1/2")
        assert_eq_str(-self.one_I_three, "-1/3")
        assert_eq_str(-self.one_I_four, "-1/4")
        assert_eq_str(-self.two_I_three, "-2/3")
        assert_eq_str(-self.three_I_four, "-3/4")
        
        assert_eq_str(-self.three_I_two, "-3/2")
        
        assert_eq_str(-self.one_I_zero, "nan")
        assert_eq_str(-self.neg_one_I_zero, "nan")
        assert_eq_str(-self.hundred_I_zero, "nan")
    
    def test_add_simple(self):
        assert_eq_str(self.zero + self.zero, "0")
        assert_eq_str(self.zero + self.one, "1")
        assert_eq_str(self.one + self.zero, "1")
        assert_eq_str(self.one + self.one, "2")
        assert_eq_str(self.one + self.neg_one, "0")
        assert_eq_str(self.one + self.two, "3")
        assert_eq_str(self.two + self.two, "4")
        
    def test_add_complex(self):
        assert_eq_str(self.one_I_two + self.zero, "1/2")
        assert_eq_str(self.one_I_two + self.one, "3/2")
        assert_eq_str(self.one_I_two + self.one_I_two, "1")
        assert_eq_str(self.one_I_two + self.neg_one, "-1/2")
        assert_eq_str(self.one_I_two + self.two, "5/2")
        assert_eq_str(self.one_I_two + self.two_I_three, "7/6")
        assert_eq_str(self.one_I_two + self.three_I_four, "5/4")
        
        assert_eq_str(self.one_I_three + self.zero, "1/3")
        assert_eq_str(self.one_I_three + self.two_I_three, "1")
        assert_eq_str(self.one_I_three + self.three_I_four, "13/12")
    
    def test_add_improper(self):
        assert_eq_str(self.three_I_two + self.one_I_two, "2")
        assert_eq_str(self.three_I_two + self.one_I_three, "11/6")
        assert_eq_str(self.three_I_four + self.three_I_four, "6/4")
        assert_eq_str(self.three_I_two + self.three_I_two, "3")
    
    def test_add_to_nan(self):
        for x in self.rat_nans:
            for y in self.rat_non_nans:
                assert_eq_str(x+y, "nan")
                assert_eq_str(y+x, "nan")
            for z in self.rat_nans:
                assert_eq_str(x+z, "nan")
    
    def test_add_transitively(self):
        assert_eq_str(self.one + self.one + self.one, "3")
        assert_eq_str(self.one + (self.one + self.one), "3")
        
        assert_eq_str(self.zero + self.zero + self.zero, "0")
        assert_eq_str(self.zero + (self.zero + self.zero), "0")
        
        assert_eq_str(self.one + self.two + self.three, "6")
        assert_eq_str(self.one + (self.two + self.three), "6")
        
        assert_eq_str(self.one_I_three + self.one_I_three + self.one_I_three, "1")
        assert_eq_str(self.one_I_three + (self.one_I_three + self.one_I_three), "1")
        
        assert self.one_I_zero + self.one_I_zero + self.one_I_zero == RatNum(1,0)
        assert self.one_I_zero + (self.one_I_zero + self.one_I_zero) == RatNum(1,0)
    
    def test_sum_simple(self):
        assert_eq_str(self.zero - self.one, "-1")
        assert_eq_str(self.zero - self.zero, "0")
        assert_eq_str(self.one - self.zero, "1")
        assert_eq_str(self.one - self.one, "0")
        assert_eq_str(self.two - self.one, "1")
        assert_eq_str(self.one - self.neg_one, "2")
        assert_eq_str(self.one - self.two, "-1")
        assert_eq_str(self.one - self.three, "-2")
    
    def test_sub_complex(self):
        assert_eq_str(self.one - self.one_I_two, "1/2")
        assert_eq_str(self.one_I_two - self.one, "-1/2")
        assert_eq_str(self.one_I_two - self.zero, "1/2")
        assert_eq_str(self.one_I_two - self.two_I_three, "-1/6")
        assert_eq_str(self.one_I_two - self.three_I_four, "-1/4")
        
    def test_sub_improper(self):
        assert_eq_str(self.three_I_two - self.one_I_two, "1")
        assert_eq_str(self.three_I_two - self.one_I_three, "7/6")
    
    def test_sub_with_nan(self):
        for x in self.rat_nans:
            for y in self.rat_non_nans:
                assert_eq_str(x-y, "nan")
                assert_eq_str(y-x, "nan")
            for z in self.rat_nans:
                assert_eq_str(x-z, "nan")
    
    def test_sub_transitively(self):
        assert_eq_str(self.one - self.one - self.one, "-1")
        assert_eq_str(self.one - (self.one - self.one), "1")
        
        assert_eq_str(self.zero - self.zero - self.zero, "0")
        assert_eq_str(self.zero - (self.zero - self.zero), "0")
        
        assert_eq_str(self.one - self.two - self.three, "-4")
        assert_eq_str(self.one - (self.two - self.three), "2")
        
        assert_eq_str(self.one_I_three - self.one_I_three - self.one_I_three, "-1/3")
        assert_eq_str(self.one_I_three - (self.one_I_three - self.one_I_three), "1/3")
        
        assert_eq_str(self.one_I_two - self.one_I_three - self.one_I_four, "-1/12")
        assert_eq_str(self.one_I_two - (self.one_I_three - self.one_I_four), "5/12")
        
    def test_mul_properties(self):
        # one
        for x in self.rat_non_nans:
            assert self.one * x == x
            assert x * self.one == x
        # zero
        for x in self.rat_non_nans:
            assert self.zero * x == self.zero
            assert x * self.zero == self.zero
        # negative one
        for x in self.rat_non_nans:
            assert self.neg_one * x == -x
            assert x * self.neg_one == -x
    
    def test_mul_simple(self):
        assert_eq_str(self.two * self.two, "4")
        assert_eq_str(self.two * self.three, "6")
        assert_eq_str(self.three * self.two, "6")
        
    def test_mul_complex(self):
        assert_eq_str(self.one_I_two * self.two, "1")
        assert_eq_str(self.two * self.one_I_two, "1")
        
        assert_eq_str(self.one_I_two * self.one_I_two, "1/4")
        assert_eq_str(self.one_I_two * self.one_I_three, "1/6")
        assert_eq_str(self.one_I_three * self.one_I_two, "1/6")
        
    def test_mul_improper(self):
        assert_eq_str(self.three_I_two * self.one_I_two, "3/4")
        assert_eq_str(self.three_I_two * self.one_I_three, "1/2")
        assert_eq_str(self.three_I_two * self.three_I_four, "9/8")
        assert_eq_str(self.three_I_two * self.three_I_two, "9/4")
    
    def test_mul_to_nan(self):
        for x in self.rat_nums:
            for y in self.rat_nans:
                assert_eq_str(x*y, "nan")
                assert_eq_str(y*x, "nan")
    
    def test_mul_transitively(self):
        assert_eq_str(self.one * self.one * self.one, "1")
        assert_eq_str(self.one * (self.one * self.one), "1")
        
        assert_eq_str(self.zero * self.zero * self.zero, "0")
        assert_eq_str(self.zero * (self.zero * self.zero), "0")
        
        assert_eq_str(self.one * self.two * self.three, "6")
        assert_eq_str(self.one * (self.two * self.three), "6")
        
        assert_eq_str(self.one_I_three * self.one_I_three * self.one_I_three, "1/27")
        assert_eq_str(self.one_I_three * (self.one_I_three * self.one_I_three), "1/27")
        
        assert_eq_str(self.one_I_two * self.one_I_three * self.one_I_four, "1/24")
        assert_eq_str(self.one_I_two * (self.one_I_three * self.one_I_four), "1/24")

    def test_div_simple(self):
        assert self.one / self.zero == RatNum(1,0)
        assert_eq_str(self.zero / self.one, "0")
        assert self.zero / self.zero == RatNum(1,0)
        assert_eq_str(self.one / self.one, "1")
        assert_eq_str(self.one / self.neg_one, "-1")
        assert_eq_str(self.one / self.two, "1/2")
        assert_eq_str(self.two / self.two, "1")
        
    def test_div_complex(self):
        assert self.one_I_two / self.zero == RatNum(1,0)
        assert_eq_str(self.one_I_two / self.one, "1/2")
        assert_eq_str(self.one_I_two / self.one_I_two, "1")
        assert self.one_I_two / self.one_I_three == self.three_I_two
        assert_eq_str(self.one_I_two / self.neg_one, "-1/2")
        assert_eq_str(self.one_I_two / self.two, "1/4")
        assert_eq_str(self.one_I_two / self.two_I_three, "3/4")
        assert_eq_str(self.one_I_two / self.three_I_four, "2/3")
        
        assert self.one_I_three / self.zero == RatNum(1,0)
        assert_eq_str(self.one_I_three / self.two_I_three, "1/2")
        assert_eq_str(self.one_I_three / self.three_I_four, "4/9")
    
    def test_div_improper(self):
        assert_eq_str(self.three_I_two / self.one_I_two, "3")
        assert_eq_str(self.three_I_two / self.one_I_three, "9/2")
        assert_eq_str(self.three_I_two / self.three_I_four, "2")
        assert_eq_str(self.three_I_two / self.three_I_two, "1")
    
    def test_div_to_nan(self):
        for x in self.rat_nums:
            for y in self.rat_nans:
                assert_eq_str(x/y, "nan")
                assert_eq_str(y/x, "nan")
    
    def test_mul_transitively(self):
        assert_eq_str(self.one / self.one / self.one, "1")
        assert_eq_str(self.one / (self.one / self.one), "1")

        assert self.zero / self.zero / self.zero == RatNum(1,0)
        assert self.zero / (self.zero / self.zero) == RatNum(1,0)

        assert_eq_str(self.one / self.two / self.three, "1/6")
        assert_eq_str(self.one / (self.two / self.three), "3/2")

        assert_eq_str(self.one_I_three / self.one_I_three / self.one_I_three, "3")
        assert_eq_str(self.one_I_three / (self.one_I_three / self.one_I_three), "1/3")

        assert_eq_str(self.one_I_two / self.one_I_three / self.one_I_four, "6")
        assert_eq_str(self.one_I_two / (self.one_I_three / self.one_I_four), "3/8")
    
    def test_compare_non_fraction(self):
        assert self.one > self.zero
        assert self.one > self.neg_one
        assert self.two > self.one
        assert self.two > self.zero
        assert self.zero > self.neg_one
    
    def test_compare_fraction(self):
        assert self.one > self.one_I_two
        assert self.two > self.one_I_three
        assert self.one > self.two_I_three
        assert self.two > self.two_I_three
        
        assert self.one_I_two > self.zero
        assert self.one_I_two > self.neg_one
        assert self.one_I_two > self.neg_one_I_two
        assert self.zero > self.neg_one_I_two
        
    def test_compare_with_nan(self):
        for x in self.rat_nans:
            for y in self.rat_non_nans:
                assert x > y
                assert y < x
            for z in self.rat_nans:
                assert x == z

if __name__ == "__main__":
    pytest.main("test_rat_num.py")