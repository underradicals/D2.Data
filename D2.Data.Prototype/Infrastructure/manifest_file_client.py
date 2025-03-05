from io import BytesIO
from zipfile import ZipFile


def create_world_content(wc_bytes: bytes, filename: str) -> None:
	io_bytes = BytesIO(wc_bytes)
	with ZipFile(io_bytes, "r") as archive:
		name = archive.namelist()[0]
		with archive.open(name, "r") as f1:
			data = f1.read()
			with open(f"{filename}.db", "wb") as f2:
				f2.write(data)