from config import AVULSOS, MASTER
from job_avulsos import JobAvulsos
from job_banco import JobBanco
from job_master import JobMaster
from job_instalador_jenkins_v2 import JobsInstaladorJenkinsV2
from job_instalador_multinotas import JobInstaladorMultinotas
from job_instalador_mdfe import JobInstaladorMDFE

def getInstance(jobName):
    job = None
    if jobName == "Integratto ERP Avulsos":
        job = JobAvulsos()
        job.jobName = AVULSOS
        job.categories = 3
    
    elif jobName == "ERP - Banco":
        job = JobBanco()
        job.categories = 5
    
    elif jobName == "ERP - Integratto":
        job = JobMaster()
        job.jobname = MASTER
        job.categories = 2

    elif jobName == "Instalador":
        job = JobsInstaladorJenkinsV2()
        job.categories = 6
    
    elif jobName == "MonitorMultinotas":
        job = JobInstaladorMultinotas()
        job.categories = 6

    elif jobName == "InstaladorMDFE":
        job = JobInstaladorMDFE()
        job.categories = 6

    return job
