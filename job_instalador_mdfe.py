from job import Job, URL_TYPE

class JobInstaladorMDFE(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)

    def getTitle(self):
        jsonObj = super().configJson

        return jsonObj["fullDisplayName"]

    def getVersion(self):
        jsonObj = super().configJson

        return jsonObj["displayName"]

    def getHtml(self):
        version = self.getVersion()
        
        content = "<div class=\"container-artefatos\">\n"
        content = content + "<h4>Links para cliente:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorMDFe(URL_TYPE.CLIENTE) + "\">nsjInstaladorMDFe.exe - " \
            + version + "<self./a></li>\n" + "</ul>\n"
        
        content = content + "<h4>Links para uso interno:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorMDFe(URL_TYPE.INTERNO).toString() \
            + "\">nsjInstaladorMDFe.exe - "+version+"<self./a></li>\n" \
            + "</ul>\n" + "</div>"

        return content

    def getSlug(self):
        return self.getVersion()