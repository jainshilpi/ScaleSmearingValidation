import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaTools.regressionModifier_cfi import regressionModifier106XULOnlyEle
#from RecoEgamma.EgammaTools.regressionModifier_cfi import regressionModifier

#slimmedElectrons = cms.EDProducer("ModifiedGsfElectronProducer",
slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
                                  src = cms.InputTag("slimmedElectrons",processName=cms.InputTag.skipCurrentProcess()),
                                  #src = cms.InputTag("slimmedElectrons"),
    modifierConfig = cms.PSet( modifications = cms.VPSet() )
)
 
'''
#slimmedPhotons = cms.EDProducer("ModifiedRecoPhotonProducer",
slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
                                src = cms.InputTag("slimmedPhotons",processName=cms.InputTag.skipCurrentProcess()),
                                #src = cms.InputTag("slimmedPhotons"),
    modifierConfig = cms.PSet( modifications = cms.VPSet() )
)    
'''

egamma_modifications = cms.VPSet( )
egamma_modifications.append( regressionModifier106XULOnlyEle )
#egamma_modifications.append( regressionModifier )

slimmedElectrons.modifierConfig.modifications = egamma_modifications
#slimmedPhotons.modifierConfig.modifications   = egamma_modifications

egammaEnRegTask = cms.Task()

egammaEnRegTask.add(slimmedElectrons) 
#egammaEnRegTask.add(slimmedPhotons)

regressionApplication = cms.Sequence(egammaEnRegTask)

#regressionApplication = cms.Sequence( slimmedElectrons * slimmedPhotons )
