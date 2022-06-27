class FileVersionLine:
    def __init__(self, nameExe, versionExe, dateRelease):
        self.nameExe = nameExe
        self.versionExe = versionExe
        self.dateRelease = dateRelease

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
        description = self.nameExe

        description = description.replace("nsj", "")
        description = description.replace(".exe", "")

        return description.strip()

    def canShow(self):
        if not self.nameExe in self.exceptionList:
            return self.exceptionList
    
    @property
    def nameExe(self):
        return self.nameExe

    @nameExe.setter
    def nameExe(self, nameExe):
        self.nameExe = nameExe

    @property
    def versionExe(self):
        return self.versionExe

    @versionExe.setter
    def versionExe(self, versionExe):
        self.versionExe = versionExe

    @property
    def dateRelease(self):
        return self.dateRelease

    @dateRelease.setter
    def dateRelease(self, dateRelease):
        self.dateRelease = dateRelease
    
    