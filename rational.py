

#importing sys module
import sys

#implementation of a rational class
class Rational:

#def __init__ ( self, num = 0, den = 1 ): This function (constructor) creates a Rational number with the numerator num and denominator den.

    def __init__(self, num=0, den=1):         #constructor
        self.num = num
        self.den = den
        if den == "":
            return num
        
        def gcd(num, den):                    #function to reduse rational number to its lowest form
            a = num
            b = den
            while a % b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            ret_n = num // b
            ret_d = den // b
            return ret_n, ret_d

        if self.num < 0 and self.den < 0:
            self.num = self.num
        (self.num, self.den) = gcd(self.num, self.den)


#def __add__ ( self, other ): This function overload the arithmetic operator: + for the Rational class.

    def __add__(self, other):
        if self.den == other.den:
            return Rational(self.num + other.num, other.den)
        else:
            return Rational((self.num * other.den) + (other.num * self.den), self.den * other.den)


#def __sub__ ( self, other ): This function overload the arithmatic operator: - for the Rational class.

    def __sub__(self, other):
        if self.den == other.den:
            return Rational(self.num - other.num, other.den)
        else:
            return Rational((self.num * other.den) - (other.num * self.den), self.den * other.den)


#def __mul__(self, other): This function overload the arithmatic operator: * for the rational class.

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)


#def __truediv__ ( self, other ): These functions overload the arithmetic operators: / for the Rational class.

    def __truediv__(self, other):
        return Rational(self.num * other.den, self.den * other.num)


#def __neg__ ( self ): This function overloads the negate operator ( - ) for the Rational class.

    def __neg__(self):
        return Rational(-self.num, self.den)


#def __eq__ ( self, other ): These functions overload the relational operators: == for the Rational class.

    def __eq__(self, other):
        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False


#def __ne__ ( self, other ): These functions overload the relational operators: != for the Rational class.

    def __ne__(self, other):
        if self.num * other.den != self.den * other.num:
            return True
        else:
            return False


#def __lt__ ( self, other ):These functions overload the relational operators: < for the Rational class.

    def __lt__(self, other):
        if self.num * other.den < self.den * other.num:
            return True
        else:
            return False


#def __le__ (self, other ):These functions overload the relational operators: <= for the Rational class.

    def __le__(self, other):
        if self.num * other.den <= self.den * other.num:
            return True
        else:
            return False


#def __gt__ ( self, other ):These functions overload the relational operators: > for the Rational class.

    def __gt__(self, other):
        if self.num * other.den > self.den * other.num:
            return True
        else:
            return False


#def __ge__ ( self, other ): These functions overload the relational operators: >= for the Rational class.

    def __ge__(self, other):
        if self.num * other.den >= self.den * other.num:
            return True
        else:
            return False


#def __float__ ( self ): This function overloads the float ( ) operator for the Rational class.It converts a Rational number to a floating-point number.

    def __float__(self):
        return float(self.num) / self.den


#def __str__ ( self ): This function can be used to print out a Rational number

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)


#def read ( ): This function overloads the readline ( ) function from the sys package, which can be used to read a Rational number from the stdin.

    def read():
        line = sys.stdin.readline()
        while (line):
            read = line.strip().split("/")
            if len(read) == 2 and read[1].strip().isdigit():
                return Rational(int(read[0]), int(read[1]))
            elif len(read) == 1 and read[0].isdigit():
                return Rational(int(read[0]))
            else:
                sys.stderr.write("Error: invalid rational number:" + line)
                return " "
           






 
