from flask import Flask
import pytest
import os
import sys
from flask import request

app = Flask(__name__)

@app.route('/')
def root():
    python_version = "\npython-version%s\n" % sys.version
    return 'Hello python app : '+ python_version 


if __name__ == '__main__':
    # Get port from environment variable or choose 9099 as local default
    port = int(os.getenv("PORT", 9099))
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port, debug=True)


