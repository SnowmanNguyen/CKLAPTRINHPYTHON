import sys
from os import getenv
from pathlib import Path
import constants


def _user_data_dir():
	home = Path.home()
	# get os specific path
	if sys.platform.startswith("win"):
		os_path = getenv("LOCALAPPDATA", home / "AppData" / "Local")
	elif sys.platform.startswith("darwin"):
		os_path = "~/Library/Application Support"
	else:
		# linux
		os_path = getenv("XDG_DATA_HOME", "~/.local/share")

	path = Path(os_path).expanduser()
	return path


def app_data_dir() -> Path:
	dir = _user_data_dir() / constants.APP_NAME
	dir.mkdir(parents=True, exist_ok=True)
	return dir

def db_path() -> Path:
	return app_data_dir() / 'db.sqlite'