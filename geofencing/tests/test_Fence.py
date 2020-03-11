import unittest
from unittest.mock import patch
from ..fence import Fence


class FenceTest(unittest.TestCase):

    vs = [0, 0, 1, 1, 2, 0]

    def test_fence(self):
        fence = Fence(self.vs)
        self.assertIsInstance(Fence(), type(fence))
        self.assertRaises(AssertionError, lambda: Fence([1, 2]))
        self.assertRaises(AssertionError, lambda: Fence([1, 2, 3, 4, 5, 6, 7]))

    def test_get_vertices(self):
        fence = Fence(self.vs)
        self.assertEqual(fence.vertices, self.vs)

    def test_set_vertices(self):
        fence = Fence(self.vs)
        vs2 = [1, 1, 2, 0, 0, 0]
        fence.vertices = vs2
        self.assertEqual(fence.vertices, vs2)

    @patch('geofencing.fence._import_file', return_value='someList')
    def test_vertices_from_file(self, mock_import):
        fence = Fence(self.vs)
        self.assertEqual(None, fence.set_vertices_from_file('/path'))
        self.assertEqual('someList', fence.vertices)

    @patch('geofencing.fence._point_in_poly', return_value=None)
    def test_detect(self, mock_poly):
        fence = Fence(self.vs)
        point1 = [1, 0.5]
        self.assertEqual(None, fence.detect(point1))
        self.assertEqual(None, fence.detect(point1, 'rc'))

        point2 = [1]
        self.assertRaises(AssertionError, lambda: fence.detect(point2))
        self.assertRaises(AssertionError, lambda: fence.detect(point2, 'rc'))
