class FileVersionLine:
    def __init__(self, nameExe, versionExe, dateRelease):
        self.__nameExe = nameExe
        self.__versionExe = versionExe
        self.__dateRelease = dateRelease

    exceptionList = [
        "nsjAssinatura.exe",
        #"nsjContabilizacao.exe",
        "nsjDIPJ.exe",
        #"nsjDIRF.exe",
        "nsjECF.exe",
        "nsjGetLauncher.exe",
        "nsjMonitorMigracao.exe",
        "nsjReinfNET.exe",
        "nsjScrittaImportador.exe",
        "nsjWs.exe",
        "ImpCNPJWeb.exe"
    ]

    @property
    def description(self):
        description = self.__nameExe

        description = description.replace("nsj", "")
        description = description.replace(".exe", "")

        return description.strip()

    def canShow(self):
        if not self.__nameExe in self.exceptionList:
            return self.exceptionList
    
    @property
    def nameExe(self):
        return self.__nameExe

    @nameExe.setter
    def nameExe(self, nameExe):
        self.__nameExe = nameExe

    @property
    def versionExe(self):
        return self.__versionExe

    @versionExe.setter
    def versionExe(self, versionExe):
        self.__versionExe = versionExe

    @property
    def dateRelease(self):
        return self.__dateRelease

    @dateRelease.setter
    def dateRelease(self, dateRelease):
        self.__dateRelease = dateRelease
    
    