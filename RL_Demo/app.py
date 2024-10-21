from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

@app.route('/get-latest-colors', methods=['GET'])
def get_latest_colors():
    new_json_folder = "new_files"
    try:
        # List files in the directory and sort them by modification time
        files = sorted(os.listdir(new_json_folder), key=lambda x: os.path.getmtime(os.path.join(new_json_folder, x)))
        latest_file = files[-1]  # Get the most recent file

        # Load the contents of the latest JSON file
        with open(os.path.join(new_json_folder, latest_file), 'r') as f:
            data = json.load(f)

        return jsonify(data)  # Return the JSON data
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # You can set debug=False for production
