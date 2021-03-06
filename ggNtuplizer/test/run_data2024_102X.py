import FWCore.ParameterSet.Config as cms

process = cms.Process('ggKit')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load("Configuration.Geometry.GeometryIdeal_cff" )
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff" )
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_v11', '') #2018ABC
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2024_realistic_v4', '') #2018ABC
#process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v14', '') #2018D

#process.Tracer = cms.Service("Tracer")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #'file:/data4/cmkuo/testfiles/DoubleMuon_Run2018C_17Sep2018.root'
        #'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/434/00000/966E12EA-BC93-E811-9D72-02163E00CDCE.root'
        #'/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/434/00000/1858FF04-BD93-E811-A4C8-FA163E472C72.root'
        #'/store/data/Run2018D/EGamma/AOD/PromptReco-v2/000/325/170/00000/F7E3E79C-2C18-834D-86D5-C45D0F71996D.root'
                                #'/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v2/000/325/110/00000/884564F2-A9EA-3142-A453-00EDF40A6505.root'
                                #'/store/mc/Run3Summer19MiniAOD/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/260000/B6655B14-BB29-9C4F-B0F3-E9D2AD1CDD94.root'
                                #'/store/mc/Run3Summer19MiniAOD/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/260000/030B8332-39C6-0E40-9EEC-7FE7D5FC355A.root'
                                #'/store/mc/Run3Summer19MiniAOD/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/260000/C788ED59-A299-8940-8BC2-A95D3F1738ED.root'
                                '/store/mc/Run3Summer19MiniAOD/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/2024Scenario_106X_mcRun3_2024_realistic_v4-v2/260000/96D141D3-72DD-F34B-BEBF-175CF2B11BEA.root'
        #'file:out.root'
        #'file:out_new.root'
        #'file:/data4/cmkuo/testfiles/DoubleMuon_Run2018D_PR.root'
        )
                            )

#process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.load( "PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff" )
process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
process.load( "PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff" )

### fix a bug in the ECAL-Tracker momentum combination when applying the scale and smearing
'''
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       runEnergyCorrections=False,
                       runVID=True,
                       era='2018-Prompt',
                       eleIDModules=['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff'],
                       phoIDModules=['RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V2_cff',
                                     'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_94X_V2_cff']
                       )
'''


#from PhysicsTools.PatAlgos.tools.cmsswVersionTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *
#runOnData( process,  names=['Photons', 'Electrons','Muons','Taus','Jets'], outputModules = [] )
#runOnData( process, outputModules = [] )
#removeMCMatching(process, names=['All'], outputModules=[])

process.TFileService = cms.Service("TFileService", fileName = cms.string('ggtree_data.root'))

### update JEC
'''
process.load("PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff")
process.jetCorrFactors = process.updatedPatJetCorrFactors.clone(
    src = cms.InputTag("slimmedJets"),
    levels = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'],
    payload = 'AK4PFchs') 

process.slimmedJetsJEC = process.updatedPatJets.clone(
    jetSource = cms.InputTag("slimmedJets"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("jetCorrFactors"))
    )
'''

'''
### reduce effect of high eta EE noise on the PF MET measurement
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD (
        process,
        isData = True, # false for MC
        fixEE2017 = True,
        fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} ,
        postfix = "ModifiedMET"
)
'''

