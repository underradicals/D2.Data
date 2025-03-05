from Infrastructure.manifest_repository import ManifestRepository


def create_table():
	db = ManifestRepository()
	db.create_table()

def insert_version(version: str):
	db = ManifestRepository()
	db.insert_version(version)

def is_empty(version: str):
	db = ManifestRepository()
	return db.is_empty(version)

def get_current_version() -> str | None:
	db = ManifestRepository()
	return db.get_current_version()