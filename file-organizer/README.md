# File Organizer

Organize files in a directory by extension or modification date. Also find duplicate files by SHA-256 hash.

## Usage

```bash
python organize.py /path/to/folder --by ext
python organize.py /path/to/folder --by date --dry-run
python organize.py /path/to/folder --duplicates
```

## Tests

```bash
pip install pytest
pytest
```
