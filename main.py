from wsgiref.simple_server import make_server
from threading import Thread
from rest_api.app import app as rest_app
from soap_api.app import soap_app
from rest_api.logger import logger as rest_logger
from soap_api.logger import logger as soap_logger

def run_soap_server():
    server = make_server('127.0.0.1', 8000, soap_app)
    soap_logger.info('SOAP Server running at http://127.0.0.1:8000')
    server.serve_forever()

if __name__ == '__main__':
    # Start SOAP server in a separate thread
    soap_thread = Thread(target=run_soap_server)
    soap_thread.daemon = True
    soap_thread.start()
    
    # Run REST server
    rest_logger.info('REST Server running at http://127.0.0.1:5000')
    rest_app.run(host='127.0.0.1', port=5000)

