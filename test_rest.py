import requests

def test_rest_api():
    base_url = 'http://localhost:5000/api/calculate'
    test_data = {'num1': 10, 'num2': 5}
    
    operations = ['add', 'subtract', 'multiply', 'divide']
    
    for op in operations:
        response = requests.post(f'{base_url}/{op}', json=test_data)
        print(f'REST {op.capitalize()}: {response.json()}')
        
test_rest_api()