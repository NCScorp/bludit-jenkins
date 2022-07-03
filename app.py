import requests
import argparse
import json
from bludit import Bludit
from config import AUTHENTICATION, TOKEN_API
from job_instalador_jenkinsv2 import JobInstaladorJenkinsV2

parse = argparse.ArgumentParser(description="cli para pegar jenkinsv2 info")
parse.add_argument('-j', help="JobName")
parse.add_argument('-i', help="Job ID")
parse.add_argument('-b', help="Branch Name")
parse.add_argument('-f', help="File version")

args = parse.parse_args()

res = json.loads(requests.get(f"http://v2.nasajon.com.br/job/{args.j}/job/{args.b}/{args.i}/api/json").text)

jobInstaladorJenkinsV2 = JobInstaladorJenkinsV2(args.b, args.f)

post = Bludit(
    AUTHENTICATION, TOKEN_API, res["fullDisplayName"], jobInstaladorJenkinsV2.getHTML(res), res["displayName"], 
    "categoria-marota"
)

print(post.doPost())

print(jobInstaladorJenkinsV2.getHTML(res))

