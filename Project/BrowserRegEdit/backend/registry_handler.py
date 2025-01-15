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
