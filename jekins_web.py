import json
import requests
from job import Job

from posts import Posts

class JenkinsWeb:
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
            config = requests.get(uri, proxies=proxy)
        
        return config.content

    def getLastFailures(self):
        success = False
        jobId = self.__jobId
        list = {}

        while not success:
            jobId -= 1
            uri = f"http://{self.baseUrl}/job/{self.__jobName}/{jobId}/api/json"
            entity = self.getEntity(uri)

            if entity != None:
                jsonObj = json.dumps(entity)

                if not jsonObj["result"] == "SUCCESS":
                    list.add(jsonObj)
                else:
                    success = True

        return list

    def getUriJenkinsInfo(self):
        return f"http://{self.baseUrl}/job/{self.__jobName}/{self.__jobId}/api/json"

    def getBluditPost(self):
        post = Posts()
        categories = {}
        uri = self.getUriJenkinsInfo
        entity = self.getEntity(uri)

        if entity != None:
            result = json.dumps(entity)
            job: Job = Job().getInstance(self.__jobName)
            job.configJson = result
            job.failures = self.getLastFailures
            job.compilarV1 = self.__compilarV1
            job.fileVersionPath = self.__fileVersionPath

            categories.add(job.categories)

            post.title = job.getTitle
            post.content = job.getHtml
            post.categories = categories
            post.slug = job.getSlug

        return post