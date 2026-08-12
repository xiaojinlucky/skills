# Create HDF5 data file from Seurat object

- Package: scop
- Language: R
- Function: `CreateDataFile`
- Source: https://mengxu98.github.io/scop/reference/CreateDataFile.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CreateDataFile.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create HDF5 data file from Seurat object

## Signature

```text
CreateDataFile( srt, data_file, name = NULL, assays = "RNA", layers = "data", compression_level = 6, overwrite = TRUE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `data_file`: Path to the output data file. If not provided, the file will be named "data.hdf5" in the current directory.
- `name`: Name of the dataset. If not provided, the name will default to the Seurat object's project name.
- `assays`: The assays to include in the data file. Default is "RNA".
- `layers`: The layers to include in the data file. Default is "data".
- `compression_level`: Compression level for the HDF5 dataset. Default is 6.
- `overwrite`: Whether to overwrite existing data in the data file. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Create HDF5 data file from Seurat object

## Usage

```text
CreateDataFile( srt, data_file, name = NULL, assays = "RNA", layers = "data", compression_level = 6, overwrite = TRUE, verbose = TRUE )
```

## Description

Create HDF5 data file from Seurat object
