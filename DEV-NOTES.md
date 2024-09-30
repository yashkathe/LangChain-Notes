# Dev Notes

## PIP

- Virtual Environment

```bash
python3 -m venv name-of-folder
```

- Create requirements.txt

```bash
pip freeze > requirements.txt
```

- Install requirements.txt

```bash
pip install -r requirements.txt
```

## Python

- Ignore Deprecation Warnings

```bash
import warnings

# Ignore all deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=Warning)
```
