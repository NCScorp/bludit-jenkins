from enum import Enum

from config import CDN_NASAJON, STATIC_NASAJON


class URL_TYPE(Enum):
    CLIENTE = 1
    INTERNO = 2

class Instaladores:
    def __init__(self, branch):
        self.__branch = branch 

    def getLinkInstaladorAgente(a_tyUrl, res):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if CDN_NASAJON else STATIC_NASAJON}/instaladores/nsjInstaladorAgente.exe"


    def getLinkInstaladorCliente(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorCliente_" + res["displayName"] + "-master.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorCliente_" + res["displayName"] + ".exe"


    def getLinkInstaladorMDFe(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorMDFe_" + res["displayName"] + "-master.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorMDFe_" + res["displayName"] + ".exe"


    def getLinkInstalador(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstalador_" + res["displayName"] + "-master.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstalador_" + res["displayName"] + ".exe"


    def getLinkInstaladorV2(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorV2_" + res["displayName"] + "-master.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjInstaladorV2_" + res["displayName"] + ".exe"


    def getLinkInstaladorMultiNotas(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/InstaladorIntegradorMultinotas_" + res["displayName"] + "-master.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/InstaladorIntegradorMultinotas_" + res["displayName"] + ".exe"


    def getLinkConversor(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjConversor.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/nsjConversor.exe"


    def getLinkAbreLog(self, a_tyUrl, res):
        if self.__branch == "master":
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/AbreLog.exe"
        else:
            return f"https://{ CDN_NASAJON if a_tyUrl == URL_TYPE.CLIENTE else STATIC_NASAJON}/instaladores/AbreLog.exe"
