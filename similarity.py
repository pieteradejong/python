import math

class SimilarityMeasures():

  #def __init__(self):
  #  main()

  def euclidian(self, a, b):
    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 )



  #def manhattan(self, a, b):
    #


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

if __name__ == '__main__':
  SimilarityMeasures().main()
