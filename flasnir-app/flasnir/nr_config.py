from nornir import InitNornir
from nornir.core import Nornir
from flasnir.definitions import PROJECT_ROOT

HOSTS = PROJECT_ROOT / "config" / "inventory" / "hosts.yaml"
DEFAULTS = PROJECT_ROOT / "config" / "inventory" / "defaults.yaml"

def init_nornir() -> Nornir:
    return InitNornir(
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 100,
            },
        },
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": str(HOSTS),
                "defaults_file": str(DEFAULTS)
            },
        },
    )