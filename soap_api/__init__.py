"""
SOAP API Calculator Package

This package provides a SOAP API implementation of a calculator service
using Spyne. It includes basic arithmetic operations and error handling.
"""

from .calculator import Calculator
from .logger import logger
from .app import soap_app, CalculatorService

__version__ = '1.0.0'
__author__ = 'sonic'

# Export the main components for easier imports
__all__ = ['Calculator', 'soap_app', 'CalculatorService']

# Optional: Configure package-level logging
import logging

# Create a logger for the SOAP API package
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler with formatting
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)