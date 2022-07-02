import argparse
from config import AUTHENTICATION, TOKEN_API
from bludit import Bludit
import json
import requests
from datetime import datetime

parse = argparse.ArgumentParser(description="cli para pegar jenkinsv2 info")
parse.add_argument('-j', help="JobName")
parse.add_argument('-i', help="Job ID")
parse.add_argument('-b', help="Branch Name")

args = parse.parse_args()

res = json.loads(requests.get(f"http://v2.nasajon.com.br/job/{args.j}/job/{args.b}/{args.i}/api/json").text)

def getDate():
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y")
    return dt_string

def getDescription(desc) -> str:
    desc = desc.replace("nsj", "")
    desc = desc.replace(".exe", "")

    return desc.strip()

def getHTML():        
    teste = "nsjteste.exe"
    displayName = 'v2.2204.31.0'
    html = []
    
    html.append("<div class=\"flex\">")
    html.append("<div>")
    html.append("<h3 class=\"versoes\">Artefatos contidos no instalador:</h3>")            
    html.append("<div class=\"table-container\">")
    html.append("<table class=\"table-scroll\">")
    html.append("<thead>")
    html.append("<tr>")
    html.append("<th>Sistema</th>")
    html.append("<th>Versão</th>")
    html.append("<th>Data de lançamento</th>")
    html.append("</tr>")
    html.append("</thead>")
    html.append("<tbody>")

    html.append("<td>%s</td>" % getDescription(teste))
    html.append("<td>%s</td>" % displayName)
    html.append("<td>%s</td>" % getDate())
    html.append("<tr>")
    
    html.append("</tbody>")
    html.append("</table>")
    html.append("</div>")
    html.append("</div>")
    html.append("</div>")
    
    html.append("<div class=container-artefatos>")
    
    html.append("<h4>Links para cliente:</h4>")
    html.append("<ul class=container-artefatos-link>")        
    html.append("<li><a href=https://cdn.nasajon.com.br/instaladores/nsjInstaladorCliente_2.2204.31.0.exe>nsjInstaladorCliente_2.2204.31.0.exe</a></li>")
    html.append("<li><a href=https://cdn.nasajon.com.br/instaladores/nsjInstaladorV2_2.2204.31.0.exe>nsjInstaladorV2_2.2204.31.0.exe</a></li>")
    html.append("</ul>")
    
    html.append("<h4>Links para uso interno:</h4>")
    html.append("<ul class=container-artefatos-link>")
    html.append("<li><a href=https://167.114.1.112/instaladores/nsjInstaladorCliente_2.2204.31.0.exe>nsjInstaladorCliente_2.2204.31.0.exe</a></li>")
    html.append("<li><a href=https://cdn.nasajon.com.br/instaladores/nsjInstaladorV2_2.2204.31.0.exe>nsjInstaladorV2_2.2204.31.0.exe</a></li>")
    html.append("</ul>")                
    html.append("</div>")

    return '\n'.join(html)



post = Bludit(
    AUTHENTICATION, TOKEN_API, res["fullDisplayName"], getHTML(), res["displayName"], 
    "categoria-marota"
)

# print(post.doPost())

print(getHTML())
