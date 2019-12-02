from time import sleep

from apprise import Apprise

from notify_ip.server import get_public_ip

CHECK_INTERVAL_IN_SECONDS = 60 * 15


def run_server(apprise: Apprise):
    apprise.notify("Starting notification service")
    public_ip = ""

    while True:
        current_ip = get_public_ip()
        if public_ip != current_ip:
            apprise.notify(f"Public IP changed to '{current_ip}'")
            public_ip = current_ip
        sleep(CHECK_INTERVAL_IN_SECONDS)

