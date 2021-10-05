#from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from flasnir.nr_config import init_nornir

def getusers():
    nr = init_nornir()

    results = nr.run(task=napalm_get, getters='users')
    processed_results = {}
    for host, data in results.items():
        processed_results[host] = [
            {
                "username": username,
                "password": details["password"],
                "privilege": details["level"],
            }
            for username, details in data.result["users"].items()
        ]

    return processed_results

def getinter():
    nr = init_nornir()

    results = nr.run(task=napalm_get, getters='interfaces')

    processed_results = {}
    for host, data in results.items():
        processed_results[host] = {
            interface_name: values["mac_address"]
            for interface_name, values in data.result["interfaces"].items()
        }

    return processed_results