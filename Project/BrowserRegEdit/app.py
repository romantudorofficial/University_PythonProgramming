from flask import Flask, render_template, request, redirect, url_for
import json
from backend.registry_handler import create_registry_value

app = Flask(__name__, template_folder='frontend/templates')

@app.route('/')
def index():
    return render_template('index.html', registry_tree=get_registry_tree())

@app.route('/create_registry_value', methods=['POST'])
def create_value():
    if request.method == 'POST':
        registry_key = request.form['registry_key']
        value_name = request.form['value_name']
        value_type = request.form['value_type']
        value_data = request.form['value_data']
        
        create_registry_value(registry_key, value_name, value_type, value_data)
        return redirect(url_for('index'))

def get_registry_tree():
    """Simulate a registry tree."""
    # For demonstration purposes, a simplified static registry structure is used
    # In a real scenario, you would retrieve it dynamically from a backend file or database
    return {
        "HKEY_LOCAL_MACHINE": {
            "Software": {
                "MyApp": {
                    "Version": "1.0",
                    "Settings": {
                        "EnableFeatureX": "True"
                    }
                }
            }
        }
    }

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
