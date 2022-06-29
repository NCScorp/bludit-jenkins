import argparse
from bludit import Bludit
from jenkins import Jenkins
from jenkins_v2 import JenkinsV2
from posts import Posts

class App:
    parser = argparse.ArgumentParser("CLI para fazer posts no Bludit através do jenkins")
    parser.add_argument('-i', help="Job ID")
    parser.add_argument('-j', help="Job name")
    parser.add_argument('-v1', help="V1 flag")
    parser.add_argument('-jenkinsV2', help="Aplicacoes na v2")
    parser.add_argument('-b', help="Branch Name")
    parser.add_argument('-f', help="File Version")

    parser.add_argument('-p', nargs=2, help="Use proxy")
    
    try:
        args = parser.parse_args()
    except Exception as err:
        print(err)

    if args.j and args.i:
        jobname = args.j
        jobId = args.i
        useProxy = args.p

        hostname = ''
        port = 0

        if useProxy:
            proxyArgs = useProxy
            hostname = proxyArgs[0]
            port = proxyArgs[1]

        compilarv1 = False

        if args.v:
            compilarv1 = True

        if args.b:
            branchName = args.b

        if args.f:
            fileVersionPath = args.f

        bludit: Bludit = Bludit()

        if args.jenkinsV2:
            jenkins: Jenkins = JenkinsV2(jobName=jobname, jobId=jobId, 
                useProxy=useProxy, proxyHostName=hostname, proxyPort=port, fileVersionPath=fileVersionPath
            )
        else:
            jenkins: Jenkins = Jenkins(jobName=jobname, jobId=jobId, useProxy=useProxy, compilarV1=compilarv1)
        
        post: Posts = jenkins.getBluditPost()
        bludit.doPost(post)

    else:
        print("Não há argumentos")