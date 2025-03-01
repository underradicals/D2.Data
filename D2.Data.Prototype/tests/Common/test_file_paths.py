from Common import APP_SETTINGS
from Common import ROOT

def test_root_path() -> None:
	is_dir = ROOT.is_dir()
	cwd = str(ROOT)
	assert is_dir == True
	assert cwd == "F:\Systems\Programs\D2\D2.Data.Prototype"

def test_app_settings_path() -> None:
	assert APP_SETTINGS == ROOT / "appsettings.json"