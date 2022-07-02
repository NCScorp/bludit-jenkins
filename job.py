from enum import Enum
from datetime import datetime
from config import CDN_NASAJON, STATIC_NASAJON

class URL_TYPE(Enum):
    INTERNO = 1
    CLIENTE = 2

class Job:
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        self.__categories = categories
        self.__json = json
        self.__jobName = jobName
        self.__failures = failures
        self.__compilarV1 = compilarV1
        self.__fileVersionPath = fileVersionPath
    
    def getVersion(self):
        pass

    def getSlug(self):
        pass

    def getHtml(self):
        pass
    
    def getLinkInstaladorAgent(self, a_tyUrl):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstaladorAgente.exe"
    
    def getLinkInstaladorCliente(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstaladorCliente_" + self.getVersion() + ".exe"
	
    def getLinkInstaladorMDFe(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstaladorMDFe_" + self.getVersion() + ".exe"

    def getLinkInstalador(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstalador_" + self.getVersion() + ".exe"

    def getLinkInstaladorV2(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstaladorV2_" + self.getVersion() + ".exe"
        
    def getLinkInstaladorMultiNotas(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/InstaladorIntegradorMultinotas_" + self.getVersion() + ".exe"

    def getLinkConversor(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjConversor.exe"

    def getLinkAbreLog(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/AbreLog.exe"

    def hasChanges(self):
        changeSet = self.__json['changeSet']
        items = changeSet['items']

        hasContentChanges = len(items) > 0

        if not hasContentChanges:
            for jObject in self.__failure:
                changeSet = jObject['changeSet']
                items = changeSet['items']
                hasContentChanges = len(items) > 0
                
                if hasContentChanges:
                    break
        
        return hasContentChanges
    
    def getChangeList(self):
        changeSet = self.__json['changeSet']
        items = changeSet['items']

        for i in items:
            comment = items[i]['comment']
            author = items[i]['author']['fullname']
            content = content + "<li>" + comment[0:comment.index('\n')] + " - <span class=\"commit-author\">" + author + "</span></li>\n"
        
        return content

    def buildBody(self):
        content = "<div class=\"container-mudandas\">\n"

        if self.hasChanges():
            content = content + "<h2>Mudanças</h2>\n<ol>\n"
            content = content + self.getChangeList(self.__json)
            
            for jObject in self.__failures:
                content = content + self.getChangeList(jObject)
            
            content = content + "</ol>\n" 
        
        return content

    @property
    def getJobId(self):
        numeroId = self.__json['number']
        
        return numeroId
    
    @property
    def getDate(self):
        timestamp = self.__json['timestamp']
        stamp = str(timestamp)
        date = datetime.strftime(stamp, "%d/%m/%Y %H:%M:%S")

        return date
    
    @property
    def getTitle(self):
        return "Integratto ERP " + self.getVersion + " (" + self.getDate + ")"

    @property
    def configJson(self):
        return self.__json

    @configJson.setter
    def configJson(self, json):
        self.__json = json
    
    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, categories):
        self.__categories = categories
    
    @property
    def jobName(self):
        return self.__jobName

    @jobName.setter
    def jobName(self, jobName):
        self.__jobName = jobName
    
    @property
    def failures(self):
        return self.__failures

    @failures.setter
    def failures(self, failures):
        self.__failures = failures

    @property
    def compilarV1(self):
        return self.__compilarV1

    @compilarV1.setter
    def compilarV1(self, compilarV1):
        self.__compilarV1 = compilarV1

    @property
    def fileVersionPath(self):
        return self.__fileVersionPath

    @fileVersionPath.setter
    def fileVersionPath(self, fileVersionPath):
        self.__fileVersionPath = fileVersionPath
