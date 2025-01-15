import json

registry_file = "registry.json"

# Load or initialize the registry
try:
    with open(registry_file, "r") as f:
        registry = json.load(f)
except FileNotFoundError:
    registry = {}

# Save the registry to the JSON file
def save_registry():
    with open(registry_file, "w") as f:
        json.dump(registry, f, indent=4)

# Create a registry key
def create_key(path):
    keys = path.split("\\")
    current = registry
    for key in keys:
        if key not in current:
            current[key] = {}
        current = current[key]
    save_registry()
    return True

# Delete a registry key
def delete_key(path):
    keys = path.split("\\")
    current = registry
    for key in keys[:-1]:
        if key not in current:
            return False
        current = current[key]
    if keys[-1] in current:
        del current[keys[-1]]
        save_registry()
        return True
    return False

# Get the current registry state
def get_registry():
    return registry
