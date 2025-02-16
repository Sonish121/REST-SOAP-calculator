"""
REST API Calculator Package

This package provides a REST API implementation of a calculator service
using Flask. It includes basic arithmetic operations and error handling.
"""
from .calculator import Calculator
from .app import app
from .logger import logger

__version__ = '1.0.0'
__author__ = 'sonic'

# Export the main components for easier imports
__all__ = ['Calculator', 'app']

# Optional: Configure package-level logging
import logging

# Create a logger for the REST API package
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler with formatting
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
