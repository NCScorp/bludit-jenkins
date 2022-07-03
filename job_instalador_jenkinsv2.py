from pathlib import Path
from instaladores import URL_TYPE, Instaladores
from file_version_line import FileVersionLine

class JobInstaladorJenkinsV2:
    def __init__(self, branch, file):
        self.__branch = branch
        self.__file = file

    def getHTML(self, res):
        instalador = Instaladores(self.__branch)
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

        with open(Path(self.__file), 'r') as file:
            arr = []
            for line in file:
                arr = line.replace('\n', '').split(' - ')
                fileVersionLine = FileVersionLine(arr[0])

                if fileVersionLine.canShow():
                    html.append("<tr>")
                else:
                    html.append("<tr class=\"invisible\">")

                html.append("<td>%s</td>" % fileVersionLine.description())
                html.append("<td>%s</td>" % arr[1])
                html.append("<td>%s</td>" % fileVersionLine.getDate())
                html.append("<tr>")
        
        html.append("</tbody>")
        html.append("</table>")
        html.append("</div>")
        html.append("</div>")
        html.append("</div>")
        
        html.append("<div class=container-artefatos>")
        
        html.append("<h4>Links para cliente:</h4>")
        html.append("<ul class=container-artefatos-link>")

        if self.__branch == "master":
            html.append("<li><a href=" + instalador.getLinkInstaladorCliente(URL_TYPE.CLIENTE, res) + ">nsjInstaladorCliente_" + res["displayName"] + "-master.exe</a></li>")
            html.append("<li><a href=" + instalador.getLinkInstaladorV2(URL_TYPE.CLIENTE, res) + ">nsjInstaladorV2_" + res["displayName"] + "-master.exe</a></li>")
            html.append("</ul>")
            
            html.append("<h4>Links para uso interno:</h4>")
            html.append("<ul class=container-artefatos-link>")
            html.append("<li><a href=" + instalador.getLinkInstaladorCliente(URL_TYPE.INTERNO, res) + ">nsjInstaladorCliente_" + res["displayName"] + "-master.exe</a></li>")
            html.append("<li><a href=" + instalador.getLinkInstaladorV2(URL_TYPE.INTERNO, res) + ">nsjInstaladorV2_" + res["displayName"] + "-master.exe</a></li>")
            html.append("</ul>")                
            html.append("</div>")

        else:
            html.append("<li><a href=" + instalador.getLinkInstaladorCliente(URL_TYPE.CLIENTE, res) + ">nsjInstaladorCliente_" + res["displayName"] + ".exe</a></li>")
            html.append("<li><a href=" + instalador.getLinkInstaladorV2(URL_TYPE.CLIENTE, res) + ">nsjInstaladorV2_" + res["displayName"] + ".exe</a></li>")
            html.append("</ul>")
            
            html.append("<h4>Links para uso interno:</h4>")
            html.append("<ul class=container-artefatos-link>")
            html.append("<li><a href=" + instalador.getLinkInstaladorCliente(URL_TYPE.INTERNO, res) + ">nsjInstaladorCliente_" + res["displayName"] + ".exe</a></li>")
            html.append("<li><a href=" + instalador.getLinkInstaladorV2(URL_TYPE.INTERNO, res) + ">nsjInstaladorV2_" + res["displayName"] + ".exe</a></li>")
            html.append("</ul>")                
            html.append("</div>")

        return '\n'.join(html)
