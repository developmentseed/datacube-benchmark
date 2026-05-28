# datacube-benchmark

Utilities for benchmarking [Zarr](https://zarr.dev/) datacubes — generate
synthetic stores with different chunking schemes, compressors, and
dtypes, then measure read performance under realistic access patterns.

Companion package to the [Datacube Guide](https://developmentseed.org/datacube-guide/),
which documents common pitfalls when producing and consuming
multi-dimensional data products.

## Installation

```bash
pip install datacube-benchmark
```

Python 3.12+ is required.

## Quickstart

Create a synthetic Zarr store on local disk and time a few random-access
patterns against it:

```python
from pathlib import Path

import obstore as obs
import zarr

import datacube_benchmark

path = Path.cwd() / "data" / "test.zarr"
path.mkdir(parents=True, exist_ok=True)
store = obs.store.LocalStore(str(path))
zarr_store = datacube_benchmark.create_zarr_store(store)

arr = zarr.open_array(zarr_store, zarr_version=3, path="data")
results = datacube_benchmark.benchmark_access_patterns(arr, num_samples=10)
print(results)
```

`create_zarr_store` takes target sizes and chunk shapes as strings or
[`pint`](https://pint.readthedocs.io/) quantities (e.g. `"1 GB"`,
`"10 MB"`), and writes through an [`obstore`](https://developmentseed.org/obstore/)
store — so the same call works against a local directory, S3, GCS, or
Azure by swapping the store.

See the [API reference](api.md) for the full surface.

## License

[MIT](https://github.com/developmentseed/datacube-benchmark/blob/main/LICENSE.txt)
