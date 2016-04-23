import requests
import random
from state import State
from os.path import join, dirname
import os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bridge_ip = os.getenv("ip")
username = os.getenv("username")
light_index = os.getenv("light_index")

base_uri = 'http://%s/api/%s' % (bridge_ip, username)


def random_color():
    return State("true", 255, random.randint(1, 65535), 255).to_json()


def main():
    while True:
        requests.put(base_uri+'/lights/%s/state' % light_index, data=random_color())

if __name__ == "__main__":
    main()
