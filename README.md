# geofencing

[![Build Status](https://travis-ci.com/CarmenLee111/geofencing.svg?branch=dev)](https://travis-ci.com/CarmenLee111/geofencing)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/CarmenLee111/SandboxJulia.jl?svg=true)](https://ci.appveyor.com/project/CarmenLee111/geofencing)

geofencing` is a simple tool for checking whether a GPS coordinates is inside of a geo-fence. 
Geo-fences can be generated using [Fence Editor](http://geo.jasparke.net/) and saved as json files. 

The solutions to the classic point-in-polygon problem are implemented with one method modified 
to allow detection for edge cases.

The detection allows the choices of different implementations or algorithms:
- 'rc': naive implementation of ray casting
- 'wn': native implementation of winding number
- 'rc_vectorized': vectorized implementation of ray casting
- 'wn_vectorized': vectorized implementation of winding number
- 'wn_edge': modified winding number allowing detection for edge cases.

# Installation on Mac or Linux
Dependency: Python3+, numpy

Clone the repository to your local file system.
```bash
$ git clone https://github.com/carlee0/geofencing.git
```

It is recommended to install it under a python virtual environment
```bash
$ python3 -m venv <path/to/env_name>
$ source <path/to/env_name>/bin/activate
(env_name) $ cd geofencing
(env_name) $ python3 setup.py install
```

Verify the installation in a python console

```python
>>> from geofencing import Fence
>>>
```

# Usage

```python
>>> point = [59.405014, 17.949540]
>>> fence = Fence()
>>> fence.set_vertices_from_file('data/sics.json')
>>> fence.detect(point)
True
>>>fence.detect(point, 'rc')
True
```