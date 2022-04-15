import os
import json


# The file names and paths of the needed json config files and others
class FileNames:
    _cwd = os.getcwd()
    web_server_settings = os.path.join(_cwd, "config.json")

    print(f"[+] Detected `config.json` at {web_server_settings}")


# Settings needed for hosting the website
class Config:
    with open(FileNames.web_server_settings, "r", encoding="utf-8") as _file:
        data = json.load(_file)
        print("[+] Loaded `config.json`")

    try:
        host: str = data["host"]
        if not(len(str(host).split(".")) == 4):
            host: str = "0.0.0.0"
    except KeyError:
        host: str = "0.0.0.0"

    try:
        port = data["port"]
        try:
            port: int = int(port)
        except ValueError:
            port: int = 80
    except KeyError:
        port: int = 80

    try:
        debug = data["debug"]
        if isinstance(debug, str):
            if debug.lower() in ("true", "t", "yes", "y"):
                debug: bool = True
            else:
                debug: bool = False
        elif isinstance(debug, bool):
            pass
        else:
            debug: bool = False
    except KeyError:
        debug: bool = False

    try:
        DEV = data["dev_mode"]
        if isinstance(DEV, str):
            if DEV.lower() in ("true", "t", "yes", "y"):
                DEV: bool = True
            else:
                DEV: bool = False
        elif isinstance(DEV, bool):
            pass
        else:
            DEV: bool = False
    except KeyError:
        DEV: bool = False


def log(message: str, ipaddr: str = False, mode: str = "DEBUG"):
    if Config.DEV:
        if not(ipaddr):
            print(f'[{mode}]: {message}')
        if (mode and ipaddr):
            print(f'[{mode}][{ipaddr}]: {message}')
