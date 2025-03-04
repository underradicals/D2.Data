from Infrastructure import download_manifest, create_table, insert_version, is_empty, get_current_version
# from Common import dict_to_list


def main():
	manifest_dict = download_manifest()
	if is_empty(manifest_dict.version):
		create_table()
		insert_version(manifest_dict.version)
		return
	old_version = get_current_version()
	if old_version == manifest_dict.version:
		print("Manifest is already present and up to date")
		return
	create_table()
	insert_version(manifest_dict.version)
	database_url = manifest_dict.database.en
	# json_url_list = dict_to_list(manifest_dict.json_tables.en)


if __name__ == "__main__":
	main()
