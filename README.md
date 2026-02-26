# lysqlnb

A library for reading and validating SQL notebook files (`.sqlnb`).

> [!WARNING]
> This project is a work in progress and is not yet ready for use. The API is unstable and subject to breaking changes.

## Installation

```shell
pip install lysqlnb
```

## Background

The data models are based on the VS Code [NotebookSerializer API](https://code.visualstudio.com/api/extension-guides/notebook#serializer).

## Usage

```python
>>> from pathlib import Path
>>> from lysqlnb import Notebook
>>> notebook = Notebook.from_file(Path("path/to/notebook.sqlnb"))
>>> notebook.model_dump_json(indent=2)
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
