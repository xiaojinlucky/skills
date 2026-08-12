# omicverse.single.pyCEFCON #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pyCEFCON`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pyCEFCON.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

CEFCON workflow wrapper for driver-regulator discovery.

## Signature

```text
class omicverse.single. pyCEFCON ( input_expData , input_priorNet , input_genesDE = None , additional_edges_pct = 0.01 , cuda = 0 , seed = 2023 , hidden_dim = 128 , output_dim = 64 , heads = 4 , attention = 'COS' , miu = 0.5 , epochs = 350 , repeats = 5 , edge_threshold_param = 8 , remove_self_loops = False , topK_drivers = 100 , solver = 'GUROBI' )
```

## Parameters

- `input_expData`: ( str or AnnData or pd.DataFrame ) – Input expression data with optional lineage metadata.
- `input_priorNet`: ( str or pd.DataFrame ) – Prior interaction network.
- `input_genesDE`: ( str or pd.DataFrame , optional ) – Differential-expression score table.
- `repeats`: ( int , default=5 ) – Number of model repeats.
- `solver`: ( {'GUROBI' , 'SCIP'} , default='GUROBI' ) – ILP solver used for driver-regulator selection.
- `additional_edges_pct`: Detected from function signature; no parameter description detected.
- `cuda`: Detected from function signature; no parameter description detected.
- `seed`: Detected from function signature; no parameter description detected.
- `hidden_dim`: Detected from function signature; no parameter description detected.
- `output_dim`: Detected from function signature; no parameter description detected.
- `heads`: Detected from function signature; no parameter description detected.
- `attention`: Detected from function signature; no parameter description detected.
- `miu`: Detected from function signature; no parameter description detected.
- `epochs`: Detected from function signature; no parameter description detected.
- `edge_threshold_param`: Detected from function signature; no parameter description detected.
- `remove_self_loops`: Detected from function signature; no parameter description detected.
- `topK_drivers`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.single.pyCEFCON #

class omicverse.single. pyCEFCON ( input_expData , input_priorNet , input_genesDE = None , additional_edges_pct = 0.01 , cuda = 0 , seed = 2023 , hidden_dim = 128 , output_dim = 64 , heads = 4 , attention = 'COS' , miu = 0.5 , epochs = 350 , repeats = 5 , edge_threshold_param = 8 , remove_self_loops = False , topK_drivers = 100 , solver = 'GUROBI' ) [source] #

CEFCON workflow wrapper for driver-regulator discovery.

Parameters :

-
input_expData ( str or AnnData or pd.DataFrame ) – Input expression data with optional lineage metadata.

-
input_priorNet ( str or pd.DataFrame ) – Prior interaction network.

-
input_genesDE ( str or pd.DataFrame , optional ) – Differential-expression score table.

-
repeats ( int , default=5 ) – Number of model repeats.

-
solver ( {'GUROBI' , 'SCIP'} , default='GUROBI' ) – ILP solver used for driver-regulator selection.

__init__ ( input_expData , input_priorNet , input_genesDE = None , additional_edges_pct = 0.01 , cuda = 0 , seed = 2023 , hidden_dim = 128 , output_dim = 64 , heads = 4 , attention = 'COS' , miu = 0.5 , epochs = 350 , repeats = 5 , edge_threshold_param = 8 , remove_self_loops = False , topK_drivers = 100 , solver = 'GUROBI' ) [source] #

Parameters :

-
pd.DataFrame ) ( input_genesDE ( str or )

-
pd.DataFrame )

-
pd.DataFrame )

-
( float ( miu )

-
optional ) ( Solver ( 'GUROBI' , 'SCIP' ) for solving the integer linear programming problems ( for identifying drive regulators ) ( default: 'GUROBI' ) )

-
( int ( topK_drivers )

-
optional )

-
( int

-
optional )

-
( int

-
optional )

-
( int

-
optional )

-
( int

-
optional )

-
( str ( solver )

-
optional )

-
( float

-
optional )

-
( int

-
optional )

-
( int

-
optional )

-
( int

-
optional )

-
( bool ( remove_self_loops )

-
optional )

-
( int

-
optional )

-
( str

-
optional )

Return type :

None

Methods

`__init__ `(input_expData, input_priorNet[, ...])

`predicted_RGM `()

`predicted_driver_regulators `()

`preprocess `()

`train `()
