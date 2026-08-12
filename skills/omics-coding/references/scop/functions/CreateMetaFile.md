# Create Meta File in HDF5 format from Seurat object

- Package: scop
- Language: R
- Function: `CreateMetaFile`
- Source: https://mengxu98.github.io/scop/reference/CreateMetaFile.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CreateMetaFile.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create Meta File in HDF5 format from Seurat object

## Signature

```text
CreateMetaFile( srt, meta_file, name = NULL, write_tools = FALSE, write_misc = FALSE, ignore_nlevel = 100, compression_level = 6, overwrite = TRUE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `meta_file`: Path to the output meta file. If not provided, the file will be named "meta.hdf5" in the current directory.
- `name`: Name of the dataset. If not provided, the name will default to the Seurat object's project name.
- `write_tools`: Whether to write the tools information to the meta file. Default is FALSE.
- `write_misc`: Whether to write the miscellaneous information to the meta file. Default is FALSE.
- `ignore_nlevel`: The number of levels above which a metadata field will be ignored. Default is 100.
- `compression_level`: The level of compression for the meta file. Default is 6.
- `overwrite`: Whether to overwrite existing metadata and reductions in the meta file. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Create Meta File in HDF5 format from Seurat object

## Usage

```text
CreateMetaFile( srt, meta_file, name = NULL, write_tools = FALSE, write_misc = FALSE, ignore_nlevel = 100, compression_level = 6, overwrite = TRUE, verbose = TRUE )
```

## Description

Create Meta File in HDF5 format from Seurat object
