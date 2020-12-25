import os
import requests
from bs4 import BeautifulSoup as bs

from ..tools.path import run_here
from ..operate.config import load_config

__all__ = ["check_source"]

config_data = load_config()


def get_page(url):
    timeout = config_data["timeout"]

    while True:
        try:
            page = requests.get(url, timeout=timeout)
            break
        except requests.Timeout:
            timeout = timeout + 1
        except requests.URLRequired:
            print(f"Invalid URL: {url}")
            return

    if page.status_code == requests.codes.ok:
        return page
    print(f"{url} is not work")
    return


def get_latest_version_number():
    # Try get page
    page = get_page("https://market.ape-apps.com/my-colony.html")

    # If page is work, find out latest version number
    if page is not None:
        page = bs(page.text, "lxml")
        download_options = page.find_all(class_="appDownloadItem")

        for option in download_options:
            if "html5" in str(option):
                centereds = option.find_all(class_="centered")

                for centered in centereds:
                    if "Tag" != centered.contents[0].__class__.__name__:
                        latest_version_number = str(centered.contents[0])
                        break
                break
    else:
        return

    return latest_version_number


@run_here
def download_source(file, *, version=get_latest_version_number()):
    if version is not None:
        page = get_page(
            f"https://www.apewebapps.com/apps/my-colony/{version}/{file}.js"
        )
        page.encoding = "UTF-8"

        if page is not None:
            os.chdir("..")

            with open(f"source/{file}.js", "w", encoding="UTF-8") as source_file:
                source_file.write(page.text)

            return True
        return False
    return False


@run_here
def check_source():
    os.chdir("..")
    listdir = os.listdir("source")

    if "game.js" not in listdir or "strings.js" not in listdir:
        print("Missing source file, trying to download...")

        if "game.js" not in listdir:
            download_source("game")

        if "strings.js" not in listdir:
            download_source("strings")

        print("Download completed")
