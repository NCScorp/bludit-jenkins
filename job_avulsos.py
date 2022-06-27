from job import Job, URL_TYPE

class JobAvulsos(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)

    def getTitle():
        return "[Avulsos] " + super().getTitle()
    
    def getVersion(self):
        self.__json = super().configJson()
        parameters = self.__json['actions'][0]['parameters']
        
        for i in len(parameters):
            if parameters[i]['name'] == "NUMEROBUILDEXE":
                numBuild = parameters[i]['value']

            if parameters[i]['name'] == "NUMEROREVISAOEXE":
                numVersao = parameters[i]['value']
            
        return numBuild + "." + numVersao

    def getHtml(self):
        content = self.buildBody()
        version = self.getVersion()

        content = content + "<div class=\"container-artefatos\">\n"

        content = content + "<h4>Links para cliente:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" + \
            self.getLinkInstaladorAgente(URL_TYPE.CLIENTE) + "\">nsjInstaladorAgente.exe</a></li>\n" \
            + "<li><a href=\"" + self.getLinkInstaladorCliente(URL_TYPE.CLIENTE) + "\">nsjInstaladorCliente_" \
            + version + ".exe</a></li>\n" \
            + "<li><a href=\"" + self.getLinkInstaladorMDFe(URL_TYPE.CLIENTE) + "\">nsjInstaladorMDFe_" \
            + version + ".exe</a></li>\n"
        
        if self.compilarV1():
            content = content + "<li><a href=\"" + self.getLinkInstalador(URL_TYPE.CLIENTE) \
                + "\">nsjInstalador_" + version + ".exe</a></li>\n"
        
        content = content + "<li><a href=\"" + self.getLinkInstaladorV2(URL_TYPE.CLIENTE) \
            + "\">nsjInstaladorV2_" + version + ".exe</a></li>\n" + "</ul>\n"
        
        content = content + "<h4>Links para uso interno:</h4>"
        content = content + "<ul class=\"container-artefatos-link\">\n"
        content = content + "<li><a href=\"" \
            + self.getLinkInstaladorAgente(URL_TYPE.INTERNO) + "\">nsjInstaladorAgente.exe</a></li>\n" \
            + "<li><a href=\"" + self.getLinkInstaladorCliente(URL_TYPE.INTERNO) + "\">nsjInstaladorCliente_" \
            + version + ".exe</a></li>\n" + "<li><a href=\"" + self.getLinkInstaladorMDFe(URL_TYPE.INTERNO) \
            + "\">nsjInstaladorMDFe_" + version + ".exe</a></li>\n"
        
        if self.compilarV1():
            content = content + "<li><a href=\"" + self.getLinkInstalador(URL_TYPE.INTERNO) \
                + "\">nsjInstalador_" + version + ".exe</a></li>\n"            
        
        
        content = content + "<li><a href=\"" + self.getLinkInstaladorV2(URL_TYPE.INTERNO) \
            + "\">nsjInstaladorV2_" + version + ".exe</a></li>\n" + "</ul>\n" + "</div>"

        return content
    
    @property
    def slug(self):
        json = super().configJson()
        parameters = []
        numBuild = ""
        numVersion = ""
        parameters = json["actions"][0]["parameters"]

        for i in parameters:
            if parameters[i]["name"] == "NUMEROBUILDEXE":
                numBuild = parameters[i]["value"]

        if parameters[i]["name"] == "NUMEROREVISAOEXE":
            numVersion = parameters[i]["value"]

        return numBuild + "-" + numVersion
    