from Application.manifest import ManifestResponse
from Infrastructure import download_manifest, create_table, insert_version, is_empty, get_current_version, create_world_content
from Infrastructure import download_world_content_database

def do(manifest_dict: ManifestResponse):
	create_table()
	insert_version(manifest_dict.version)
	database_url = manifest_dict.database.en
	world_content_bytes = download_world_content_database(database_url)
	create_world_content(world_content_bytes, "world_content")


def main():
	manifest_dict = download_manifest()
	if manifest_dict is None:
		print("Server Error: 500: Destiny Servers have failed.")
		exit(0)
	old_version = get_current_version()
	if is_empty(manifest_dict.version) or old_version is None:
		do(manifest_dict)
		return
	old_version = get_current_version()
	if old_version == manifest_dict.version:
		print("Manifest is already present and up to date")
		return
	do(manifest_dict)

if __name__ == "__main__":
	main()
