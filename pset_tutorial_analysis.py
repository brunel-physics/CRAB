import FWCore.ParameterSet.Config as cms

process = cms.Process('NoSplit')

#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/data/Run2017B/DoubleMuon/NANOAOD/UL2017_02Dec2019-v1/260000/2F46AECE-633C-E644-B5D1-C4305B53F36F.root'))

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/data/Run2017B/DoubleEG/NANOAOD/Nano14Dec2018-v1/10000/0C9C5536-0A0C-D649-A75C-3936F52B6DC2.root'))

#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch///store/mc/HC/GenericTTbar/GEN-SIM-RECO/CMSSW_9_0_0_90X_mcRun1_realistic_v4-v1/10000/00678018-A931-E711-B047-0CC47A4C8F30.root'))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("drop *", "keep recoTracks_*_*_*"),
    fileName = cms.untracked.string('output.root'),
)

process.out = cms.EndPath(process.output)
