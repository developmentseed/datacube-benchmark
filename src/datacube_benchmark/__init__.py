from .create import (
    create_empty_dataarray,
    create_zarr_store,
    create_or_open_zarr_array,
    create_or_open_zarr_store,
)
from .config import Config
from .query import benchmark_zarr_array, benchmark_access_patterns
from .open import benchmark_dataset_open

try:
    from ._version import __version__
except ImportError:  # pragma: no cover - _version.py is generated at build time
    __version__ = "0.0.0+unknown"

__all__ = [
    "__version__",
    "Config",
    "create_empty_dataarray",
    "create_zarr_store",
    "create_or_open_zarr_array",
    "create_or_open_zarr_store",
    "benchmark_zarr_array",
    "benchmark_access_patterns",
    "benchmark_dataset_open",
]
