# Why This Script?

If you, like me, make multiple copies of your files as backup and do not know which one to delete to save storage space, this python script is for you.

This python script will generate a sha256 hash of files to find duplicates, and store them in a CSV. You can then review what you want to keep or discard. You can remove them by running delete commands in a terminal.

# How to run the script?

```
python hashGenerator.py config.yaml
```

``hashGenerator.py`` -> main entry point of the script.
``config.yaml`` -> config that indicates: (1) root path to hash files, (2) recursive indicator (to go through sub directories), (3) file encoding, which is necessary if your directory or file have non utf-8 characters.