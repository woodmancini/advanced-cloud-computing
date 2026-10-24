## bash command to delete all .venv folders starting from cwd:
```
find . -type d -name ".venv" -prune -exec rm -rf {} +
```

find . : Starts the search in your current directory (.) and works its way down.

-type d : Restricts the search to directories only (ignoring any standard files that might happen to be named .venv).

-name ".venv" : Looks for folders with this exact name.

-prune : Tells find not to look inside the .venv folders. This makes the command much faster and prevents "No such file or directory" errors that happen when find tries to search a folder it just deleted.

-exec: Tells find to execute a shell command on the items it just matched.

rm -rf: The standard Linux remove command. -r (recursive) is required to delete folders and their contents, and -f (force) ensures it doesn't pause to ask you for confirmation for every single file.

{}: The placeholder. find automatically substitutes these curly brackets with the actual file paths of the .venv folders it discovered.

+: The batch execution flag. This is a crucial performance optimizer. If you used a semicolon (\;) here instead of +, find would launch a brand new rm -rf process for every single folder it found. The + bundles all the discovered paths together and runs the command exactly once (e.g., rm -rf folder/one folder/two folder/three), which is significantly faster and uses less CPU.

### so, to find all .venv folders:
```
find . -type d -name ".venv"
```

## show only directories in cwd:
```
ls -d */
```

#### double up single quotes to escape them in SQL strings:
```
'Gravity''s Rainbow'
```

### edit Git config file (Powershell):
```
git config --global -e
```

### and add new alias under [alias]
```
[alias]
    acp = "!f() { git add . && git commit -m \"$1\" && git push origin main; }; f"
```

### pull from upstream repo while defaulting to their (changed) versions of files
```
git pull upstream main -X theirs
```