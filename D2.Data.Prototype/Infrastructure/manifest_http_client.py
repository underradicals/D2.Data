from requests import Session

from Application.manifest import JsonWorldComponentContentPathsResponse
from Application.manifest import ManifestResponse
from Application.manifest import MobileWorldContentPathsResponse
from .http_io import download



def download_manifest() -> ManifestResponse:
	session = Session()
	with download(session, '/Platform/Destiny2/Manifest') as response:
		manifest = response.json()
		Response = manifest[ "Response" ]
		dictionary = {
			'version': Response[ "version" ],
			'database': MobileWorldContentPathsResponse.create(Response["mobileWorldContentPaths"]),
			'json_tables': JsonWorldComponentContentPathsResponse.create(Response[ "jsonWorldComponentContentPaths" ])
		}
		return ManifestResponse(**dictionary)

