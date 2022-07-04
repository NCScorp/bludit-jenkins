from datetime import datetime

class FileVersionLine:
    def __init__(self, nameExe):
        self.__nameExe = nameExe

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
        "ImpCNPJWeb.exe",
    ]
    
    def canShow(self):
        if not self.__nameExe in self.exceptionList:
           return True
        else:
            pass

    def description(self):
        desc = self.__nameExe

        desc = desc.replace('nsj', '')
        desc = desc.replace('.exe', '')

        return desc.strip()

    def getDate(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y")
        
        return dt_string
