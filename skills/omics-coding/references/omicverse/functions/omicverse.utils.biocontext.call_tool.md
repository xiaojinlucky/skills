# omicverse.utils.biocontext.call_tool #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.biocontext.call_tool`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.biocontext.call_tool.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Call any BioContext MCP tool by name.

## Signature

```text
omicverse.utils.biocontext. call_tool ( tool_name , ** kwargs )
```

## Parameters

- `tool_name`: ( str ) – The BioContext tool name (e.g. 'get_uniprot_protein_info' ).
- `**kwargs`: ( Any ) – Tool-specific arguments.

## Full Documentation

# omicverse.utils.biocontext.call_tool #

omicverse.utils.biocontext. call_tool ( tool_name , ** kwargs ) [source] #

Call any BioContext MCP tool by name.

Parameters :

-
tool_name ( str ) – The BioContext tool name (e.g. `'get_uniprot_protein_info' `).

-
**kwargs ( `Any `) – Tool-specific arguments.

Returns :

Tool result, automatically parsed from JSON when possible.

Return type :

dict or str
