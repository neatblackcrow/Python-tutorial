from rat_num import RatNum
from rat_term import RatTerm
from rat_poly import RatPoly
from asserts import *
#import pytest
import unittest

def num(a, b=1):
    return RatNum(a,b)

def term(*args):
    if len(args) == 1:
        return RatTerm(RatNum(args[0]), 0)
    elif len(args) == 2:
        return RatTerm(RatNum(args[0]), args[1])
    elif len(args) == 3:
        return RatTerm(RatNum(args[0], args[1]), args[2])
    else:
        raise ArgumentError("term receives only one, two, or three arguments")

def poly(coeff, expt=0):
    if isinstance(coeff, RatNum):
        return RatPoly(coeff, expt)
    else:
        return RatPoly(RatNum(coeff), expt)

def quad_poly(x2, x1, x0):
    return poly(x2,2) + poly(x1,1) + poly(x0,0)

def parse(s):
    return RatPoly.from_str(s)

def assert_str(p, s):
    assert str(p) == s

def assert_eq_str(p, s):
    assert p == parse(s)

def assert_poly_coeff(p, expected_coeffs):
    if p.is_zero():
        assert p.degree() == 0
    else:
        assert p.degree() == len(expected_coeffs)-1

    for i in xrange(len(expected_coeffs)):
        if isinstance(expected_coeffs[-(i+1)], RatNum):
            assert p.coeff(i) == expected_coeffs[-(i+1)]
        else:
            assert p.coeff(i) == RatNum(expected_coeffs[-(i+1)])

def assert_from_str(s, expected_coeffs):
    p = parse(s)
    assert_poly_coeff(p, expected_coeffs)

def assert_str_from_str_works(s):
    assert s == str(parse(s))

