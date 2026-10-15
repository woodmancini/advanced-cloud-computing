### bash command to delete all .venv folders starting from cwd:
```
find . -type d -name ".venv" -prune -exec rm -rf {} +
```
### and to find all .venv folders:
```
find . -type d -name ".venv"
```