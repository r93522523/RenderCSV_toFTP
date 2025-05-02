from flask import Flask, request, jsonify
import paramiko
import os
import shutil
from werkzeug.utils import secure_filename

app = Flask(__name__)

hostname = '35.242.211.28'
port = 2022
username = 'familymart-tw-test'
key_path = r'/mnt/data/familymart-tw-test.key'
render_folder = r'/mnt/data'

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        csv_file = [f for f in os.listdir(render_folder) if f.endswith('.csv')]
        if csv_file:
            filename = csv_files[0]
            uploaded_file = os.path.join(render_folder, filename)
            
            done_folder = os.path.join(render_folder, 'done')
            os.makedirs(done_folder, exist_ok=True)
            done_path = os.path.join(done_folder, filename)
            shutil.copy(uploaded_file_path, done_path)

            private_key = paramiko.RSAKey.from_private_key_file(key_path)
            transport = paramiko.Transport((hostname, port))
            transport.connect(username=username, pkey=private_key)
            sftp = paramiko.SFTPClient.from_transport(transport)

            FTP_path = f'/APItest/{filename}'
            sftp.put(done, FTP_path)

            sftp.close()
            transport.close()

            return jsonify({'message': 'File uploaded successfully'}), 200
        else:
            return jsonify({'error': 'No CSV file found'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
#    app.run(debug=True)
