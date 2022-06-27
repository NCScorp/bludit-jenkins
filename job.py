from enum import Enum
import json


class URL_TYPE(Enum):
    INTERNO = 1
    CLIENTE = 2

class Job():
    AVULSOS = "Integratto+ERP+Avulsos"
    MASTER = "ERP+-+Integratto"
    CDN_NASAJON = "cdn.nasajon.com.br"
    CDN_NASAJON_PATH = "instaladores"
    STATIC_NASAJON = "167.114.1.112"

    def getVersion():
        pass

    def getSlug():
        pass

    def getLinkInstaladorAgent(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjInstaladorAgente.exe"
    
    def getLinkInstaladorCliente(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjInstaladorCliente_" + self.getVersion() + ".exe"
	
    def getLinkInstaladorMDFe(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjInstaladorMDFe_" + self.getVersion() + ".exe"

    def getLinkInstalador(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjInstalador_" + self.getVersion() + ".exe"

    def getLinkInstaladorV2(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjInstaladorV2_" + self.getVersion() + ".exe"
        
    def getLinkInstaladorMultiNotas(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/InstaladorIntegradorMultinotas_" + self.getVersion() + ".exe"

    def getLinkConversor(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/nsjConversor.exe"

    def getLinkAbreLog(self, a_tyUrl: URL_TYPE):
        return f"https://{a_tyUrl == URL_TYPE.CLIENTE if self.CDN_NASAJON else self.STATIC_NASAJON}/instaladores/AbreLog.exe"

    