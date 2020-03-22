import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geofencing",
    version="0.0.1",
    author="Carmen Lee",
    author_email="mailtocarmenlee@gmail.com",
    description="Simple geo-fencing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CarmenLee111/geofencing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
