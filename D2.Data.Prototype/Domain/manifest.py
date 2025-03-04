from enum import Enum


class Localization(Enum):
	EN = 'en'
	FR = 'fr'
	ES = 'es'
	ES_MX = 'es-mx'
	DE = 'de'
	IT = 'it'
	JA = 'ja'
	PT_BR = 'pt-br'
	RU = 'ru'
	PL = 'pl'
	KO = 'ko'
	ZH_CHT = 'zh-cht'
	ZH_CHS = 'zh-chs'


class MobileWorldContentPaths:

	def __init__(
			self, en: str,
			fr: str,
			es: str,
			es_mx: str,
			de: str,
			it: str,
			ja: str,
			pt_br: str,
			ru: str,
			pl: str,
			ko: str,
			zh_cht: str,
			zh_chs: str
			):
		self.en = en
		self.fr = fr
		self.es = es
		self.es_mx = es_mx
		self.de = de
		self.it = it
		self.ja = ja
		self.pt_br = pt_br
		self.ru = ru
		self.pl = pl
		self.ko = ko
		self.zh_cht = zh_cht
		self.zh_chs = zh_chs

class JsonWorldComponentContentPathsTable:

	def __init__(
			self,
			destinyArtDyeChannelDefinition: str,
			destinyArtDyeReferenceDefinition: str,
			destinyPlaceDefinition: str,
			destinyActivityDefinition: str,
			destinyActivityTypeDefinition: str,
			destinyClassDefinition: str,
			destinyGenderDefinition: str,
			destinyInventoryBucketDefinition: str,
			destinyRaceDefinition: str,
			destinyUnlockDefinition: str,
			destinyStatGroupDefinition: str,
			destinyProgressionMappingDefinition: str,
			destinyFactionDefinition: str,
			destinyVendorGroupDefinition: str,
			destinyRewardSourceDefinition: str,
			destinyUnlockValueDefinition: str,
			destinyRewardMappingDefinition: str,
			destinyRewardSheetDefinition: str,
			destinyItemCategoryDefinition: str,
			destinyDamageTypeDefinition: str,
			destinyActivityModeDefinition: str,
			destinyMedalTierDefinition: str,
			destinyAchievementDefinition: str,
			destinyActivityGraphDefinition: str,
			destinyActivityInteractableDefinition: str,
			destinyBondDefinition: str,
			destinyCharacterCustomizationCategoryDefinition: str,
			destinyCharacterCustomizationOptionDefinition: str,
			destinyCollectibleDefinition: str,
			destinyDestinationDefinition: str,
			destinyEntitlementOfferDefinition: str,
			destinyEquipmentSlotDefinition: str,
			destinyEventCardDefinition: str,
			destinyFireteamFinderActivityGraphDefinition: str,
			destinyFireteamFinderActivitySetDefinition: str,
			destinyFireteamFinderLabelDefinition: str,
			destinyFireteamFinderLabelGroupDefinition: str,
			destinyFireteamFinderOptionDefinition: str,
			destinyFireteamFinderOptionGroupDefinition: str,
			destinyStatDefinition: str,
			destinyInventoryItemDefinition: str,
			destinyInventoryItemLiteDefinition: str,
			destinyItemTierTypeDefinition: str,
			destinyLoadoutColorDefinition: str,
			destinyLoadoutIconDefinition: str,
			destinyLoadoutNameDefinition: str,
			destinyLocationDefinition: str,
			destinyLoreDefinition: str,
			destinyMaterialRequirementSetDefinition: str,
			destinyMetricDefinition: str,
			destinyObjectiveDefinition: str,
			destinySandboxPerkDefinition: str,
			destinyPlatformBucketMappingDefinition: str,
			destinyPlugSetDefinition: str,
			destinyPowerCapDefinition: str,
			destinyPresentationNodeDefinition: str,
			destinyProgressionDefinition: str,
			destinyProgressionLevelRequirementDefinition: str,
			destinyRecordDefinition: str,
			destinyRewardAdjusterPointerDefinition: str,
			destinyRewardAdjusterProgressionMapDefinition: str,
			destinyRewardItemListDefinition: str,
			destinySackRewardItemListDefinition: str,
			destinySandboxPatternDefinition: str,
			destinySeasonDefinition: str,
			destinySeasonPassDefinition: str,
			destinySocialCommendationDefinition: str,
			destinySocketCategoryDefinition: str,
			destinySocketTypeDefinition: str,
			destinyTraitDefinition: str,
			destinyUnlockCountMappingDefinition: str,
			destinyUnlockEventDefinition: str,
			destinyUnlockExpressionMappingDefinition: str,
			destinyVendorDefinition: str,
			destinyMilestoneDefinition: str,
			destinyActivityModifierDefinition: str,
			destinyReportReasonCategoryDefinition: str,
			destinyArtifactDefinition: str,
			destinyBreakerTypeDefinition: str,
			destinyChecklistDefinition: str,
			destinyEnergyTypeDefinition: str,
			destinySocialCommendationNodeDefinition: str,
			destinyGuardianRankDefinition: str,
			destinyGuardianRankConstantsDefinition: str,
			destinyLoadoutConstantsDefinition: str,
			destinyFireteamFinderConstantsDefinition: str,
			destinyGlobalConstantsDefinition: str
			):
		self.DestinyArtDyeChannelDefinition = destinyArtDyeChannelDefinition
		self.DestinyArtDyeReferenceDefinition = destinyArtDyeReferenceDefinition
		self.DestinyPlaceDefinition = destinyPlaceDefinition
		self.DestinyActivityDefinition = destinyActivityDefinition
		self.DestinyActivityTypeDefinition = destinyActivityTypeDefinition
		self.DestinyClassDefinition = destinyClassDefinition
		self.DestinyGenderDefinition = destinyGenderDefinition
		self.DestinyInventoryBucketDefinition = destinyInventoryBucketDefinition
		self.DestinyRaceDefinition = destinyRaceDefinition
		self.DestinyUnlockDefinition = destinyUnlockDefinition
		self.DestinyStatGroupDefinition = destinyStatGroupDefinition
		self.DestinyProgressionMappingDefinition = destinyProgressionMappingDefinition
		self.DestinyFactionDefinition = destinyFactionDefinition
		self.DestinyVendorGroupDefinition = destinyVendorGroupDefinition
		self.DestinyRewardSourceDefinition = destinyRewardSourceDefinition
		self.DestinyUnlockValueDefinition = destinyUnlockValueDefinition
		self.DestinyRewardMappingDefinition = destinyRewardMappingDefinition
		self.DestinyRewardSheetDefinition = destinyRewardSheetDefinition
		self.DestinyItemCategoryDefinition = destinyItemCategoryDefinition
		self.DestinyDamageTypeDefinition = destinyDamageTypeDefinition
		self.DestinyActivityModeDefinition = destinyActivityModeDefinition
		self.DestinyMedalTierDefinition = destinyMedalTierDefinition
		self.DestinyAchievementDefinition = destinyAchievementDefinition
		self.DestinyActivityGraphDefinition = destinyActivityGraphDefinition
		self.DestinyActivityInteractableDefinition = destinyActivityInteractableDefinition
		self.DestinyBondDefinition = destinyBondDefinition
		self.DestinyCharacterCustomizationCategoryDefinition = destinyCharacterCustomizationCategoryDefinition
		self.DestinyCharacterCustomizationOptionDefinition = destinyCharacterCustomizationOptionDefinition
		self.DestinyCollectibleDefinition = destinyCollectibleDefinition
		self.DestinyDestinationDefinition = destinyDestinationDefinition
		self.DestinyEntitlementOfferDefinition = destinyEntitlementOfferDefinition
		self.DestinyEquipmentSlotDefinition = destinyEquipmentSlotDefinition
		self.DestinyEventCardDefinition = destinyEventCardDefinition
		self.DestinyFireteamFinderActivityGraphDefinition = destinyFireteamFinderActivityGraphDefinition
		self.DestinyFireteamFinderActivitySetDefinition = destinyFireteamFinderActivitySetDefinition
		self.DestinyFireteamFinderLabelDefinition = destinyFireteamFinderLabelDefinition
		self.DestinyFireteamFinderLabelGroupDefinition = destinyFireteamFinderLabelGroupDefinition
		self.DestinyFireteamFinderOptionDefinition = destinyFireteamFinderOptionDefinition
		self.DestinyFireteamFinderOptionGroupDefinition = destinyFireteamFinderOptionGroupDefinition
		self.DestinyStatDefinition = destinyStatDefinition
		self.DestinyInventoryItemDefinition = destinyInventoryItemDefinition
		self.DestinyInventoryItemLiteDefinition = destinyInventoryItemLiteDefinition
		self.DestinyItemTierTypeDefinition = destinyItemTierTypeDefinition
		self.DestinyLoadoutColorDefinition = destinyLoadoutColorDefinition
		self.DestinyLoadoutIconDefinition = destinyLoadoutIconDefinition
		self.DestinyLoadoutNameDefinition = destinyLoadoutNameDefinition
		self.DestinyLocationDefinition = destinyLocationDefinition
		self.DestinyLoreDefinition = destinyLoreDefinition
		self.DestinyMaterialRequirementSetDefinition = destinyMaterialRequirementSetDefinition
		self.DestinyMetricDefinition = destinyMetricDefinition
		self.DestinyObjectiveDefinition = destinyObjectiveDefinition
		self.DestinySandboxPerkDefinition = destinySandboxPerkDefinition
		self.DestinyPlatformBucketMappingDefinition = destinyPlatformBucketMappingDefinition
		self.DestinyPlugSetDefinition = destinyPlugSetDefinition
		self.DestinyPowerCapDefinition = destinyPowerCapDefinition
		self.DestinyPresentationNodeDefinition = destinyPresentationNodeDefinition
		self.DestinyProgressionDefinition = destinyProgressionDefinition
		self.DestinyProgressionLevelRequirementDefinition = destinyProgressionLevelRequirementDefinition
		self.DestinyRecordDefinition = destinyRecordDefinition
		self.DestinyRewardAdjusterPointerDefinition = destinyRewardAdjusterPointerDefinition
		self.DestinyRewardAdjusterProgressionMapDefinition = destinyRewardAdjusterProgressionMapDefinition
		self.DestinyRewardItemListDefinition = destinyRewardItemListDefinition
		self.DestinySackRewardItemListDefinition = destinySackRewardItemListDefinition
		self.DestinySandboxPatternDefinition = destinySandboxPatternDefinition
		self.DestinySeasonDefinition = destinySeasonDefinition
		self.DestinySeasonPassDefinition = destinySeasonPassDefinition
		self.DestinySocialCommendationDefinition = destinySocialCommendationDefinition
		self.DestinySocketCategoryDefinition = destinySocketCategoryDefinition
		self.DestinySocketTypeDefinition = destinySocketTypeDefinition
		self.DestinyTraitDefinition = destinyTraitDefinition
		self.DestinyUnlockCountMappingDefinition = destinyUnlockCountMappingDefinition
		self.DestinyUnlockEventDefinition = destinyUnlockEventDefinition
		self.DestinyUnlockExpressionMappingDefinition = destinyUnlockExpressionMappingDefinition
		self.DestinyVendorDefinition = destinyVendorDefinition
		self.DestinyMilestoneDefinition = destinyMilestoneDefinition
		self.DestinyActivityModifierDefinition = destinyActivityModifierDefinition
		self.DestinyReportReasonCategoryDefinition = destinyReportReasonCategoryDefinition
		self.DestinyArtifactDefinition = destinyArtifactDefinition
		self.DestinyBreakerTypeDefinition = destinyBreakerTypeDefinition
		self.DestinyChecklistDefinition = destinyChecklistDefinition
		self.DestinyEnergyTypeDefinition = destinyEnergyTypeDefinition
		self.DestinySocialCommendationNodeDefinition = destinySocialCommendationNodeDefinition
		self.DestinyGuardianRankDefinition = destinyGuardianRankDefinition
		self.DestinyGuardianRankConstantsDefinition = destinyGuardianRankConstantsDefinition
		self.DestinyLoadoutConstantsDefinition = destinyLoadoutConstantsDefinition
		self.DestinyFireteamFinderConstantsDefinition = destinyFireteamFinderConstantsDefinition
		self.DestinyGlobalConstantsDefinition = destinyGlobalConstantsDefinition


class JsonWorldComponentContentPaths:

	def __init__(
			self,
			en: dict,
			fr: dict,
			es: dict,
			es_mx: dict,
			de: dict,
			it: dict,
			ja: dict,
			pt_br: dict,
			ru: dict,
			pl: dict,
			ko: dict,
			zh_cht: dict,
			zh_chs: dict
	):
		self.en = en
		self.fr = fr
		self.es = es
		self.es_mx = es_mx
		self.de = de
		self.it = it
		self.ja = ja
		self.pt_br = pt_br
		self.ru = ru
		self.pl = pl
		self.ko = ko
		self.zh_cht = zh_cht
		self.zh_chs = zh_chs

	@classmethod
	def create(cls, en: dict, fr: dict, es: dict, es_mx: dict, de: dict, it: dict, ja: dict, pt_br: dict, ru: dict, pl: dict, ko: dict, zh_cht: dict, zh_chs: dict):
		return JsonWorldComponentContentPathsTable(
			**en,
			**fr,
			**es,
			**es_mx,
			**de,
			**it,
			**ja,
			**pt_br,
			**ru,
			**pl,
			**ko,
			**zh_cht,
			**zh_chs
		)