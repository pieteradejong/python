import math
import sys

# assumes two points in R^2 (points in 2D-space)
class SimilarityMeasures():

  def euclidian(self, a, b):
    return self.minkowski(a, b, 2)

  def manhattan(self, a, b):
    return self.minkowski(a, b, 1)

  def minkowski(self, a, b, p):
    p = float(p) # ensure 1/p is accurate when p is int
    sum = math.fabs(a[0]-b[0])**p + math.fabs(a[1]-b[1])**p 
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
    print "Testing distance metrics...\n"

    print "\nEuclidean distance:\n"
    print "Expect ", math.sqrt(5)," actual: " , self.euclidian((0,0), (1,2))
    print "Expect ", math.sqrt(25+11*11)," actual: " , self.euclidian((-2,-5), (3,6))

    print "\nManhattan distance:\n"
    print "Expect 16.0, actual: ", self.manhattan((1,2), (10, -5))
    print "Expect 32.0, actual: ", self.manhattan((10, 18), (2, -6))

    print "\nMinkowski distance:\n"
    print "Expect: ", math.sqrt(25+11*11), " actual: ", self.minkowski( (-2,-5), (3,6), 2 ) #Euclidan
    print "Expect: ", self.manhattan((10,18), (2,-6)), " actual: ", self.minkowski( (10,18), (2,-6), 1 ) #Euclidan
    print "Expect ~12.749", self.minkowski((1,2), (10, -5), 1.5) #manual calc
    print "Expect ~24.175", self.minkowski((10, 15), (2, -6), 1.5) #manual calc

    print "\ncosine distance:\n"
    print "Expect 0.0", self.cosine((1,2), (10, -5)) #manual calc
    print "Expect ~-0.676", self.cosine((10, 18), (2, -6))

    print "\njaccard distance:\n"
    print "Expect ~.333", self.jaccard(['a', 'b', 'c'], ['a'])
    print "Expect =.5", self.jaccard(['frodo', 'bilbo', 'gandalf'], ['gollum', 'elrond', 'frodo', 'samwise', 'bilbo', 'gandalf'])
    print "Expect 0.0", self.jaccard(['a', 'b', 'c'], ['d', 'e', 'f'])
    print "Expect 1.0", self.jaccard(['a', 'b', 'c'], ['a', 'b', 'c'])

    # todo: calculate all distances for similar numbers -> compare

if __name__ == '__main__':
  SimilarityMeasures().main()



