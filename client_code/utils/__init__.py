import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import functools
from itertools import cycle

def to_upper(x):
    try:
        return x.strip().upper()
    except Exception:
        return x


# append a prefix in each key of a form_config (dict)
# crawls recursively into nested sublists
def form_config_prefix_key(form_config: list, prefix: str):
    def map_fn(item):
        if type(item) == list:
            return [*list(map(map_fn, item))]
        elif type(item) == dict:
            item = {**item}
            if "key" in item:
                item["key"] = f"{prefix}{item['key']}"
            return item
        raise Exception("form_config must be a list or dict")

    return list(map(map_fn, [*form_config]))