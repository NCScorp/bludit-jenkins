from jenkins import Jenkins

class JenkinsV2(Jenkins):
    def __init__(self, jobName, jobId, useProxy, fileVersionPath, proxyHostName, proxyPort, branchName):
        super().__init__(jobName, jobId, useProxy, fileVersionPath, proxyHostName, proxyPort)
        self.__branchName = branchName
        self.__fileVersionPath = fileVersionPath

    def getBaseUrl(self):
        return "//v2.nasajon.com.br"
    
    def getLastFailures(self):
        return []

    def getUriJenkinsInfo(self):
        url = f"http://{self.getBaseUrl}/job/{self.__jobName}/job/{self.__branchName}/{self.__jobId}/api/json"

        return url