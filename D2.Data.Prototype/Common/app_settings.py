from json import loads

from Common.file_paths import APP_SETTINGS


class Auth:
    SECTION_NAME = "Auth"

    def __init__(self, apikey: str, baseurl: str):
        self.apikey = apikey
        self.baseurl = baseurl


def get_config(section_name) -> Auth:
    with open(APP_SETTINGS, "r", encoding="utf-8") as file:
        data = loads(file.read())

    match section_name:
        case "Auth":
            auth = Auth(data[section_name]["apikey"], data[section_name]["baseurl"])
            return auth
        case _:
            print("Default")


if __name__ == "__main__":
    pass
