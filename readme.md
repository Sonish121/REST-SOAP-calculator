# Calculator API Service

A dual-implementation calculator service providing both REST and SOAP APIs. This project demonstrates how to implement and run concurrent API services using Python, Flask, and Spyne.

## Features

- REST API using Flask
- SOAP API using Spyne
- Concurrent server operation
- Basic arithmetic operations (add, subtract, multiply, divide)
- Error handling for invalid operations and division by zero
- Modular code structure
- Comprehensive testing tools

## Project Structure

```
calculator/
│
├── requirements.txt
├── rest_api/
│   ├── __init__.py
│   ├── app.py
│   └── calculator.py
│
├── soap_api/
│   ├── __init__.py
│   ├── app.py
│   └── calculator.py
│
├── main.py
├── test_rest.py
└── test_soap.py
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/calculator-api.git
cd calculator-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

Start both REST and SOAP servers:
```bash
python main.py
```

This will start:
- REST API server on `http://localhost:5000`
- SOAP API server on `http://localhost:8000`

## API Usage

### REST API

The REST API accepts POST requests with JSON data.

#### Endpoint Format
```
POST http://localhost:5000/api/calculate/<operation>
```

Available operations:
- add
- subtract
- multiply
- divide

#### Request Body
```json
{
    "num1": <first_number>,
    "num2": <second_number>
}
```

#### Example using curl
```bash
curl -X POST http://localhost:5000/api/calculate/add \
-H "Content-Type: application/json" \
-d '{"num1": 10, "num2": 5}'
```

#### Response Format
```json
{
    "result": <calculated_result>
}
```

### SOAP API

The SOAP API provides a WSDL interface at `http://localhost:8000/?wsdl`

Available methods:
- add(num1, num2)
- subtract(num1, num2)
- multiply(num1, num2)
- divide(num1, num2)

## Testing

The project includes test scripts for both APIs:

Test REST API:
```bash
python test_rest.py
```

Test SOAP API:
```bash
python test_soap.py
```

## Error Handling

Both APIs handle common errors including:
- Invalid operations
- Division by zero
- Invalid input types
- Missing parameters

Error responses include appropriate status codes and error messages.

## Development

To add new operations:

1. Add the operation method to both `rest_api/calculator.py` and `soap_api/calculator.py`
2. Add the operation to the REST API routes in `rest_api/app.py`
3. Add the operation to the SOAP service methods in `soap_api/app.py`
4. Update the tests accordingly

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## TEST

For support, please open an issue in the GitHub repository.

OUTPUT for REST_API
'''
sonish@Spamwer ~/D/REST-SOAP-Calculator (main)> python test_rest.py
REST Add: {'result': 15.0}
REST Subtract: {'result': 5.0}
REST Multiply: {'result': 50.0}
REST Divide: {'result': 2.0}
'''

OUTPUT for SOAP_API
'''
sonish@Spamwer ~/D/REST-SOAP-Calculator (main)> python test_soap.py
SOAP Add: 15.0
SOAP Subtract: 5.0
SOAP Multiply: 50.0
SOAP Divide: 2.0
'''

