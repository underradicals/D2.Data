from typing import Any
from typing import Generator
from requests import Session, Response
from contextlib import contextmanager

from Common import Auth
from Common import get_config


@contextmanager
def download( session: Session, url: str ) -> Generator[ Response, Any, None ]:
	try:
		config = get_config(Auth.SECTION_NAME)
		session.headers.update({ 'x-api-key': config.apikey })
		response = session.get(f'{config.baseurl}{url}', stream = True)
		response.raise_for_status()
		yield response
	except Exception as e:
		print(e)
	finally:
		session.close()
