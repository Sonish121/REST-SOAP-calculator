import logging

def setup_logger():
    # Create a logger for the SOAP API package
    logger = logging.getLogger('soap_api')
    logger.setLevel(logging.INFO)

    # Create console handler with formatting
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

logger = setup_logger()
