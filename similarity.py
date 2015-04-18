import math

# assumes two points in R^2 (points in 2D-space)
class SimilarityMeasures():

  def euclidian(self, a, b):
    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )

  def manhattan(self, a, b):
    return ( math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1]) ) 


  #def minkowski(self, a, b):
    #


  #def cosine(self, a, b):
    #



  #def jaccard(self, a, b):
    #

  def main(self):
    print "Testing distance metrics..."

    print "Euclidean distance:"
    print "Expect ", math.sqrt(5)," " , self.euclidian((0,0), (1,2))
    print "Expect ", math.sqrt(25+11*11)," " , self.euclidian((-2,-5), (3,6))

    print "Manhattan distance:"
    print "Expect 16", self.manhattan((1,2), (10, -5))
    print "Expect 32", self.manhattan((10, 18), (2, -6))

if __name__ == '__main__':
  SimilarityMeasures().main()
