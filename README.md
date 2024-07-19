# pydomify
Engine to build html documents

## Build project for PyPI
```
python -m pip install build twine
python -m build
twine check dist/*
twine upload -r testpypi dist/*
twine upload dist/*
```