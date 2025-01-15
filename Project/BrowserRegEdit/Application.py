from flask import Flask, render_template, request, redirect, url_for
from backend.registry_handler import *
import json



app = Flask(__name__, template_folder = 'frontend/templates')



@app.route('/')
def index ():

    return render_template('index.html', registry_tree = get_registry_tree())



@app.route('/create_registry_value', methods = ['POST'])
def create_value ():

    if request.method == 'POST':

        registry_key = request.form['registry_key']
        value_name = request.form['value_name']
        value_type = request.form['value_type']
        value_data = request.form['value_data']
        
        create_registry_value(registry_key, value_name, value_type, value_data)

        return redirect(url_for('index'))
    

@app.route('/create_registry_key', methods=['POST'])
def create_key():
    if request.method == 'POST':
        key_path = request.form['key_path']
        new_key_name = request.form['new_key_name']
        
        try:
            create_registry_key(key_path, new_key_name)
        except ValueError as e:
            return str(e), 400  # Return an error if the key already exists

        return redirect(url_for('index'))


@app.route('/rename_registry_key', methods=['POST'])
def rename_key():
    if request.method == 'POST':
        old_key = request.form['old_key']
        new_key = request.form['new_key']

        try:
            rename_registry_key(old_key, new_key)
        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@app.route('/rename_registry_value', methods=['POST'])
def rename_value():
    if request.method == 'POST':
        registry_key = request.form['registry_key']
        old_value_name = request.form['old_value_name']
        new_value_name = request.form['new_value_name']

        try:
            rename_registry_value(registry_key, old_value_name, new_value_name)
        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@app.route('/delete_registry_key', methods=['POST'])
def delete_key():
    if request.method == 'POST':
        registry_key = request.form['registry_key']

        try:
            delete_registry_key(registry_key)
        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@app.route('/delete_registry_value', methods=['POST'])
def delete_value():
    if request.method == 'POST':
        registry_key = request.form['registry_key']
        value_name = request.form['value_name']

        try:
            delete_registry_value(registry_key, value_name)
        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



def get_registry_tree():
    """Load the registry tree from the JSON file and return it."""
    try:
        with open('backend/registry.json', 'r') as file:
            data = json.load(file)  # Load the JSON file
            if isinstance(data, dict):  # Ensure it's a dictionary
                return data
            else:
                return {}  # Return empty dictionary if the structure is invalid
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty structure if the file doesn't exist or is invalid





if __name__ == '__main__':

    app.run(debug = True, host = '127.0.0.1')