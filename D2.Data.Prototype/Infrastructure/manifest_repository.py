import sqlite3


class ManifestRepository:

	def __init__(self):
		self.connection = sqlite3.connect('manifest.db')
		self.connection.execute("PRAGMA foreign_keys = ON")
		self.connection.execute("PRAGMA journal_mode = WAL")
		self.connection.execute("PRAGMA synchronous = OFF")
		self.connection.execute("PRAGMA cache_size = 100000")
		self.connection.execute("PRAGMA page_size = 4096")

	def create_table( self ):
		cursor = self.connection.cursor()
		sql = """
		DROP TABLE IF EXISTS manifest;
    CREATE TABLE IF NOT EXISTS MANIFEST(
        ID INTEGER PRIMARY KEY,
        VERSION TEXT NOT NULL
    );
		"""
		try:
			cursor.executescript(sql)
		except Exception as e:
			print(e)
		finally:
			self.connection.commit()
			self.connection.close()

	def insert_version(self, version):
		cursor = self.connection.cursor()
		sql = """
		INSERT INTO manifest (version) VALUES (?)
		"""
		try:
			cursor.execute(sql, (version,))
		except Exception as e:
			print(e)
		finally:
			self.connection.commit()
			self.connection.close()

	def is_empty(self, version: str):
		cursor = self.connection.cursor()
		sql = """
		select version from manifest where version = ?;
		"""
		try:
			cursor.execute(sql, (version,))
			row = cursor.fetchone()
			if row is None:
				print(row)
				return True
			else:
				return False
		except Exception as e:
			print(e)
		finally:
			self.connection.commit()
			self.connection.close()

	def get_current_version(self):
		cursor = self.connection.cursor()
		sql = """
		select version from manifest order by version desc limit 1;
		"""
		try:
			cursor.execute(sql)
			row = cursor.fetchone()
			if row is None:
				return None
			else:
				return row[0]
		except Exception as e:
			print(e)
		finally:
			self.connection.commit()
			self.connection.close()
