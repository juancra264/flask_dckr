import os
import uuid
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
