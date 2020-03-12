import unittest
from ..utils import _is_left, _point_in_poly, _import_file


class UtilsTest(unittest.TestCase):

    def test_is_left(self):
        points1 = [0, 0, 0, 1, 1, 0]   # origin on the left
        self.assertTrue(_is_left(*points1) > 0)

        points2 = [0, 0, 0, -1, 1, 0]  # origin on the right
        self.assertTrue(_is_left(*points2) < 0)

        points3 = [0, 0, 1, 0, -1, 0]  # origin on the line
        self.assertTrue(_is_left(*points3) == 0)

    def test_point_in_poly(self):
        # Convex U shape facing west
        vertices = [[0, 0], [0, 2], [3, 2], [3, 0], [2, 0], [2, 1], [1, 1], [1, 0]]
        point1 = [1.5, 1.5]     # inside vertical area
        self.assertTrue(_point_in_poly(point1, vertices))
        self.assertTrue(_point_in_poly(point1, vertices, 'rc'))

        point2 = [1.5, 0.5]     # outside between horizontal areas
        self.assertFalse(_point_in_poly(point2, vertices))
        self.assertFalse(_point_in_poly(point2, vertices, 'rc'))

        point3 = [4, 2]         # outside above
        self.assertFalse(_point_in_poly(point3, vertices))
        self.assertFalse(_point_in_poly(point3, vertices, 'rc'))

        point4 = [2.5, 0.5]     # inside top horizontal area
        self.assertTrue(_point_in_poly(point4, vertices))
        self.assertTrue(_point_in_poly(point4, vertices, 'rc'))

    def test_import_file(self):
        # TODO: mock the input files
        name, vertices = _import_file("./data/SICS.txt")
        self.assertEqual("site", name)
        self.assertTrue(type(vertices) == list)
        self.assertTrue(len(vertices) > 0)

        name1, vertices1 = _import_file("./data/sics.json")
        self.assertTrue(type(name1) == str)
        self.assertTrue(name1 == 'sics')
        self.assertTrue(type(vertices1) == list)
        self.assertTrue(len(vertices1) > 0)

        self.assertRaises(FileNotFoundError, lambda: _import_file("/path-not-exist"))
        self.assertRaises(ValueError, lambda: _import_file('./data/bad.txt'))
        self.assertRaises(ValueError, lambda: _import_file('./data/map.png'))
