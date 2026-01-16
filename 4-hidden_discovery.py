#!/usr/bin/python3
import marshal

def main():
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # ignorer l'en-tête du .pyc
        code = marshal.load(f)
    names = sorted(name for name in code.co_names if not name.startswith("__"))
    for name in names:
        print(name)

if __name__ == "__main__":
    main()
