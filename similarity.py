import math
import sys

# assumes two points in R^2 (points in 2D-space)
class SimilarityMeasures():

  def euclidian(self, a, b):
    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

  def manhattan(self, a, b):
    return ( math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1]) ) 


  def minkowski(self, a, b, p):
    if p == 1:
      return self.manhattan(a, b)
    elif p == 2:
      return self.euclidian(a, b)
    else:
      sum = (math.fabs(a[0]-b[0]))**p + (math.fabs(a[1]-b[1])**p)
      return sum**(1/p)


  def cosine(self, a, b):
    dotprod = a[0] * b[0] + a[1] * b[1]
    a_Magnitude = math.sqrt(a[0]**2 + a[1]**2)
    b_Magnitude = math.sqrt(b[0]**2 + b[1]**2)
    res = float(dotprod) / (a_Magnitude * b_Magnitude)
    return res

  def jaccard(self, a, b):
    a_set = set(a)
    b_set = set(b)
    size_of_intersection = len( a_set.intersection(b_set) )
    size_of_union = len( a_set.union(b_set) )
    return float(size_of_intersection) / size_of_union
    

  def main(self):
    print "Testing distance metrics..."

    print "Euclidean distance:"
    print "Expect ", math.sqrt(5)," " , self.euclidian((0,0), (1,2))
    print "Expect ", math.sqrt(25+11*11)," " , self.euclidian((-2,-5), (3,6))

    print "Manhattan distance:"
    print "Expect 16", self.manhattan((1,2), (10, -5))
    print "Expect 32", self.manhattan((10, 18), (2, -6))

    print "minkowski distance:"
    print "Expect ", self.minkowski((1,2), (10, -5), 1.5)
    print "Expect ", self.minkowski((10, 18), (2, -6), 1.5)

    print "cosine distance:"
    print "Expect ", self.cosine((1,2), (10, -5))
    print "Expect ", self.cosine((10, 18), (2, -6))

    print "jaccard distance:"
    print "Expect .333", self.jaccard(['a', 'b', 'c'], ['a'])
    #print "Expect ", self.cosine((10, 18), (2, -6))


if __name__ == '__main__':
  SimilarityMeasures().main()
