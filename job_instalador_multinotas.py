from job import Job, URL_TYPE

class JobInstaladorMultinotas(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)

    def getTitle(self):
        jsonObj = super().configJson
        
        return jsonObj["fullDisplayName"]

    def getVersion():
        jsonObj = super().configJson

        return jsonObj["displayName"]

    def getHtml(self):
        version = self.getVersion()
        content = "<div class=\"container-artefatos\">\n"
        
        content = content + "<h4>Links para cliente:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorMultiNotas(URL_TYPE.CLIENTE) \
            + "\">InstaladorMultiNotas.exe - " + version + "</a></li>\n" + "</ul>\n"
        
        content = content + "<h4>Links para uso interno:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorMultiNotas(URL_TYPE.INTERNO) \
            + "\">InstaladorMultiNotas.exe - " + version \
            + "</a></li>\n" + "</ul>\n" + "</div>"

        return content

    def slug(self):
        return self.getVersion()