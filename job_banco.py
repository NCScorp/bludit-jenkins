from job import Job

class JobBanco(Job):
    def __init__(self, categories, json, jobName, failures, compilarV1, fileVersionPath):
        super().__init__(categories, json, jobName, failures, compilarV1, fileVersionPath)
    
    def getTitle():
        return "[BANCO] " + super().getTitle()
    
    def getVersion(self):
        self.__json = super().configJson()
        numBuild = self.__json["number"]
        
        return numBuild
    
    def getHtml(self):
        content = super().buildBody()
        content = content + "\n</div>"

        return content

    def getSlug(self):
        return self.getVersion()