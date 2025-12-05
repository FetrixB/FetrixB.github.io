# Notebook Manipulation Protocol

## Purpose

A safe protocol for creating, modifying, and extending Jupyter Notebook
(`.ipynb`) files programmatically.

------------------------------------------------------------------------

## 1. Use `nbformat` for All Notebook Operations

-   Load using `nbformat.read()`
-   Write using `nbformat.write()`
-   Create cells using `nbformat.v4` factories
-   **Never modify the JSON by hand**

------------------------------------------------------------------------

## 2. Valid Notebook Structure Requirements

### Notebook-level required fields:

-   `nbformat`
-   `nbformat_minor`
-   `metadata`
-   `cells`

### Cell-level required fields:

-   `cell_type` (`code`, `markdown`, or `raw`)
-   `source` (string or list)
-   `metadata` (dict)
-   `outputs` (for code cells)
-   `execution_count` (for code cells)

------------------------------------------------------------------------

## 3. Allowed Cell Operations

-   Append new cells using `nb.cells.append()`
-   Insert cells using list `.insert()`
-   Modify **only**:
    -   `source`
    -   `metadata`
    -   `outputs`
-   **Do not change** `cell_type` after creation

------------------------------------------------------------------------

## 4. Validation Requirement

Always validate before saving:

    nbformat.validate(nb)

------------------------------------------------------------------------

## 5. Content Guidelines

### For Markdown Cells
- Use standard Markdown syntax

### For Code Cells with HTML Output
- Always import: `from IPython.core.display import HTML`
- Use triple quotes for HTML strings: `HTML("""<div>...</div>""")`
- Escape quotes inside HTML: `style=\"color: red\"`
- Keep HTML demos under 30 lines
- Test incrementally

------------------------------------------------------------------------

## 6. Prohibited Actions

- ❌ **Never** write raw XML/JSON directly
- ❌ **Never** manually edit `.ipynb` as text
- ❌ **Never** create cells without planning first
- ❌ **Never** use placeholder comments like `...existing code...`
- ❌ **Never** batch insert many cells without testing

------------------------------------------------------------------------

## 6. Prohibited Actions

- ❌ **Never** write raw XML/JSON directly
- ❌ **Never** manually edit `.ipynb` as text
- ❌ **Never** create cells without planning first
- ❌ **Never** use placeholder comments like `...existing code...`
- ❌ **Never** batch insert many cells without testing

------------------------------------------------------------------------

## 7. Safe Execution (Optional)

If execution is required, use `nbclient`:

``` python
from nbclient import NotebookClient  
client = NotebookClient(nb)
client.execute()
```

------------------------------------------------------------------------

## 8. Recommended Agent Workflow

1.  Load or initialize a notebook using `nbformat`
2.  Perform requested changes via official APIs only
3.  Validate using `nbformat.validate()`
4.  Save using `nbformat.write()`

------------------------------------------------------------------------

## 9. Python Script for Notebook Creation

Create notebooks programmatically

```bash
source ~/workspace/felix/2025_Adventskalender/.venv/bin/activate
```

```python
import nbformat as nbf
nb = nbf.v4.new_notebook()
nb.cells.append(nbf.v4.new_markdown_cell("# Title"))
nb.cells.append(nbf.v4.new_code_cell("print('Hello')"))
nbf.validate(nb)
with open('output.ipynb', 'w') as f:
    nbf.write(nb, f)
```

------------------------------------------------------------------------
