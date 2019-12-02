from notify_ip.loop import run_server
from notify_ip.server import construct_apprise_object

if __name__ == "__main__":
    apprise = construct_apprise_object()
    run_server(apprise)
