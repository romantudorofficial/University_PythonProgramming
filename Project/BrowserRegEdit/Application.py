"""
    This module is responsible for handling the Front-End and Back-End communication.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import json

from backend.registry_handler import *

application = Flask(__name__, template_folder = 'frontend/templates')
application.secret_key = 'regedit'



@application.route('/')

def index ():

    """
        This function is responsible for rendering the index.html template.

        Parameters:
            None

        Returns:
            render_template: renders the index.html template
    """

    return render_template('index.html', registry_tree = get_registry_tree())



@application.route('/create_registry_value', methods = ['POST'])

def create_value ():

    """
        This function is responsible for creating a new registry value.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        registry_key = request.form['registry_key']
        value_name = request.form['value_name']
        value_type = request.form['value_type']
        value_data = request.form['value_data']
        
        create_registry_value(registry_key, value_name, value_type, value_data)

        return redirect(url_for('index'))



@application.route('/create_registry_key', methods = ['POST'])

def create_key ():

    """
        This function is responsible for creating a new registry key.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        key_path = request.form['key_path']
        new_key_name = request.form['new_key_name']
        
        try:
            create_registry_key(key_path, new_key_name)

        except ValueError as e:
            return str(e), 400

        return redirect(url_for('index'))



@application.route('/rename_registry_key', methods = ['POST'])

def rename_key ():

    """
        This function is responsible for renaming a registry key.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        old_key = request.form['old_key']
        new_key = request.form['new_key']

        try:
            rename_registry_key(old_key, new_key)

        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@application.route('/rename_registry_value', methods = ['POST'])

def rename_value ():

    """
        This function is responsible for renaming a registry value.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        registry_key = request.form['registry_key']
        old_value_name = request.form['old_value_name']
        new_value_name = request.form['new_value_name']

        try:
            rename_registry_value(registry_key, old_value_name, new_value_name)

        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@application.route('/delete_registry_key', methods = ['POST'])

def delete_key ():

    """
        This function is responsible for deleting a registry key.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        registry_key = request.form['registry_key']

        try:
            delete_registry_key(registry_key)

        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@application.route('/delete_registry_value', methods = ['POST'])

def delete_value ():

    """
        This function is responsible for deleting a registry value.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        registry_key = request.form['registry_key']
        value_name = request.form['value_name']

        try:
            delete_registry_value(registry_key, value_name)

        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@application.route('/edit_registry_value', methods = ['POST'])

def edit_value ():

    """
        This function is responsible for editing a registry value.

        Parameters:
            None
            
        Returns:
            redirect: redirects the user to the index route
    """

    if request.method == 'POST':

        registry_key = request.form['registry_key']
        value_name = request.form['value_name']
        new_value = request.form['new_value']

        try:
            edit_registry_value(registry_key, value_name, new_value)

        except KeyError as e:
            return f"Error: {str(e)}", 400

        return redirect(url_for('index'))



@application.route('/', methods = ['GET', 'POST'])

def search_value ():

    """
        This function is responsible for handling the search functionality.
        
        Parameters:
            None
            
        Returns:
            render_template: renders the index.html template
    """
    
    registry_tree = load_registry()
    search_results = []

    if request.method == 'POST':

        search_term = request.form.get('search_term', '')

        if search_term:
            search_results = search_registry(registry_tree, search_term)
            session['search_results'] = search_results

    return render_template('index.html', registry_tree = registry_tree, search_results = session.get('search_results', []))



def get_registry_tree ():

    """
        This function is responsible for loading the registry data.

        Parameters:
            None
            
        Returns:
            data: the registry data
    """

    try:
        with open('backend/registry.json', 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                return {}
            
    except (FileNotFoundError, json.JSONDecodeError):
        return {}



if __name__ == '__main__':

    application.run(debug = True, host = '127.0.0.1')