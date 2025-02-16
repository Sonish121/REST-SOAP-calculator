from zeep import Client

def test_soap_api():
    client = Client('http://localhost:8000/?wsdl')
    num1, num2 = 10, 5
    
    operations = ['add', 'subtract', 'multiply', 'divide']
    
    for op in operations:
        result = getattr(client.service, op)(num1, num2)
        print(f'SOAP {op.capitalize()}: {result}')
test_soap_api()
