def get_value(elmnt):
    if isinstance(elmnt, dict):
        return '[complex value]'
    return f'\'{elmnt}\''


def build_plain(data, name=""):
    res = []
    for k, v in data.items():
        if v["type"] == "nested":
            res.append(build_plain(v["value"], name=name + f"{k}."))
        elif v["type"] == "added":
            res.append(f"Property \'{name}{k}\' was added with value: {get_value(v['value'])}")  # noqa E:501
        elif v["type"] == "removed":
            res.append(f"Property \'{name}{k}\' was removed")
        elif v["type"] == "changed":
            res.append(f"Property \'{name}{k}\' was updated. From {get_value(v['old_value'])} to {get_value(v['new_value'])}")  # noqa E:501
    return "\n".join(res)
