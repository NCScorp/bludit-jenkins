from datetime import datetime
from file_version_line import FileVersionLine
from job import Job, URL_TYPE

class JobsInstaladorJenkinsV2(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)

    @property    
    def title(self):
        self.__json = super().configJson()    
        return self.__json["fullDisplayName"]

    @property
    def buildDateRelease(self):
        self.__json = super().configJson()
        timestamp = self.__json("timestamp")

        return datetime.strftime(timestamp, "%d/%m/%Y")

    @property
    def version(self):
        self.__json = super().configJson()
        version = self.__json["displayName"]

        if "master" in self.__json["fullDisplayName"]:
            version = version + "-master"
        
        return version

    #compare two fileversionpath case insensive
    def compare():
        o1 = FileVersionLine()
        o2 = FileVersionLine()
        
        return str(o1.nameExe).casefold() == str(o2.nameExe).casefold()

    @property
    def fileVersionContent(self):
        file: FileVersionLine = []
        
        if not self.getFileVersionPath():
            with open(self.fileVersionPath, 'r', encoding="ISO-8859-1") as fileLines:
                if fileLines:
                    for line in file:
                        if "Access violation" in line:
                            continue
                        
                        nameExe = line[0:line.index("-")].strip()
                        versionExe = line[line.index("-") + 1, len(line.strip)]                    
                        fileLine = FileVersionLine()
                        fileLine.nameExe = nameExe
                        fileLine.versionExe = versionExe
                        fileLine.dateRelease = self.buildDateRelease
                    
                    file.add(fileLine)                    
        
        return file

    def getHTML(self):        
        version = self.version
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
        
        file: FileVersionLine = self.fileVersionContent
        
        #using comparator
        file_sorted = sorted(file, cmp_to_key=self.compare())
        
        for line in file_sorted:
            if line.canShow():
                html.append("<tr>")                
            else:
                html.append("<tr class=\"invisible\">")                
            
            html.append(("<td>%s</td>" % (line.description)))
            html.append(("<td>%s</td>" % (line.versionExe)))
            html.append(("<td>%s</td>" % (line.dateRelease)))
            html.append("<tr>")
        
        html.append("</tbody>")
        html.append("</table>")
        html.append("</div>")
        html.append("</div>")
        html.append("</div>")
        
        html.append("<div class=\"container-artefatos\">")
        
        html.append("<h4>Links para cliente:</h4>")
        html.append("<ul class=\"container-artefatos-link\">")        
        html.append("<li><a href=\"" + self.getLinkInstaladorCliente(URL_TYPE.CLIENTE) + "\">nsjInstaladorCliente_" + version + ".exe</a></li>")
        html.append("<li><a href=\"" + self.getLinkInstaladorV2(URL_TYPE.CLIENTE) + "\">nsjInstaladorV2_" + version + ".exe</a></li>")
        html.append("</ul>")
        
        html.append("<h4>Links para uso interno:</h4>")
        html.append("<ul class=\"container-artefatos-link\">")
        html.append("<li><a href=\"" + self.getLinkInstaladorCliente(URL_TYPE.INTERNO) + "\">nsjInstaladorCliente_" + version + ".exe</a></li>")
        html.append("<li><a href=\"" + self.getLinkInstaladorV2(URL_TYPE.INTERNO) + "\">nsjInstaladorV2_" + version + ".exe</a></li>")
        html.append("</ul>")                
        html.append("</div>")

        return str(html)

    @property
    def slug(self):
        return self.version