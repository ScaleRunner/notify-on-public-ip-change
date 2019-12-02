from requests import get

from apprise import Apprise

from notify_ip.config import PROWL_API_KEY


def construct_apprise_object():
    apprise = Apprise()
    apprise.add(f"prowl://{PROWL_API_KEY}")
    return apprise


def get_public_ip():
    return get("https://api.ipify.org").text
