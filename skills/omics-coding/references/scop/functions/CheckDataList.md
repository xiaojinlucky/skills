# Check and preprocess a list of Seurat objects

- Package: scop
- Language: R
- Function: `CheckDataList`
- Source: https://mengxu98.github.io/scop/reference/CheckDataList.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CheckDataList.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

This function checks and preprocesses a list of Seurat objects. It performs various checks on the input, including verification of input types, assay type consistency, feature name consistency, and batch column consistency. It also performs data normalization and variable feature finding based on the specified parameters. Finally, it prepares the data for integration analysis based on the highly variable features.

## Signature

```text
CheckDataList( srt_list, batch, assay = NULL, do_normalization = NULL, normalization_method = "LogNormalize", do_HVF_finding = TRUE, HVF_source = "separate", HVF_method = "vst", nHVF = 2000, HVF_min_intersection = 1, HVF = NULL, vars_to_regress = NULL, cores = 1L, verbose = TRUE, seed = 11 )
```

## Parameters

- `srt_list`: A list of Seurat objects to be checked and preprocessed.
- `batch`: A character string specifying the batch variable name.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `do_normalization`: Whether data normalization should be performed. Default is TRUE.
- `normalization_method`: The normalization method to be used. Possible values are "LogNormalize", "SCT", "TFIDF", and "scran". Default is "LogNormalize".
- `do_HVF_finding`: Whether to perform high variable feature finding. If TRUE, the function will force to find the highly variable features (HVF) using the specified HVF method.
- `HVF_source`: The source of highly variable features. Possible values are "global" and "separate". Default is "separate".
- `HVF_method`: The method to use for finding highly variable features. Options are "vst", "mvp", "disp", or "scran". Default is "vst".
- `nHVF`: The number of highly variable features to select. If NULL, all highly variable features will be used. Default is 2000.
- `HVF_min_intersection`: The feature needs to be present in batches for a minimum number of times in order to be considered as highly variable. Default is 1.
- `HVF`: A vector of feature names to use as highly variable features. If NULL, the function will use the highly variable features identified by the HVF method.
- `vars_to_regress`: A vector of variable names to include as additional regression variables. Default is NULL.
- `cores`: Number of CPU cores used by supported preprocessing steps. Default is 1.
- `verbose`: Whether to print the message. Default is TRUE.
- `seed`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Check and preprocess a list of Seurat objects

## Usage

```text
CheckDataList( srt_list, batch, assay = NULL, do_normalization = NULL, normalization_method = "LogNormalize", do_HVF_finding = TRUE, HVF_source = "separate", HVF_method = "vst", nHVF = 2000, HVF_min_intersection = 1, HVF = NULL, vars_to_regress = NULL, cores = 1L, verbose = TRUE, seed = 11 )
```

## Description

This function checks and preprocesses a list of Seurat objects. It performs various checks on the input, including verification of input types, assay type consistency, feature name consistency, and batch column consistency. It also performs data normalization and variable feature finding based on the specified parameters. Finally, it prepares the data for integration analysis based on the highly variable features.

## Value

A list containing the preprocessed Seurat objects, the highly variable features, the assay name, and the type of assay.
