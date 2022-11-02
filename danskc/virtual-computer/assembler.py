from assembler.parser import parse_lines
from assembler.symbols import find_symbols
from assembler.checker import check_lines
from assembler.generator import generate_lines


def assemble(text: str) -> str:
    lines = parse_lines(text)
    symbols = find_symbols(lines)
    lines = [line for line in lines if line.operation]
    check_lines(lines, symbols)
    return generate_lines(lines, symbols)

if __name__ == "__main__":
    from argparse import ArgumentParser
    argparser = ArgumentParser()
    argparser.add_argument("file")
    args = argparser.parse_args()
    with open(args.file) as file:
        # print(assemble(file.read()), end="", flush=True)
        print(assemble(file.read()))
    
