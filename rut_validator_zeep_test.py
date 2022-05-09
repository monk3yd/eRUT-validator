from zeep import Client, Settings
from zeep.wsse.username import UsernameToken

header = {}
settings = Settings(strict=False, extra_http_headers=header)
client = Client(
    wsdl="https://ws1.sii.cl/WSCREP/crepwsservice.wsdl",
    settings=settings
)
# print(client)
# print(client.service)

request_data = {
    "rut": "76745604",
    "dv": "2",
    # "serie": "0"
    "serie": "201903175410"
}
# client.service.SERVICE_NAME(parameter_name='value')
response = client.service.verificacionCedulaSmp(**request_data)  # 
print(response)
