from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'tutorial_May2015_Data_analysis'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pset_tutorial_analysis.py'

config.Data.inputDataset = '/DoubleEG/Run2017B-Nano14Dec2018-v1/NANOAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.runRange = '294927-306462' # '193093-194075'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_Run2017B_Data_analysis'

config.Site.storageSite = 'T2_UK_London_Brunel'
