def _point_in_poly(point: list, vertices: list, algo="wn"):
    """ determine if a point is in the polygon

    Args:
        point -- latitude, longitude of the point to test
        vertices -- defined region [lat0, lon0, lat1, lon1, ...], counter-clock order
        algo -- default "wn"-winding_number, other option "rc"-ray_casting

    Returns:
        True if the point is inside of the polygon, boundary points undefined
    """
    if algo == 'rc':
        return _rc_point_in_poly(point, vertices)
    else:
        return _wn_point_in_poly(point, vertices)


def _is_left(y0, x0, y1, x1, y2, x2):
    """ determine if a point on the left of a line using cross-product rule

    Args:
        y0, x0 -- latitude and longitude of point to test
        y1, x1 -- latitude and longitude of end point 1 of line
        y2, x2 -- latitude and longitude of end point 2 of line

    Returns:
        >0 if it is on the left
        <0 if it is on the right
        =0 if it is on the line
    """
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


def _wn_point_in_poly(point: list, vertices: list):
    """ determin if a point is in the polygon using winding number algorithm

    Args:
        point -- latitude, longitude of the point to test
        vertices -- defined region [lat0, lon0, lat1, lon1, ...], counter-clock order

    Returns:
        True if the point is inside of the polygon (when wn != 0). Undefined on boundary
    """
    wn = 0
    n = len(vertices) // 2

    for i in range(n):
        j = (i + 1) % n
        if vertices[i * 2] <= point[0]:
            if (vertices[j * 2] > point[0]) and (
                    _is_left(*point, *vertices[i * 2:i * 2 + 2], *vertices[j * 2:j * 2 + 2]) > 0):
                wn += 1
        else:
            if (vertices[j * 2] <= point[0]) and (
                    _is_left(*point, *vertices[i * 2:i * 2 + 2], *vertices[j * 2:j * 2 + 2]) < 0):
                wn -= 1
    return wn != 0


def _rc_point_in_poly(point: list, vertices: list):
    """ determine if a point is in the polygon using ray casting algorithm

    Args:
      point -- [latitude, longitude]
      vertices -- list of vertices of the defined region [lat0, lon0, lat1, lon1, ...]

    Returns:
      True if the point is inside of the polygon. Undefined on the boundary
    """
    inside = False
    n = len(vertices) // 2
    j = n - 1
    lat, lon = point

    for i in range(n):
        if ((vertices[i * 2] < lat <= vertices[j * 2]
             or vertices[j * 2] < lat <= vertices[i*2])
                and (vertices[i*2+1] <= lon or vertices[j*2+1] <= lon)):
            k = (lat - vertices[i*2]) / (vertices[j*2] - vertices[i*2])
            inside ^= (vertices[i*2+1] + k * (vertices[j*2+1] - vertices[i*2+1]) < lon)
        j = i

    return inside


def _import_file(file_path):
    """ import coordinates from file

    Args:
      file_path -- file path
        example file:
            59.4048184072506,17.9478923473923
            59.4043815528131,17.9485360775559
            59.404422508156,17.9486433659165
            59.4044197778013,17.9486621413796

    Returns:
        a list of floats [lat0, lon0, lat1, lon1, ...]
    """
    try:
        with open(file_path) as file:
            lines = list(file)
            vs = []
            for line in lines:
                line = line.strip().split(',')
                for d in line:
                    vs.append(float(d))
            return vs
    except FileNotFoundError:
        raise
    except ValueError:
        raise ValueError("File must contain only floats, separated by \',\' and \\n")
