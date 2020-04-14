# geofencing

[![Build Status](https://travis-ci.com/CarmenLee111/geofencing.svg?branch=dev)](https://travis-ci.com/CarmenLee111/geofencing)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/CarmenLee111/SandboxJulia.jl?svg=true)](https://ci.appveyor.com/project/CarmenLee111/geofencing)

geofencing is a tool for checking whether a GPS coordinates is inside of a geo-fence.

# Installation on Mac or Linux
Clone the repository to your local file system.
```bash
$ git clone https://github.com/CarmenLee111/geofencing.git
```

It is recommended to install it under a python virtual environment
```bash
$ python3 -m venv ~/venv/env_name
$ source ~/venv/env_name/bin/activate
(env_name) $ cd geofencing
(env_name) $ python3 setup.py install
```

Verify the installation in a python console

```python
>>> from geofencing import Fence
>>>
```
