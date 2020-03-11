from .utils import _point_in_poly, _import_file


class Fence(object):
    """
        The Fence object contains all the vertices information
            and method for detecting whether a point is inside of the geo-fence

        Example:
            >>> point = [59.405014, 17.949540]
            >>> fence = Fence()
            >>> fence.set_vertices_from_file('data/SICS.txt')
            >>> fence.detect(point)
            True
    """

    def __init__(self, vs=None):
        self._vertices = []
        if vs:
            self.vertices = vs

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vs):
        assert len(vs) >= 6, "polygon need to have at least three vertices"
        assert len(vs) % 2 == 0, "list must contain latitude, longitude pairs"
        self._vertices = vs

    def set_vertices_from_file(self, file):
        self.vertices = _import_file(file)

    def detect(self, point: list, algo=None):
        assert len(point) == 2, "coordinates must be latitude, longitude"
        return _point_in_poly(point, self._vertices, algo)
