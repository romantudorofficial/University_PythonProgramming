import json

REGISTRY_FILE = 'backend/registry.json'



def load_registry ():

    try:

        with open(REGISTRY_FILE, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:

        return {}



def save_registry (data):

    with open(REGISTRY_FILE, 'w') as file:
        json.dump(data, file, indent = 4)



def create_registry_value (key, value_name, value_type, value_data):

    registry = load_registry()
    keys = key.split("\\")
    current_key = registry

    for part in keys:
        if part not in current_key:
            current_key[part] = {}

        current_key = current_key[part]

    current_key[value_name] = {
        "type": value_type,
        "data": value_data
    }
    
    save_registry(registry)



def create_registry_key(key_path, new_key_name):
    registry = load_registry()
    keys = key_path.split("\\")
    current_key = registry

    for part in keys:
        if part not in current_key:
            current_key[part] = {}
        current_key = current_key[part]

    if new_key_name in current_key:
        raise ValueError(f"The key '{new_key_name}' already exists under '{key_path}'")
    else:
        current_key[new_key_name] = {}

    save_registry(registry)


def rename_registry_key(old_key, new_key):
    """
    Renames a registry key from `old_key` to `new_key`.
    """
    registry = load_registry()
    keys = old_key.split("\\")
    current_key = registry

    # Traverse the tree to find the parent of the key to rename
    for part in keys[:-1]:
        if part not in current_key:
            raise KeyError(f"Key '{old_key}' does not exist.")
        current_key = current_key[part]

    # Rename the key
    key_to_rename = keys[-1]
    if key_to_rename in current_key:
        current_key[new_key] = current_key.pop(key_to_rename)
        save_registry(registry)
    else:
        raise KeyError(f"Key '{old_key}' does not exist.")



def rename_registry_value(registry_key, old_value_name, new_value_name):
    """
    Renames a value within a specified registry key.
    """
    registry = load_registry()
    keys = registry_key.split("\\")
    current_key = registry

    # Traverse the tree to find the target key
    for part in keys:
        if part not in current_key:
            raise KeyError(f"Key '{registry_key}' does not exist.")
        current_key = current_key[part]

    # Rename the value
    if old_value_name in current_key:
        current_key[new_value_name] = current_key.pop(old_value_name)
        save_registry(registry)
    else:
        raise KeyError(f"Value '{old_value_name}' does not exist in key '{registry_key}'.")
