import sys
from wordcount.cli import cli
from wordcount.gui import gui


def main():
    if len(sys.argv) > 1:
        cli()
    else:
        gui()

main()
