from typing import TypedDict

from Common import replace_dashes
from Domain.manifest import JsonWorldComponentContentPaths
from Domain.manifest import MobileWorldContentPaths


class ManifestProps(TypedDict):
	version: str
	database: MobileWorldContentPaths
	json_tables: JsonWorldComponentContentPaths


class ManifestResponse:

	def __init__( self, version: str, database: MobileWorldContentPaths, json_tables: JsonWorldComponentContentPaths ) -> None:
		self.version = version
		self.database = database
		self.json_tables = json_tables


class MobileWorldContentPathsResponse:

	@classmethod
	def create( cls, entity ):
		return MobileWorldContentPaths(**replace_dashes(entity))


class JsonWorldComponentContentPathsResponse:

	@classmethod
	def create( cls, entity ):
		return JsonWorldComponentContentPaths(**replace_dashes(entity))
