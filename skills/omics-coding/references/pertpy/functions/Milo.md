# pertpy.tl.Milo

- Package: pertpy
- Version: 1.1.1
- Language: Python
- Source: local://pertpy/1.1.1/runtime-signature
- Verified at: 2026-07-22

## Purpose

Test differential abundance of local cell neighborhoods rather than only pre-defined cell types. This gives an independent check when a discrete annotation may hide transitional states.

## Verified call chain

```python
import pertpy as pt

milo = pt.tl.Milo()
mdata = milo.load(adata)
milo.make_nhoods(mdata, neighbors_key=None, prop=0.1, seed=11)
mdata = milo.count_nhoods(mdata, sample_col="sampleID")
milo.add_covariate_to_nhoods_obs(mdata, new_covariates=["group"])
milo.da_nhoods(mdata, design="~ group", model_contrasts="groupKPC-groupKC_early", solver="pydeseq2")
```

## Verified signatures

```text
Milo.load(input, feature_key="rna")
Milo.make_nhoods(data, neighbors_key=None, feature_key="rna", prop=0.1, seed=0, copy=False)
Milo.count_nhoods(data, sample_col, feature_key="rna")
Milo.add_covariate_to_nhoods_obs(mdata, new_covariates, feature_key="rna")
Milo.da_nhoods(mdata, design, model_contrasts=None, subset_samples=None, add_intercept=True, feature_key="rna", solver="pydeseq2")
```

## Runtime contract

- Verified interpreter: `/hwdata/home/jinqc/miniconda3/envs/sccoda_py312/bin/python`.
- `pertpy==1.1.1` and `pydeseq2==0.5.4` passed import and dependency checks.
- Build the cell-neighbor graph before `Milo.load()`; record the graph construction settings in the formal analysis script.
- `sample_col` must identify real biological samples, and each contrast must be supported by sample-level replication.