process.load("ggAnalysis.ggNtuplizer.ggNtuplizer_miniAOD_cfi")
process.ggNtuplizer.year=cms.int32(2017)
process.ggNtuplizer.doGenParticles=cms.bool(True)
#process.ggNtuplizer.dumpPFPhotons=cms.bool(True)
process.ggNtuplizer.dumpPFPhotons=cms.bool(False)
process.ggNtuplizer.dumpHFElectrons=cms.bool(False)
process.ggNtuplizer.dumpJets=cms.bool(False)
process.ggNtuplizer.dumpAK8Jets=cms.bool(False)
process.ggNtuplizer.dumpSoftDrop= cms.bool(False)
process.ggNtuplizer.dumpTaus=cms.bool(False)
process.ggNtuplizer.ak4JetSrc=cms.InputTag("slimmedJetsJEC")
process.ggNtuplizer.pfMETLabel=cms.InputTag("slimmedMETsModifiedMET")
process.ggNtuplizer.addFilterInfoMINIAOD=cms.bool(True)
process.ggNtuplizer.electronSrc = cms.InputTag("slimmedElectrons","","ggKit")
process.ggNtuplizer.calibelectronSrc = cms.InputTag("slimmedElectrons","","ggKit")
process.ggNtuplizer.photonSrc = cms.InputTag("slimmedPhotons","","ggKit")
process.ggNtuplizer.calibphotonSrc = cms.InputTag("slimmedPhotons","","ggKit")

process.load("ggAnalysis.ggNtuplizer.ggMETFilters_cff")

process.cleanedMu = cms.EDProducer("PATMuonCleanerBySegments",
                                   src = cms.InputTag("slimmedMuons"),
                                   preselection = cms.string("track.isNonnull"),
                                   passthrough = cms.string("isGlobalMuon && numberOfMatches >= 2"),
                                   fractionOfSharedSegments = cms.double(0.499))




###taken from https://github.com/cms-egamma/SHarper-UserCode/blob/2018UL_SCElePho_V5a/TrigNtup/test/egRegTreeMakerRefinedAODNewReg.py
def readEleRegresFromDBFile(process,filename=None,suffex="2017UL",prod=False):
    print "reading in ele regression with tag {} from prod {}".format(suffex,prod)
    from CondCore.CondDB.CondDB_cfi import CondDB
    if filename:
        CondDBReg = CondDB.clone(connect = 'sqlite_file:{}'.format(filename))
    elif prod:
        CondDBReg = CondDB.clone(connect = 'frontier://FrontierProd/CMS_CONDITIONS')
    else:
        CondDBReg = CondDB.clone(connect = 'frontier://FrontierPrep/CMS_CONDITIONS')
    
    process.eleRegres = cms.ESSource("PoolDBESSource",CondDBReg,
                                     DumpStat=cms.untracked.bool(False),
                                     toGet = cms.VPSet(
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_eb_ecalOnly_1To300_0p2To2_mean"),
         tag = cms.string("electron_eb_ecalOnly_1To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_ee_ecalOnly_1To300_0p2To2_mean"),
         tag = cms.string("electron_ee_ecalOnly_1To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_eb_ecalOnly_1To300_0p0002To0p5_sigma"),
         tag = cms.string("electron_eb_ecalOnly_1To300_0p0002To0p5_sigma_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_ee_ecalOnly_1To300_0p0002To0p5_sigma"),
         tag = cms.string("electron_ee_ecalOnly_1To300_0p0002To0p5_sigma_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_eb_ecalTrk_1To300_0p2To2_mean"),
         tag = cms.string("electron_eb_ecalTrk_1To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_ee_ecalTrk_1To300_0p2To2_mean"),
         tag = cms.string("electron_ee_ecalTrk_1To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_eb_ecalTrk_1To300_0p0002To0p5_sigma"),
         tag = cms.string("electron_eb_ecalTrk_1To300_0p0002To0p5_sigma_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("electron_ee_ecalTrk_1To300_0p0002To0p5_sigma"),
         tag = cms.string("electron_ee_ecalTrk_1To300_0p0002To0p5_sigma_{}".format(suffex))),
                                     )
    )
    
    process.es_prefer_eleRegres = cms.ESPrefer("PoolDBESSource","eleRegres")
    return process


