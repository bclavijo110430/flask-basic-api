import platform
import subprocess
import socket
from flask import Flask



app = Flask(__name__)


@app.route('/api/v1')
def server_info():
  #  java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT).decode()
    ip_address = socket.gethostbyname(socket.gethostname())



    server_info = {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
 #       'java_version': java_version,
        'ip_addres': ip_address 
    }
    return server_info

if __name__ == '__main__':
    app.run(port=5100)
