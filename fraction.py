import numbers

def gcd(m,n):
    while m % n != 0:
      oldm = m
      oldn = n

      m = oldn
      n = oldm % oldn

    return n

class Fraction:

  def __init__(self, top, bottom):
    # validate input: top, bottom need to be int
    if not isinstance(top, numbers.Integral) or not isinstance(bottom, numbers.Integral):
      raise ValueError("Expect two integer arguments")

    common = gcd(top, bottom)
    self.num = top/common
    self.den = bottom/common

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

  def show(self):
    print self.num + "/" , self.den

  def __add__(self, other):
    newnum   = self.num * other.den + other.num * self.den
    newdenom = self.den * other.den
    return Fraction(newnum, newdenom)

  def __radd__(self, other):
    return other.__add__(self)

  def __radd__(self, other):
    # add other to self, then return self

  def __eq__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum == newOtherNum

  def __sub__(self, other):
    subnum = other.num
    subden = other.den * -1
    frac = Fraction(subnum, subden)
    return self.__add__(frac)

  def __mul__(self, other):
    newnum = self.num * other.num
    newden = self.den * other.den
    common = gcd(newnum, newden)
    return Fraction(newnum / common, newden / common)

  def __truediv__(self):
    a = float(self.num)
    b = float(self.den)
    return a/b


  def getNum(self):
    return self.num

  def getDen(self):
    return self.den

  def __gt__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum > newOtherNum

  def __ge__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum >= newOtherNum

  def __lt__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum < newOtherNum

  def __le__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum <= newOtherNum

  def __ne__(self, other):
    newSelfNum = self.num * other.den
    newOtherNum = other.num * self.den
    return newSelfNum != newOtherNum

def main():
  x = Fraction(5,6)
  y = Fraction(1,6)
  z = Fraction(2,6)
  a = Fraction(4, 16)
  b = Fraction(1,4)
  c = Fraction(3,18)

  print "Running tests...."

  print "Substraction: "
  print "Expect 2/3: ", x-y
  print "Expect 1/2: ", x - z

  print "Multiplication: "
  
  print "Expect 5/18: ", x * z
  print "Expect 5/24: ", x * a
  
  print "True division: "
  
  print "Expect .25: ", b.__truediv__()
  
  print "Expect .1667 ", c.__truediv__()

  print "subtracting: "
  print "Expect 2/3: ", Fraction(23,24) - Fraction(7,24)
  print "Expect 2/3: ", Fraction(5,9) - Fraction(-1,9)
  
  print "Inequalities:"
  print "Expect True: ", Fraction(3,4).__gt__(Fraction(1,4)) 
  print "Expect False: ", Fraction(3,4).__gt__(Fraction(4,4)) 

  print "Expect True: ", Fraction(7,15).__ge__(Fraction(7,15)) 
  print "Expect True: ", Fraction(7,15).__ge__(Fraction(3,15)) 
  print "Expect False: ", Fraction(1,3).__ge__(Fraction(2,3)) 

  print "Expect True: ", Fraction(4,24).__lt__(Fraction(5,6)) 
  print "Expect False: ", Fraction(1,2).__lt__(Fraction(-1,2)) 

  print "Expect True: ", Fraction(7,15).__le__(Fraction(7,15)) 
  print "Expect True: ", Fraction(7,15).__le__(Fraction(8,15)) 
  print "Expect True: ", Fraction(16,24).__le__(Fraction(5,6)) 

  print "Expect True: ", Fraction(1,2).__ne__(Fraction(1,3))
  print "Expect True: ", Fraction(1,2).__ne__(Fraction(-5,3)) 
  print "Expect False: ", Fraction(16,24).__ne__(Fraction(8,12)) 

  #print "Expect ValueError: ", Fraction(.5,1)




  print "(Finished) Running tests...."
main()