def readPhoRegresFromDBFile(process,filename=None,suffex="2017UL",prod=False):
    print "reading in pho regression with tag {} from prod {}".format(suffex,prod)
    from CondCore.CondDB.CondDB_cfi import CondDB
    if filename:
        CondDBReg = CondDB.clone(connect = 'sqlite_file:{}'.format(filename))
    elif prod:
        CondDBReg = CondDB.clone(connect = 'frontier://FrontierProd/CMS_CONDITIONS')
    else:
        CondDBReg = CondDB.clone(connect = 'frontier://FrontierPrep/CMS_CONDITIONS')
    process.phoRegres = cms.ESSource("PoolDBESSource",CondDBReg,
                                     DumpStat=cms.untracked.bool(False),
                                     toGet = cms.VPSet(
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("photon_eb_ecalOnly_5To300_0p2To2_mean"),
         tag = cms.string("photon_eb_ecalOnly_5To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("photon_ee_ecalOnly_5To300_0p2To2_mean"),
         tag = cms.string("photon_ee_ecalOnly_5To300_0p2To2_mean_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("photon_eb_ecalOnly_5To300_0p0002To0p5_sigma"),
         tag = cms.string("photon_eb_ecalOnly_5To300_0p0002To0p5_sigma_{}".format(suffex))),
cms.PSet(record = cms.string("GBRDWrapperRcd"),
         label = cms.untracked.string("photon_ee_ecalOnly_5To300_0p0002To0p5_sigma"),
         tag = cms.string("photon_ee_ecalOnly_5To300_0p0002To0p5_sigma_{}".format(suffex))),
                                     )
                                 )
    process.es_prefer_phoRegres = cms.ESPrefer("PoolDBESSource","phoRegres")
    return process


#readEleRegresFromDBFile(process,suffex="2023")
#readPhoRegresFromDBFile(process,suffex="2023")


readEleRegresFromDBFile(process,suffex="2023Run3ProjV1")

###taken from https://github.com/cms-egamma/SHarper-UserCode/blob/2018UL_SCElePho_V5a/SHNtupliser/python/regressionApplicationAOD_cff.py
#########################Modify the regression###########################
'''
from RecoEgamma.EgammaTools.regressionModifier_cfi import regressionModifier

gedGsfElectrons = cms.EDProducer("ModifiedGsfElectronProducer",
    src = cms.InputTag("gedGsfElectrons",processName=cms.InputTag.skipCurrentProcess()),
    modifierConfig = cms.PSet( modifications = cms.VPSet() )
)
 
gedPhotons = cms.EDProducer("ModifiedRecoPhotonProducer",
    src = cms.InputTag("gedPhotons",processName=cms.InputTag.skipCurrentProcess()),
    modifierConfig = cms.PSet( modifications = cms.VPSet() )
)    

egamma_modifications = cms.VPSet( )
egamma_modifications.append( regressionModifier )

gedGsfElectrons.modifierConfig.modifications = egamma_modifications
gedPhotons.modifierConfig.modifications   = egamma_modifications

regressionApplication = cms.Sequence( gedGsfElectrons * gedPhotons )
'''


process.load("ggAnalysis.ggNtuplizer.regressionApplication2023_cff")
###########################################################################

process.p = cms.Path(
#    process.fullPatMetSequenceModifiedMET *
    process.regressionApplication * 
    #process.egammaPostRecoSeq *
    process.cleanedMu *
    process.ggMETFiltersSequence *
    #process.jetCorrFactors *
    #process.slimmedJetsJEC *
    
    process.ggNtuplizer
    )


#process.p = cms.Path(process.regressionApplication)

#print process.dumpPython()
'''
process.out = cms.OutputModule("PoolOutputModule",
                               compressionAlgorithm = cms.untracked.string('LZMA'),
                               compressionLevel = cms.untracked.int32(4),
                               #dataset = cms.untracked.PSet(
                               #dataTier = cms.untracked.string('AODSIM'),
                               #filterName = cms.untracked.string('')
                               #),
                               eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
                               fileName = cms.untracked.string("out.root"),
                               #SelectEvents = cms.untracked.PSet(
                               #               SelectEvents = cms.vstring("p") 
                               #               )
                               )      


process.e = cms.EndPath(process.out)    
'''


