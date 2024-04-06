from pathlib import Path
from typing import Callable

def scan_python_1(path: Path)-> int:
    sloc = 0
    with path.open() as source:
        for line in source:
            line = line.strip()
            if line and not line.startswith('#'):
                sloc += 1
    print(path.relative_to(path.parent), ":", sloc)
    return sloc 

def count_sloc(path: Path, scanner: Callable[[Path], int])-> int:
    if path.name.startswith("."):
        return 0
    elif path.is_file():
        if path.suffix != ".py":
            return 0
        with path.open() as source:
            return scanner(path)
    elif path.is_dir():
        count = sum(count_sloc(name, scanner) for name in path.iterdir())
        return count
    else:
        return 0
    
def main():
    base = Path.cwd().absolute()
    print("Hitung jumlah baris kode dari semua file di:\n", base)
    count = count_sloc(base, scan_python_1)
    print(
        f"{base.relative_to(base.parent)}: {count} baris kode"
    )
    
if __name__ == "__main__":
    main()
