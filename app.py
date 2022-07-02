import argparse
from bludit import Bludit
from jenkins_v2 import JenkinsV2

class App:
    parser = argparse.ArgumentParser("CLI para fazer posts no Bludit através do jenkins")
    parser.add_argument('-i', help="Job ID")
    parser.add_argument('-j', help="Job name")
    parser.add_argument('-v1', help="V1 flag")
    parser.add_argument('-jenkinsV2', help="Aplicacoes na v2", action='store_true')
    parser.add_argument('-b', help="Branch Name")
    parser.add_argument('-f', help="File Version")

    parser.add_argument('-p', nargs=2, help="Use proxy")
    
    try:
        args = parser.parse_args()
    except Exception as err:
        print(err)

    if args.i and args.j:
        jobName = args.j
        jobId = args.i

        branchName = ''
        if branchName:
            branchName = args.b

        filePathVersion = ''
        if args.f:
            filePathVersion = args.f
            

    else:
        print("Não há argumentos")