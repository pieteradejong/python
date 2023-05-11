from abc import ABC, abstractmethod


class DistanceMetric(ABC):
    @abstractmethod
    def calc_distance(self, a, b):
        pass


class Euclidean1D(DistanceMetric):
    def calc_distance(self, a: float, b: float) -> float:
        return abs(a - b)

# class EuclideanNDimensions(DistanceMetric):
#     def calc_distance(self, a: float, b: float) -> float:
#         return abs(a - b)

# import unittest
# class TestEuclidean1D(unittest.TestCase):
#     def test_calc_distance(self, a, b):
#         pass
#
#
# # if __name__ == '__main__':
# #     unittest.main()
