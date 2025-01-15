"""
    This module is responsible for handling the registry operations.
"""

import json

REGISTRY_FILE = 'backend/registry.json'



def load_registry ():

    """
        This function is responsible for loading the registry.

        Parameters:
            None

        Returns:
            data: the registry data
    """

    try:
        with open(REGISTRY_FILE, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {}



def save_registry (data):

    """
        This function is responsible for saving the registry.

        Parameters:
            None

        Returns:
            None
    """

    with open(REGISTRY_FILE, 'w') as file:
        json.dump(data, file, indent = 4)



def create_registry_value (key, value_name, value_type, value_data):

    """
        This function is responsible for creating a registry value.

        Parameters:
            key: the registry key
            value_name: the value name
            value_type: the value type
            value_data: the value data

        Returns:
            None
    """

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



def create_registry_key (key_path, new_key_name):

    """
        This function is responsible for creating a registry key.

        Parameters:
            key_path: the registry key path
            new_key_name: the new key name

        Returns:
            None
    """

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



def rename_registry_key (old_key, new_key):

    """
        This function is responsible for renaming a registry key.

        Parameters:
            old_key: the old key name
            new_key: the new key name

        Returns:
            None
    """

    registry = load_registry()
    keys = old_key.split("\\")
    current_key = registry

    for part in keys[:-1]:

        if part not in current_key:
            raise KeyError(f"Key '{old_key}' does not exist.")
        
        current_key = current_key[part]

    key_to_rename = keys[-1]

    if key_to_rename in current_key:

        current_key[new_key] = current_key.pop(key_to_rename)
        save_registry(registry)

    else:
        raise KeyError(f"Key '{old_key}' does not exist.")



def rename_registry_value (registry_key, old_value_name, new_value_name):

    """
        This function is responsible for renaming a registry value.

        Parameters:
            registry_key: the registry key
            old_value_name: the old value name
            new_value_name: the new value name

        Returns:
            None
    """

    registry = load_registry()
    keys = registry_key.split("\\")
    current_key = registry

    for part in keys:

        if part not in current_key:
            raise KeyError(f"Key '{registry_key}' does not exist.")
        
        current_key = current_key[part]

    if old_value_name in current_key:
        current_key[new_value_name] = current_key.pop(old_value_name)
        save_registry(registry)

    else:
        raise KeyError(f"Value '{old_value_name}' does not exist in key '{registry_key}'.")



def delete_registry_key (registry_key):

    """
        This function is responsible for deleting a registry key.

        Parameters:
            registry_key: the registry key

        Returns:
            None
    """

    registry = load_registry()
    keys = registry_key.split("\\")
    current_key = registry

    for part in keys[:-1]:

        if part not in current_key:
            raise KeyError(f"Key '{registry_key}' does not exist.")
        
        current_key = current_key[part]

    last_key = keys[-1]

    if last_key in current_key:
        del current_key[last_key]
        save_registry(registry)

    else:
        raise KeyError(f"Key '{registry_key}' does not exist.")



def delete_registry_value (registry_key, value_name):

    """
        This function is responsible for deleting a registry value.

        Parameters:
            registry_key: the registry key
            value_name: the value name

        Returns:
            None
    """

    registry = load_registry()
    keys = registry_key.split("\\")
    current_key = registry

    for part in keys:

        if part not in current_key:
            raise KeyError(f"Key '{registry_key}' does not exist.")
        
        current_key = current_key[part]

    if value_name in current_key:
        del current_key[value_name]
        save_registry(registry)

    else:
        raise KeyError(f"Value '{value_name}' does not exist in key '{registry_key}'.")



def edit_registry_value (registry_key, value_name, new_value):

    """
        This function is responsible for editing a registry value.

        Parameters:
            registry_key: the registry key
            value_name: the value name
            new_value: the new value

        Returns:
            None
    """

    registry = load_registry()
    keys = registry_key.split("\\")
    current_key = registry

    for part in keys:

        if part not in current_key:
            raise KeyError(f"Key '{registry_key}' does not exist.")
        
        current_key = current_key[part]

    if value_name in current_key:

        current_key[value_name] = {
            "type": "string",
            "data": new_value
        }

        save_registry(registry)
        
    else:
        raise KeyError(f"Value '{value_name}' does not exist in key '{registry_key}'.")