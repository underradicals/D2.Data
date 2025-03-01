from Common import get_config, Auth, APP_SETTINGS

def test_get_config() -> None:
    # Arrange
    config = get_config(Auth.SECTION_NAME)

    # Act
    apikey = config.apikey
    baseurl = config.baseurl

    # Asert
    assert apikey is not None
    assert baseurl is not None
    assert apikey != ""
    assert baseurl != ""


