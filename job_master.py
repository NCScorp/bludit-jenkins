from job import Job, URL_TYPE

class JobMaster(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)

    def getTitle():
        return "[Master] " + super().getTitle()

    def getVersion(self):
        self.__json = super().configJson()
        numBuild = self.__json["number"]
        
        return numBuild
    

    def getHTML(self):
        content = super().buildBody()
        version = self.getVersion()
        content = content + "<div class=\"container-artefatos\">\n"

        content = content + "<h4>Links para cliente:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorAgente(URL_TYPE.CLIENTE) + "\">nsjInstaladorAgente.exe</a></li>\n" \
            + "<li><a href=\"" + self.getLinkInstaladorCliente(URL_TYPE.CLIENTE) \
            + "\">nsjInstaladorCliente_" + version + ".exe</a></li>\n" \
            + "<li><a href=\"" + self.getLinkInstaladorV2(URL_TYPE.CLIENTE) \
            + "\">nsjInstaladorV2_" + version + ".exe</a></li>\n"+ "</ul>\n";
        
        content = content + "<h4>Links para uso interno:</h4>";
        content = content + "<ul class=\"container-artefatos-link\">\n";
        content = content + "<li><a href=\"" + self.getLinkInstaladorAgente(URL_TYPE.INTERNO) \
            + "\">nsjInstaladorAgente.exe</a></li>\n" + "<li><a href=\"" \
            + self.getLinkInstaladorCliente(URL_TYPE.INTERNO) + "\">nsjInstaladorCliente_" \
            + version + ".exe</a></li>\n" + "<li><a href=\"" \
            + self.getLinkInstaladorV2(URL_TYPE.INTERNO) + "\">nsjInstaladorV2_" \
            + version + ".exe</a></li>\n" + "</ul>\n" + "</div>"

        return content
    

    def getSlug(self):
        return self.getVersion()
    
