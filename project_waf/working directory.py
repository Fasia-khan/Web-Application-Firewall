from pathlib import Path

# home would contain something like "/Users/jame"
home = str(Path.home())

path = home + "/Desktop/data-code/Testdata"
print(path)