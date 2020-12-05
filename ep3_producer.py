from faker import Faker
from faker_vehicle import VehicleProvider
import time
import random
import redis
import json

fake = Faker()
fake.add_provider(VehicleProvider)

r = redis.Redis(host="192.168.15.133", port=6379, db=0, password="")

while(True):
  output = {
    "id": fake.numerify(text="id-%#%#"),
    "nome": fake.name(),
    "telefone": fake.numerify(text="(%%) 9%%%%-%%%%"),
    "email": fake.ascii_safe_email(),
    "endereco": fake.address(),
    "veiculo_placa": fake.license_plate(),
    "veiculo_ano": fake.vehicle_year(),
    "veiculo_fabricante": fake.vehicle_make(),
    "veiculo_modelo": fake.vehicle_model()
  }
  print(output)
  print(r.xadd("veiculo", output))
  time.sleep(random.randint(1, 10))