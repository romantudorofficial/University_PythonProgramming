import json

# Assuming registry.json file stores the registry in a JSON format.
REGISTRY_FILE = 'backend/registry.json'

def load_registry():
    try:
        with open(REGISTRY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_registry(data):
    with open(REGISTRY_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_registry_value(key, value_name, value_type, value_data):
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
