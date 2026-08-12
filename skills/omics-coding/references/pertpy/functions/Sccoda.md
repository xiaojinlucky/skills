# pertpy.tl.Sccoda

- Package: pertpy
- Version: 1.1.1
- Language: Python
- Source: local://pertpy/1.1.1/runtime-signature
- Verified at: 2026-07-22

## Purpose

Model sample-level cell-type compositions with a Bayesian compositional model. Use real biological samples, not cell-level pseudo-replicates, as the statistical unit.

## Verified call chain

```python
import pertpy as pt

sccoda = pt.tl.Sccoda()
mdata = sccoda.load(
    adata,
    type="cell_level",
    generate_sample_level=True,
    cell_type_identifier="celltype",
    sample_identifier="sampleID",
    covariate_obs=["group"],
)
mdata = sccoda.prepare(mdata, formula="group", reference_cell_type="automatic")
sccoda.run_nuts(mdata, num_samples=10000, num_warmup=1000, rng_key=11)
sccoda.set_fdr(mdata, est_fdr=0.05)
effects = sccoda.get_effect_df(mdata)
credible = sccoda.credible_effects(mdata, est_fdr=0.05)
```

## Verified signatures

```text
Sccoda.load(adata, type, generate_sample_level=True, cell_type_identifier=None, sample_identifier=None, covariate_uns=None, covariate_obs=None, covariate_df=None, modality_key_1="rna", modality_key_2="coda")
Sccoda.prepare(data, formula, reference_cell_type="automatic", automatic_reference_absence_threshold=0.05, modality_key="coda")
Sccoda.run_nuts(data, modality_key="coda", num_samples=10000, num_warmup=1000, rng_key=0, copy=False, *args, **kwargs)
Sccoda.set_fdr(data, est_fdr, modality_key="coda", *args, **kwargs)
Sccoda.get_effect_df(data, modality_key="coda")
Sccoda.credible_effects(data, modality_key="coda", est_fdr=None)
```

## Runtime contract

- Verified interpreter: `/hwdata/home/jinqc/miniconda3/envs/sccoda_py312/bin/python`.
- Use `pertpy==1.1.1` on Python 3.12; this is the maintained replacement for the retired standalone TensorFlow `sccoda` package.
- `cell_type_identifier` and `sample_identifier` must name columns present in `adata.obs`.
- The formula is evaluated on sample-level covariates. With three groups, use planned contrasts or a clearly stated reference group instead of interpreting every coefficient as a monotonic time trend.
- `run_nuts(..., copy=False)` and `set_fdr(..., copy=False)` modify the supplied AnnData/MuData in place and return `None`; do not assign their return values back to the data object.
- For sample-level input under pertpy 1.1.1, set the sample index name to `"obs"` before `load()` so the ArviZ posterior coordinates match the expected dimension name.
