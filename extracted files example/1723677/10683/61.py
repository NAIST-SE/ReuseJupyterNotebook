# SET THIS VARIABLE TO TRUE TO RUN KERNEL QUICKLY
# AND TEST FOR BUGS. ONLY 10000 ROWS OF DATA IS LOADED
Debug = False

# IMPORT LIBRARIES
import pandas as pd, numpy as np, os, gc

# LOAD THESE BUT DONT ENCODE
MM = ['AvSigVersion','Census_OSVersion','Census_OSBuildRevision','AppVersion','EngineVersion']

# LOAD AND NUMERIC ENCODE
NE = ['Census_SystemVolumeTotalCapacity','Census_PrimaryDiskTotalCapacity']

# LOAD AND STATISTICAL ONE-HOT-ENCODE
OHE = [ 'RtpStateBitfield','DefaultBrowsersIdentifier', 'AVProductStatesIdentifier',
        'AVProductsInstalled', 'AVProductsEnabled', 'CountryIdentifier', 'CityIdentifier', 
        'GeoNameIdentifier', 'LocaleEnglishNameIdentifier', 'Processor', 'OsBuild', 'OsSuite',
        'SmartScreen','Census_MDC2FormFactor', 'Census_OEMNameIdentifier', 
        'Census_ProcessorCoreCount', 'Census_ProcessorModelIdentifier', 
        'Census_OSUILocaleIdentifier', 'Census_PrimaryDiskTypeName',
        'Census_HasOpticalDiskDrive', 'Census_TotalPhysicalRAM', 'Census_ChassisTypeName',
        'Census_InternalPrimaryDiagonalDisplaySizeInInches',
        'Census_InternalPrimaryDisplayResolutionHorizontal',
        'Census_InternalPrimaryDisplayResolutionVertical',
        'Census_PowerPlatformRoleName', 'Census_InternalBatteryType',
        'Census_InternalBatteryNumberOfCharges', 'Census_OSEdition', 'Census_GenuineStateName',
        'Census_ActivationChannel', 'Census_FirmwareManufacturerIdentifier', 'Census_IsTouchEnabled', 
        'Census_IsPenCapable', 'Census_IsAlwaysOnAlwaysConnectedCapable', 'Wdft_IsGamer', 
        'Wdft_RegionIdentifier', 'OsBuildLab', 'OrganizationIdentifier','Platform',
        'Census_OEMModelIdentifier', 'IsProtected', 'IeVerIdentifier','Firewall', 
        'Census_ProcessorManufacturerIdentifier','Census_OSInstallTypeName',
        'Census_OSWUAutoUpdateOptionsName','Census_IsFlightingInternal',
        'Census_FlightRing','Census_ThresholdOptIn','Census_FirmwareVersionIdentifier',
        'Census_IsSecureBootEnabled','Census_IsWIMBootEnabled']

# DONT LOAD THESE
XX = ['SMode','IsBeta', 'OsVer', 'OsPlatformSubRelease', 'SkuEdition', 'AutoSampleOptIn', 'PuaMode',
     'UacLuaenable', 'Census_ProcessorClass', 'Census_OSArchitecture', 'Census_OSBranch',
     'Census_OSBuildNumber', 'Census_OSSkuName', 'Census_OSInstallLanguageIdentifier',
     'Census_IsPortableOperatingSystem', 'Census_IsFlightsDisabled', 'Census_IsVirtualDevice',
     'IsSxsPassiveMode','ProductName','HasTpm','Census_DeviceFamily']

# DONT LOAD THIS
XXX = ['MachineIdentifier']

# LOAD ALL AS CATEGORIES
dtypes = {}
for x in OHE+NE+MM: dtypes[x] = 'category'
dtypes['HasDetections'] = 'int8'

# LOAD TRAIN CSV FILE
if Debug:
    df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv', usecols=dtypes.keys(), dtype=dtypes,nrows=10000)
else:
    df_train = pd.read_csv('../input/microsoft-malware-prediction/train.csv', usecols=dtypes.keys(), dtype=dtypes)
if 5244810 in df_train.index:
    df_train.loc[5244810,'AvSigVersion'] = '1.273.1144.0'
    df_train['AvSigVersion'].cat.remove_categories('1.2&#x17;3.1144.0',inplace=True)
print ('Loaded',len(df_train),'rows of TRAIN.CSV!')

# SHUFFLE TRAIN DATA
df_train = df_train.sample(frac=1)
df_train.reset_index(drop=True,inplace=True)

# LOAD TEST CSV FILE
if Debug:
    df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv', usecols=list(dtypes.keys())[0:-1], dtype=dtypes,nrows=10000)
else:
    df_test = pd.read_csv('../input/microsoft-malware-prediction/test.csv', usecols=list(dtypes.keys())[0:-1], dtype=dtypes)
print ('Loaded',len(df_test),'rows of TEST.CSV!')
