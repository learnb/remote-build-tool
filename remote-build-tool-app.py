from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

with open('config.json') as f:
    config = json.load(f)

scripts = config['scripts']

@app.route('/update', methods=['GET'])
def execute():
    script = scripts['update']

    try:
        output = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if output.returncode != 0:
            return jsonify({'error': output.stderr.decode('utf-8')}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'output': output.stdout.decode('utf-8')}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)