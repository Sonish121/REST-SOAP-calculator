from flask import Flask, request, jsonify
from .calculator import Calculator
from .logger import logger

app = Flask(__name__)
calculator = Calculator()

@app.route('/api/calculate/<operation>', methods=['POST'])
def calculate(operation):
    logger.info(f'REST API: Received {operation} request')
    try:
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        
        operations = {
            'add': calculator.add,
            'subtract': calculator.subtract,
            'multiply': calculator.multiply,
            'divide': calculator.divide
        }
        
        if operation not in operations:
            logger.error(f'Invalid operation: {operation}')
            return jsonify({'error': 'Invalid operation'}), 400
            
        result = operations[operation](num1, num2)
        logger.info(f'Operation {operation} completed successfully')
        return jsonify({'result': result})
        
    except ValueError as e:
        logger.error(f'ValueError: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f'Internal server error: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500