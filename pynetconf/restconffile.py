import requests
from rich import print


headers = {
    "Accept": "application/yang-data+json",
}


def main():
    requests.packages.urllib3.disable_warnings()
    url = "https://10.18.10.25/restconf/data/Cisco-IOS-XE-native:native/interface"
    response = requests.get(url, headers=headers, auth=(
        "ins", "ins@lab"), verify=False)
    print(response.text)


if __name__ == '__main__':
    main()
