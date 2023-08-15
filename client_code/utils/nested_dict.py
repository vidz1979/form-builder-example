import anvil.server
class NestedDict(dict):
    def set_value(self, path: str, value: any):
        path_keys = path.split(".")
        curr_item = self
        for i, key in enumerate(path_keys):
            if i < len(path_keys) - 1:
                if type(curr_item) == list:
                    curr_item = {}
                else:
                    curr_item.setdefault(key, {})
                    curr_item = curr_item[key]
            else:
                curr_item[key] = value
        return self

    def get_value(self, path):
        path_keys = path.split(".")
        curr_item = self
        for i, key in enumerate(path_keys):
            if i < len(path_keys) - 1:
                # workaround, remove
                if type(curr_item) == list:
                    curr_item = {}
                curr_item = curr_item.get(key, {})
            else:
                return curr_item.get(key, None)
        return None
