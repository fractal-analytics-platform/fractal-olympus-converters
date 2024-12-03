"""OME Zarr converters for Olympus Microscopes"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("fractal-olympus-converters")
except PackageNotFoundError:
    __version__ = "uninstalled"
