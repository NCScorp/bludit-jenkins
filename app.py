import argparse

class App:
    parser = argparse.ArgumentParser("CLI para fazer posts no Bludit através do jenkins")
    parser.add_argument('-i', help="Job ID")
    parser.add_argument('-j', help="Job name")
    parser.add_argument('-v1', help="V1 flag")
    parser.add_argument('-jenkinsV2', help="Aplicacoes na v2")
    parser.add_argument('-b', help="Branch Name")
    parser.add_argument('-f', help="File Version")

    parser.add_argument('-p', nargs=2, help="Use proxy")

    args = parser.parse_args()

    if 