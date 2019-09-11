#!/usr/bin/python3

import sys
from rational import Rational

# rational test: A test driver for rational.py module.

def main ( ):
    generalTests ( )
    errorTests ( )

def generalTests ( ):
    """Test basic functionality."""

    """Test constructor."""

    r0 = Rational ( )
    print ( 'r0 =', r0, '  (', float ( r0 ), ')' )
    r1 = Rational ( 1, 3 )
    print ( 'r1 =', r1, '(', float ( r1 ), ')' )
    r2 = Rational ( 2, 6 )
    print ( 'r2 =', r2, '(', float ( r2 ), ')' )
    r3 = Rational ( 100, 300 )
    print ( 'r3 =', r3, '(', float ( r3 ), ')' )
    r4 = Rational ( -1, -3 )
    print ( 'r4 =', r4, '(', float ( r4 ), ')' )
    print ( )

    r6 = Rational ( 0, -5 )
    print ( 'r6 =', r6, '   ( ', float ( r6 ), ')' )
    r7 = Rational ( -2, 5 )
    print ( 'r7 =', r7, '(', float ( r7 ), ')' )
    r8 = Rational ( 2, -5 )
    print ( 'r8 =', r8, '(', float ( r8 ), ')' )
    print ( )

    """Test '+', '-', '*', '/' arithmetic operators."""

    r9  = r1 + r7
    print ( r1, '+', r7, '=' , r9,  '(', float ( r9 ),  ')' )
    r10 = r1 - r7
    print ( r1, '-', r7, '=' , r10, '( ', float ( r10 ), ')' )
    r11 = r1 * r7
    print ( r1, '*', r7, '=' , r11, '(', float ( r11 ), ')' )
    r12 = r1 / r7
    print ( r1, '/', r7, '=' , r12, ' (', float ( r12 ), ')' )
    print ( )

    """Test relational operators."""

    print ( r1, '==', r7, ':', r1 == r7 )
    print ( r1, '!=', r7, ':', r1 != r7 )
    print ( r1, '< ', r7, ':', r1 <  r7 )
    print ( r1, '<=', r7, ':', r1 <= r7 )
    print ( r1, '> ', r7, ':', r1 >  r7 )
    print ( r1, '>=', r7, ':', r1 >= r7 )
    print ( )

    """Test '+=', '-=', '*=', '/=' operators."""

    ra = r1; r1 += r7; print ( '(', ra, '+=', r7, ') =', r1 )
    r1 = ra; r1 -= r7; print ( '(', ra, '-=', r7, ') =', r1 )
    r1 = ra; r1 *= r7; print ( '(', ra, '*=', r7, ') =', r1 )
    r1 = ra; r1 /= r7; print ( '(', ra, '/=', r7, ') =', r1 )
    print ( )

    """Test negate operator."""

    print ( 'r1 =', r1, '; -r1 =', -r1 )
    print ( 'r2 =', r2, '; -r2 =', -r2 )
    print ( )

    """Test read ( ) method."""

    R = Rational.read ( ); i = 1
    while R:
        print ( 'R', i, ' = ', R, sep = '', end = ' ' )
        if type ( R ) != str: print ( '(', float ( R ), ')' ) 
        R = Rational.read ( ); i += 1
    print ( )

def errorTests ( ):
    """Test error conditions."""

    try:
        r5 = Rational ( 5, 0 )
    except ZeroDivisionError:
        sys.stderr.write ( "Error: invalid rational number: 5/0\n" )

if __name__ == "__main__": main ( )