class TestRatPoly(unittest.TestCase):
    def test_one_arg_constructor(self):
        assert_poly_coeff(RatPoly(), [])

    def test_two_args_constructor(self):
        assert_poly_coeff(poly(RatNum(0), 0), [])
        assert_poly_coeff(poly(RatNum(0), 1), [])
        assert_poly_coeff(poly(RatNum(1), 0), [1])
        assert_poly_coeff(poly(RatNum(-1), 0), [-1])
        assert_poly_coeff(poly(RatNum(1), 1), [1,0])
        assert_poly_coeff(poly(RatNum(1), 2), [1,0,0])
        assert_poly_coeff(poly(RatNum(2), 2), [2,0,0])
        assert_poly_coeff(poly(RatNum(2), 3), [2,0,0,0])
        assert_poly_coeff(poly(RatNum(-2), 3), [-2,0,0,0])
        assert_poly_coeff(poly(RatNum(-1), 1), [-1,0])
        assert_poly_coeff(poly(RatNum(-1), 3), [-1,0,0,0])

    def test_from_str_simple(self):
        assert_from_str("0", [])
        assert_from_str("x", [1,0])
        assert_from_str("x^2", [1,0,0])
    
    def test_from_str_multiple_terms(self):
        assert_from_str("x^3+x^2", [1, 1, 0, 0])
        assert_from_str("x^3-x^2", [1, -1, 0, 0])
        assert_from_str("x^10+x^2", [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])

    def test_parse_leading_neg(self):
        assert_from_str("-x^2", [-1, 0, 0])
        assert_from_str("-x^2+1", [-1, 0, 1])
        assert_from_str("-x^2+x", [-1, 1, 0])

    def test_parse_leading_constants(self):
        assert_from_str("10*x", [10, 0])
        assert_from_str("10*x^4+x^2", [10, 0, 1, 0, 0])
        assert_from_str("10*x^4+100*x^2", [10, 0, 100, 0, 0])
        assert_from_str("-10*x^4+100*x^2", [-10, 0, 100, 0, 0])

    def test_parse_rationals(self):
        assert_from_str("1/2", [num(1,2)])
        assert_from_str("1/2*x", [num(1,2), 0])
        assert_from_str("x+1/3", [1, num(1,3)])
        assert_from_str("1/2*x+1/3", [num(1,2), num(1,3)])
        assert_from_str("1/2*x+3/2", [num(1,2), num(3,2)])
        assert_from_str("1/2*x^3+3/2", [num(1,2), 0, 0, num(3,2)])
        assert_from_str("1/2*x^3+3/2*x^2+1", [num(1,2), num(3,2), 0, 1])

    def test_parse_nan(self):
        assert parse("nan").is_nan()

    def test_str_from_str_simple(self):
        assert_str_from_str_works("0")
        assert_str_from_str_works("x")
        assert_str_from_str_works("x^2")

    def test_str_from_str_mult_terms(self):
        assert_str_from_str_works("x^3+x^2")
        assert_str_from_str_works("x^3-x^2")
        assert_str_from_str_works("x^100+x^2")

    def test_str_from_str_leading_neg(self):
        assert_str_from_str_works("-x^2")
        assert_str_from_str_works("-x^2+1")
        assert_str_from_str_works("-x^2+x")

    def test_str_from_str_leading_consts(self):
        assert_str_from_str_works("10*x")
        assert_str_from_str_works("10*x^100+x^2")
        assert_str_from_str_works("10*x^100+100*x^2")
        assert_str_from_str_works("-10*x^100+100*x^2")
    
    def test_str_from_str_rationals(self):
        assert_str_from_str_works("1/2")
        assert_str_from_str_works("1/2*x")
        assert_str_from_str_works("x+1/3")
        assert_str_from_str_works("1/2*x+1/3")
        assert_str_from_str_works("1/2*x+3/2")
        assert_str_from_str_works("1/2*x^10+3/2")
        assert_str_from_str_works("1/2*x^10+3/2*x^2+1")

    def test_str_from_str_nan(self):
        assert_str_from_str_works("nan")
    
    def test_degree(self):
        assert parse("1").degree() == 0
        assert parse("x").degree() == 1
        assert parse("x^100").degree() == 100
        assert parse("0*x^100").degree() == 0
        assert parse("0*x^0").degree() == 0
        assert parse("x^2+x+1").degree() == 2
    
    def test_add(self):
        _XSqPlus2X = poly(1, 2) + poly(1, 1) + poly(1, 1)
        _2XSqPlusX = poly(1, 2) + poly(1, 2) + poly(1, 1)

        assert_eq_str(poly(1, 0) + poly(1, 0), "2")
        assert_eq_str(poly(1, 0) + poly(5, 0), "6")
        assert_eq_str(poly(1, 1) + poly(1, 1), "2*x")
        assert_eq_str(poly(1, 2) + poly(1, 2), "2*x^2")
        assert_eq_str(poly(1, 2) + poly(1, 1), "x^2+x")
        assert_eq_str(_XSqPlus2X, "x^2+2*x")
        assert_eq_str(_2XSqPlusX, "2*x^2+x")
        assert_eq_str(poly(1, 3) + poly(1, 1), "x^3+x")
    
    def test_sub(self):
        assert_eq_str(poly(1, 1) - poly(1, 0), "x-1")
        assert_eq_str(poly(2, 1) - poly(1, 1), "x")
        assert_eq_str(poly(1, 2) - poly(1, 1) + poly(1,0), "x^2-x+1")
    
    def test_mul(self):
        assert_eq_str(poly(0, 0) * poly(0, 0), "0")
        assert_eq_str(poly(1, 0) * poly(1, 0), "1")
        assert_eq_str(poly(1, 0) * poly(2, 0), "2")
        assert_eq_str(poly(2, 0) * poly(2, 0), "4")
        assert_eq_str(poly(1, 0) * poly(1, 1), "x")
        assert_eq_str(poly(1, 1) * poly(1, 1), "x^2")
        assert_eq_str( (poly(1, 1) + poly(1, 0)) * (poly(1, 1) - poly(1, 0)), "x^2-1")
    
    def ops_with_nan(self, p):
        nan = RatPoly.from_str("nan")
        assert_eq_str(p + nan, "nan")
        assert_eq_str(nan + p, "nan")
        assert_eq_str(p - nan, "nan")
        assert_eq_str(nan - p, "nan")
        assert_eq_str(p * nan, "nan")
        assert_eq_str(nan * p, "nan")
        assert_eq_str(p / nan, "nan")
        assert_eq_str(nan / p, "nan")
    
    def test_ops_with_nan(self):
        self.ops_with_nan(poly(0, 0))
        self.ops_with_nan(poly(0, 1))
        self.ops_with_nan(poly(1, 0))
        self.ops_with_nan(poly(1, 1))
        self.ops_with_nan(poly(2, 0))
        self.ops_with_nan(poly(2, 1))
        self.ops_with_nan(poly(0, 2))
        self.ops_with_nan(poly(1, 2))
    
    def test_immutability(self):
        one = poly(1,0)
        two = poly(2,0)
        
        one.degree()
        two.degree()
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one.coeff(0)
        two.coeff(0)
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one.is_nan()
        two.is_nan()
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one.eval(0.0)
        two.eval(0.0)
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        -one
        -two
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one + two
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one - two
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one * two
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")

        one / two
        assert_eq_str(one, "1")
        assert_eq_str(two, "2")
    
    def test_eval(self):
        zero = RatPoly()
        one = poly(1,0)
        _X = poly(1,1)
        _2X = poly(2, 1)
        _XSq = poly(1, 2)

        assert_approx(0.0, zero.eval(0.0), 0.0001)
        assert_approx(0.0, zero.eval(1.0), 0.0001)
        assert_approx(0.0, zero.eval(2.0), 0.0001)
        assert_approx(1.0, one.eval(0.0), 0.0001)
        assert_approx(1.0, one.eval(1.0), 0.0001)
        assert_approx(1.0, one.eval(2.0), 0.0001)

        assert_approx(0.0, _X.eval(0.0), 0.0001)
        assert_approx(1.0, _X.eval(1.0), 0.0001)
        assert_approx(2.0, _X.eval(2.0), 0.0001)

        assert_approx(0.0, _2X.eval(0.0), 0.0001)
        assert_approx(2.0, _2X.eval(1.0), 0.0001)
        assert_approx(4.0, _2X.eval(2.0), 0.0001)

        assert_approx(0.0, _XSq.eval(0.0), 0.0001)
        assert_approx(1.0, _XSq.eval(1.0), 0.0001)
        assert_approx(4.0, _XSq.eval(2.0), 0.0001)

        _XSq_minus_2X = _XSq - _2X

        assert_approx(0.0, _XSq_minus_2X.eval(0.0), 0.0001)
        assert_approx(-1.0, _XSq_minus_2X.eval(1.0), 0.0001)
        assert_approx(0.0, _XSq_minus_2X.eval(2.0), 0.0001)
        assert_approx(3.0, _XSq_minus_2X.eval(3.0), 0.0001)

    def test_coeff(self):
        # coeff has been checked a lot in assert_poly_coeff
        # so we check on negative indices here
        _XSqPlus2X = poly(1, 2) + poly(1, 1) + poly(1, 1)
        _2XSqPlusX = poly(1, 2) + poly(1, 2) + poly(1, 1)

        assert _XSqPlus2X.coeff(-1) == num(0)
        assert _XSqPlus2X.coeff(-10) == num(0)
        assert _2XSqPlusX.coeff(-1) == num(0)
        assert _2XSqPlusX.coeff(-10) == num(0)
        
        zero = poly(0,0)
        assert zero.coeff(-10) == num(0)
        assert zero.coeff(-1) == num(0)
    
    def test_div(self):
        # 0/x = 0
        assert_eq_str(poly(0, 1) / poly(1, 1), "0")

        # 2/1 = 2
        assert_eq_str(poly(2, 0) / poly(1, 0), "2")

        # x/x = 1
        assert_eq_str(poly(1, 1) / poly(1, 1), "1")

        # -x/x = -1
        assert_eq_str(poly(-1, 1) / poly(1, 1), "-1")

        # x/-x = -1
        assert_eq_str(poly(1, 1) / poly(-1, 1), "-1")

        # -x/-x = 1
        assert_eq_str(poly(-1, 1) / poly(-1, 1), "1")

        # -x^2/x = -x
        assert_eq_str(poly(-1, 2) / poly(1, 1), "-x")

        # x^100/x^1000 = 0
        assert_eq_str(poly(1, 100) / poly(1, 1000), "0")

        # x^100/x = x^99
        assert_eq_str(poly(1, 100) / poly(1, 1), "x^99")

        # x^99/x^98 = x
        assert_eq_str(poly(1, 99) / poly(1, 98), "x")

        # x^10 / x = x^9 (r: 0)
        assert_eq_str(poly(1, 10) / poly(1, 1), "x^9")

        # x^10 / x^3+x^2 = x^7-x^6+x^5-x^4+x^3-x^2+x-1  (r: -x^2)
        assert_eq_str(poly(1, 10) / (poly(1, 3) + poly(1, 2)), "x^7-x^6+x^5-x^4+x^3-x^2+x-1")

        # x^10 / x^3+x^2+x = x^7-x^6+x^4-x^3+x-1 (r: -x)
        assert_eq_str(poly(1, 10) / (poly(1, 3) + poly(1, 2) + poly(1, 1)), "x^7-x^6+x^4-x^3+x-1")

        # x^10+x^5 / x = x^9+x^4 (r: 0)
        assert_eq_str((poly(1, 10) + poly(1, 5)) / poly(1, 1), "x^9+x^4")

        # x^10+x^5 / x^3 = x^7+x^2 (r: 0)
        assert_eq_str((poly(1, 10) + poly(1, 5)) / poly(1, 3), "x^7+x^2")

        # x^10+x^5 / x^3+x+3 = x^7-x^5-3*x^4+x^3+7*x^2+8*x-10 (r: 29*x^2+14*x-30)
        assert_eq_str((poly(1, 10) + poly(1, 5)) / (poly(1, 3) + poly(1, 1) + poly(3, 0)), "x^7-x^5-3*x^4+x^3+7*x^2+8*x-10")

    def test_div_complex_I(self):
        # (x+1)*(x+1) = x^2+2*x+1
        assert_eq_str((poly(1, 2) + poly(2, 1) + poly(1, 0)) / (poly(1, 1) + poly(1, 0)), "x+1")

        # (x-1)*(x+1) = x^2-1
        assert_eq_str((poly(1, 2) + poly(-1, 0)) / (poly(1, 1) + poly(1, 0)), "x-1")
    
    def test_div_complex_II(self):
        # x^8+2*x^6+8*x^5+2*x^4+17*x^3+11*x^2+8*x+3 =
        # (x^3+2*x+1) * (x^5+7*x^2+2*x+3)
        large = (poly(1, 8) + 
            poly(2, 6) + 
            poly(8, 5) + 
            poly(2, 4) + 
            poly(17, 3) +
            poly(11, 2) +
            poly(8, 1) +
            poly(3, 0))
        
        # x^3+2*x+1
        sub1 = poly(1, 3) + poly(2, 1) + poly(1, 0)
        
        # x^5+7*x^2+2*x+3
        sub2 = poly(1, 5) + poly(7, 2) + poly(2, 1) + poly(3, 0)
        
        assert large / sub2 == sub1
        assert large / sub1 == sub2
    
    def test_div_complex_III(self):
        assert_eq_str(parse("x^3-2*x+3") / parse("3*x^2"), "1/3*x")
        assert_eq_str(parse("x^2+2*x+15") / parse("2*x^3"), "0")
    
    def test_div_complex_IV(self):
        assert_eq_str(parse("x^8+x^6+10*x^4+10*x^3+8*x^2+2*x+8") /parse("3*x^6+5*x^4+9*x^2+4*x+8"),
                      "1/3*x^2-2/9")
    
    def test_div_by_zero(self):
        assert_eq_str(poly(1,0) / poly(0,0), "nan")
        assert_eq_str(poly(1,1) / poly(0,0), "nan")
    
    def test_div_poly_with_nan(self):
        zero = poly(0,0)
        nan_x2 = poly(1, 2) * (poly(1, 1) / zero)
        one_x1 = poly(1, 1)

        assert_eq_str(nan_x2 / one_x1, "nan")
        assert_eq_str(one_x1 / nan_x2, "nan")
        assert_eq_str(nan_x2 / zero, "nan")
        assert_eq_str(zero / nan_x2, "nan")
        assert_eq_str(nan_x2 / nan_x2, "nan")
    
    def test_is_nan(self):
        assert parse("nan").is_nan()
        assert not parse("1").is_nan()
        assert not parse("1/2").is_nan()
        assert not parse("x+1").is_nan()
        assert not parse("x^2+x+1").is_nan()
    
    def test_differentiate(self):
        assert_eq_str(poly(1,1).differentiate(), "1")
        assert_eq_str(quad_poly(7,5,99).differentiate(), "14*x+5")
        assert_eq_str(quad_poly(3,2,1).differentiate(), "6*x+2")
        assert_eq_str(quad_poly(1,0,1).differentiate(), "2*x")
        assert_eq_str(parse("nan").differentiate(), "nan")
    
    def test_anti_differentiate(self):
        assert_eq_str(poly(1, 0).anti_differentiate(), "x");
        assert_eq_str(poly(2, 1).anti_differentiate(), "x^2");
        assert_eq_str(quad_poly(0, 6, 2).anti_differentiate(), "3*x^2+2*x");
        assert_eq_str(quad_poly(4, 6, 2).anti_differentiate(), "4/3*x^3+3*x^2+2*x");

        assert_eq_str(parse("nan").anti_differentiate(), "nan");
    
    def test_integrate(self):
        assert_approx(1.0, poly(1,0).integrate(0,1))
        assert_approx(3.0, poly(2,1).integrate(1,-2))
        assert_approx(369.3333333333, quad_poly(7,6,2).integrate(1,5))

if __name__ == "__main__":
    #pytest.main("test_rat_poly.py")
    unittest.main()
