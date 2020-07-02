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
#process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2021_realistic_v3', '') #2018ABC
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v20', '') #2018ABC
#process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v14', '') #2018D

#process.Tracer = cms.Service("Tracer")

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(30000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #'file:/data4/cmkuo/testfiles/DoubleMuon_Run2018C_17Sep2018.root'
        #'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/434/00000/966E12EA-BC93-E811-9D72-02163E00CDCE.root'
                                #'/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/434/00000/1858FF04-BD93-E811-A4C8-FA163E472C72.root'
        #'/store/data/Run2018D/EGamma/AOD/PromptReco-v2/000/325/170/00000/F7E3E79C-2C18-834D-86D5-C45D0F71996D.root'
                                #'/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v2/000/325/110/00000/884564F2-A9EA-3142-A453-00EDF40A6505.root'
                                #'/store/mc/Run3Summer19MiniAOD/DYToEE_M-50_NNPDF31_TuneCP5_14TeV-powheg-pythia8/MINIAODSIM/2023Scenario_106X_mcRun3_2023_realistic_v3-v2/260000/B6655B14-BB29-9C4F-B0F3-E9D2AD1CDD94.root'
                                #'/store/data/Run2017B/DoubleEG/MINIAOD/09Aug2019_UL2017-v1/50000/FDABBEEC-B587-8646-851A-ABC5D7996E1B.root'
                                #'/store/data/Run2017B/DoubleEG/MINIAOD/09Aug2019_UL2017-v1/50000/45CD943D-F9F7-F44B-B36F-E56670F4102E.root'
                                #'file:/tmp/shilpi/45CD943D-F9F7-F44B-B36F-E56670F4102E.root'  ###lxplus774
                                #'file:/tmp/shilpi/try.root' ### lxplus790
                                #'file:/tmp/shilpi/pickevents.root' ##lxplus785
                                #'file:/tmp/shilpi/pickevents_goodEle.root' ##lxplus738
                                #'file:/tmp/shilpi/pickevents_R9.root' ##lxplus738
                                #'file:/tmp/shilpi/pickevents_eta1p4442.root' ##lxplus738
                                #'file:out_new.root'
        #'file:/data4/cmkuo/testfiles/DoubleMuon_Run2018D_PR.root'
                            )#,
                            #lumisToProcess = cms.untracked.VLuminosityBlockRange('299329:1-299329:max'),
                            )


###https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGoodLumiSectionsJSONFile

process.inputs = cms.PSet (
    lumisToProcess = cms.untracked.VLuminosityBlockRange()
)


# get JSON file correctly parced
#import FWCore.PythonUtilities.LumiList as LumiList
#JSONfile = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
#myList = LumiList.LumiList (filename = JSONfile).getCMSSWString().split(',')

#process.inputs.lumisToProcess.extend(myList)

#process.load("PhysicsTools.PatAlgos.patSequences_cff")

process.load( "PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff" )
process.load( "PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff" )
process.load( "PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff" )

### fix a bug in the ECAL-Tracker momentum combination when applying the scale and smearing

from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
                       #runEnergyCorrections=False,
                       runEnergyCorrections=True,
                       runVID=True,
                       #era='2018-Prompt',
                       era='2017-UL',
                       eleIDModules=['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
                                     'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff'],
                       phoIDModules=['RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V2_cff',
                                     'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_94X_V2_cff']
                       )



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


#readEleRegresFromDBFile(process,suffex="2018ULV1")
#readPhoRegresFromDBFile(process,suffex="2018ULV1")

#readEleRegresFromDBFile(process,suffex="2018Run3Proj")

###taken from https://github.com/cms-egamma/SHarper-UserCode/blob/2018UL_SCElePho_V5a/SHNtupliser/python/regressionApplicationAOD_cff.py
#########################Modify the regression###########################


#process.load("ggAnalysis.ggNtuplizer.regressionApplication2023_cff")
###########################################################################

process.p = cms.Path(
#    process.fullPatMetSequenceModifiedMET *
    #process.regressionApplication * 
    process.egammaPostRecoSeq *
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


