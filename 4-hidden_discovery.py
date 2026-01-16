#!/usr/bin/python3
import marshal

# ouvre le .pyc correct
with open("/tmp/hidden_4.pyc", "rb") as f:
    f.read(16)  # saute l'en-tête du pyc
    code = marshal.load(f)

names = [name for name in code.co_names if not name.startswith("__")]
for name in sorted(names):
    print(name)
