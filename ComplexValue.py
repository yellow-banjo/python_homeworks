class Complex:
    def __init__(self, re, im=0.0):
        self.real = re
        self.imag = im

    def _arg(self):
        from math import atan
        from math import pi
        if self.real == 0:
            if self.imag > 0:
                return pi
            else:
                return -pi
        else:
            if self.real > 0:
                return atan(self.imag / self.real)
            else:
                return atan(self.imag / self.real) + pi

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __eq__(self, other):
        from math import isclose
        if isinstance(other, (Complex, complex)):
            return isclose(self.imag, other.imag) and isclose(self.real, other.real)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, (Complex, complex)):
            return self.imag != other.imag and self.real != other.real
        else:
            return True

    def __abs__(self):
        return (self.real * self.real + self.imag * self.imag) ** 0.5

    def __add__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            return Complex(self.real + other, self.imag)

    def __radd__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            return Complex(self.real + other, self.imag)

    def __sub__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            return Complex(self.real - other, self.imag)

    def __rsub__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(other.real - self.real, other.imag - self.imag)
        else:
            return Complex(other - self.real, -self.imag)

    def __mul__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.imag * other.real + self.real * other.imag)
        else:
            return Complex(self.real * other, self.imag * other)

    def __rmul__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.imag * other.real + self.real * other.imag)
        else:
            return Complex(self.real * other, self.imag * other)

    def __truediv__(self, other):
        if isinstance(other, (Complex, complex)):
            return Complex((self.real * other.real + self.imag * other.imag) /
                           (other.real * other.real + other.imag * other.imag),
                           (self.imag * other.real - self.real * other.imag) /
                           (other.real * other.real + other.imag * other.imag))
        else:
            return Complex(self.real / other, self.imag / other)

    def __rtruediv__(self, other):
        return Complex(self.real, self.imag) ** (-1) * other

    def __pow__(self, other):
        from math import e, log
        if isinstance(other, (Complex, complex)):
            mod = self.__abs__() ** other.real * e ** (-other.imag * self._arg())
            arg = other.imag * log(self.__abs__()) + other.real * self._arg()
            real, im = self._recalc(mod, arg)
            return Complex(real, im)
        else:
            real, im = self._recalc(self.__abs__() ** other, self._arg() * other)
            return Complex(real, im)

    def _recalc(self, mod, arg):
        from math import sin, cos
        real = mod * cos(arg)
        im = mod * sin(arg)
        return real, im

    def _sign(self, arg):
        if arg >= 0:
            return '+'
        else:
            return '-'

    def __str__(self):
        if self.real == 0:
            return f"{str(self.imag)}j"
        else:
            return f"({str(self.real)}{self._sign(self.imag)}{str(abs(self.imag))}j)"


def main():
    a = Complex(-5, -3)
    b = complex(2 + 3j)
    c = complex(-5 - 3j)
    print(b * a)
    print(b * c)


if __name__ == '__main__':
    main()









