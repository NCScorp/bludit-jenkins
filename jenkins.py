import json
import requests
from instances import getInstance
from job import Job

from posts import Posts

class Jenkins:
    def __init__(self, jobName, jobId, useProxy, compilarV1, fileVersionPath, proxyHostName, proxyPort):
        self.__jobName = jobName
        self.__jobId = jobId
        self.__useProxy = useProxy
        self.__compilarV1 = compilarV1
        self.__fileVersionPath = fileVersionPath
        self.__proxyHostName = proxyHostName
        self.__proxyPort = proxyPort

    @property
    def baseUrl(self):
        return "ci.nasajon.com.br"

    def getEntity(self, uri):
        req = requests.get(uri)
        if self.__useProxy:
            proxy = {"http": f'http://{self.__proxyHostName}:{self.__proxyPort}'}
            req = requests.get(uri, proxies=proxy)
            
        return req.content

    def getLastFailures(self):
        success = False
        jobId = self.__jobId
        list = {}

        while not success:
            jobId -= 1
            uri = f"http://{self.baseUrl()}/job/{self.__jobName}/{jobId}/api/json"
            entity = self.getEntity(uri)

            if entity != None:
                jsonObj = json.dumps(entity)

                if not jsonObj["result"] == "SUCCESS":
                    list.add(jsonObj)
                else:
                    success = True

        return list

    def getUriJenkinsInfo(self):
        return f"http://{self.baseUrl()}/job/{self.__jobName}/{self.__jobId}/api/json"

    def getBluditPost(self):
        categories = []
        uri = self.getUriJenkinsInfo()
        entity = self.getEntity(uri)

        if entity != None:
            result = entity
            job = Job(categories=6, json=result, jobName="Instalador",failures=self.getLastFailures(), compilarV1=self.__compilarV1, fileVersionPath=self.__fileVersionPath)

            categories.append(job.categories)
            post = Posts(title=job.getTitle, content=job.getHtml, slug=job.getSlug, categories=categories)

        return post