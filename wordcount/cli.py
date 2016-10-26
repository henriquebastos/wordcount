import argparse

from wordcount.cmd import top_words, count_words, read_words


def cli():
    parser = argparse.ArgumentParser(prog='wordcount', description='Count all the words!')
    parser.add_argument('-t', '--topcount', dest='command',
                        action='store_const', const=top_words, default=count_words,
                        help='Show most frequent words.')
    parser.add_argument('textfile', type=argparse.FileType(), help='Text file to be counted.')

    option = parser.parse_args()

    print(option.command(read_words(option.textfile)))
