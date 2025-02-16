from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from .calculator import Calculator
from . import logger

class CalculatorService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def add(ctx, num1, num2):
        logger.info(f'SOAP API: Received add request for {num1} and {num2}')
        return calculator.add(num1, num2)

calculator = Calculator()

class CalculatorService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def add(ctx, num1, num2):
        return calculator.add(num1, num2)
    
    @rpc(Float, Float, _returns=Float)
    def subtract(ctx, num1, num2):
        return calculator.subtract(num1, num2)
    
    @rpc(Float, Float, _returns=Float)
    def multiply(ctx, num1, num2):
        return calculator.multiply(num1, num2)
    
    @rpc(Float, Float, _returns=Float)
    def divide(ctx, num1, num2):
        return calculator.divide(num1, num2)

application = Application(
    [CalculatorService],
    tns='calculator.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

soap_app = WsgiApplication(application)