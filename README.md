# lysqlnb

A Python library for reading and validating Oracle SQL notebooks (`.sqlnb`).

> [!WARNING]
> This package is under development. The API is subject to breaking changes.

## Installation

```shell
pip install lysqlnb
```

## Background

The data models are based on the VS Code [NotebookSerializer API](https://code.visualstudio.com/api/extension-guides/notebook#serializer).

## Usage

```python
>>> from pathlib import Path
>>> import lysqlnb as sqlnb
>>> nb = sqlnb.load(Path("path/to/notebook.sqlnb"))
>>> nb.model_dump_json(indent=2)
{
  "cells": [
    {
      "kind": 1,
      "value": "# This is Markdown.",
      "language_id": "markdown"
    },
    {
      "kind": 2,
      "value": "SELECT * FROM departments;",
      "language_id": "oracle-sql"
    }
  ]
}
```

## Requirements

Python 3.14+

## Licence

[MIT](LICENCE)
