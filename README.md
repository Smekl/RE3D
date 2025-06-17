RE3D
====

A minimal rendering engine project.

This repository contains a basic OBJ model loader written in Python.

## Usage

Install Python 3 and run the following example:

```python
from src.model_loader import load_obj
model = load_obj('path/to/model.obj')
print(f"Loaded {len(model.vertices)} vertices and {len(model.faces)} faces")
```

See `tests/data/cube.obj` for a simple cube model and `tests/test_model_loader.py`
for a usage example.
