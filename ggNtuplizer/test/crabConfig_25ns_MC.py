if __name__ == '__main__':

# Usage : python crabConfig.py (to create jobs)
#         ./multicrab -c status -d <work area> (to check job status)

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    from CRABClient.UserUtilities import config
    config = config()
    
    from multiprocessing import Process

    # Common configuration

    config.General.workArea     = 'crab_projects_ntuples'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    #config.JobType.psetName     = 'run_mc_80X.py'

    #config.JobType.psetName     = 'run_data2023_102X.py'
#    config.JobType.inputFiles   = ['Summer16_23Sep2016V4_MC_L2Relative_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC_L3Absolute_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC.db']
    config.JobType.sendExternalFolder = True
    config.Data.inputDBS        = 'global'    
    #config.Data.splitting       = 'LumiBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.splitting       = 'FileBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.totalUnits      = -1
    config.Data.publication     = False
    config.Site.storageSite     = 'T2_CH_CERN'
    config.JobType.allowUndistributedCMSSW = True

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    # dataset dependent configuration

    config.JobType.psetName     = 'run_mc2017UL.py'
    config.General.requestName = 'mc'
    config.Data.unitsPerJob    = 10
    #config.Data.inputDataset   = '/DYToEE_M-50_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
    config.Data.inputDataset   = '/DYJetsToEE_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM'
#    config.Data.outLFNDirBase  = '/store/group/phys_egamma/SSvalidation/2017/'
#    config.Data.outLFNDirBase  = '/store/group/phys_egamma/SSvalidation/2017/V1'
    config.Data.outLFNDirBase  = '/store/group/phys_egamma/SSvalidation/2017/V2'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


