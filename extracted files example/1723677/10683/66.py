# DEFINE NETWORK ARCHITECTURE GROUPINGS
# (1) GEOGRAPHICAL, (2) SOFTWARE/VIRUS, (3) HARDWARE, (4) NAME/MODEL
groups = [  ['CountryIdentifier','CityIdentifier','OrganizationIdentifier','GeoNameIdentifier',
             'LocaleEnglishNameIdentifier','Census_OSInstallLanguageIdentifier','Census_OSUILocaleIdentifier',
            'Wdft_RegionIdentifier'],
            ['DefaultBrowsersIdentifier', 'AVProductStatesIdentifier', 'AVProductsInstalled', 'AVProductsEnabled',
             'IsProtected', 'SMode', 'IeVerIdentifier', 'SmartScreen', 'Firewall','Census_IsSecureBootEnabled',
            'Census_IsWIMBootEnabled','Wdft_IsGamer','Census_OSWUAutoUpdateOptionsName','Census_GenuineStateName',
            'AppVersion2'],
            ['Processor','Census_MDC2FormFactor','Census_DeviceFamily','Census_ProcessorCoreCount','Census_ProcessorClass',
            'Census_PrimaryDiskTypeName','Census_HasOpticalDiskDrive','Census_TotalPhysicalRAM','Census_ChassisTypeName',
            'Census_InternalPrimaryDiagonalDisplaySizeInInches', 'Census_InternalPrimaryDisplayResolutionHorizontal',
            'Census_InternalPrimaryDisplayResolutionVertical', 'Census_PowerPlatformRoleName', 'Census_InternalBatteryType',
            'Census_InternalBatteryNumberOfCharges','Census_IsTouchEnabled','Census_IsPenCapable',
             'Census_IsAlwaysOnAlwaysConnectedCapable'],
            ['Census_OEMNameIdentifier', 'Census_OEMModelIdentifier', 'Census_ProcessorManufacturerIdentifier',
            'Census_ProcessorModelIdentifier','Census_FirmwareManufacturerIdentifier', 'Census_FirmwareVersionIdentifier']
         ]
