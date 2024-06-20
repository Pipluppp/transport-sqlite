import random
COUNT = 770
COUNT_JEEP = 523
COUNT_BUS = 171
COUNT_UV = 75

def random_vehicle():
  """Returns a randomly chosen vehicle type with probabilities"""
  vehicle_choices = ['Jeep'] * 70 + ['Bus'] * 20 + ['UV'] * 10 
  return random.choice(vehicle_choices)

def random_condition():
  """Returns a randomly chosen condition type with probabilities"""
  condition_choices = ['Good'] * 95 + ['Bad'] * 5
  return random.choice(condition_choices)

def random_time():
    hour = random.randint(4, 16)
    minute_a = 30 * random.randint(0, 1)
    minute_b = 30 * random.randint(0, 1)
    dur = random.randint(6, 12)

    return f"{hour:02d}:{minute_a:02d}-{((hour + dur) % 24):02d}:{minute_b:02d}"

def match_vehicle_with_operator():
   """Mock data for Operators and Vehicles must match each others counts for operational units, and the type of vehicle operated"""
   operator_numbers_bus = [
    "PUB-0001", "PUB-0002", "PUB-0003", "PUB-0004", "PUB-0005", "PUB-0006", "PUB-0007", "PUB-0008",
    "PUB-0009", "PUB-0010", "PUB-0011", "PUB-0012", "PUB-0013", "PUB-0014", "PUB-0015", "PUB-0016",
    "PUB-0017", "PUB-0018", "PUB-0019", "PUB-0020", "PUB-0021", "PUB-0022"
    ]
   no_of_operational_units_bus = [10, 6, 11, 10, 4, 7, 11, 11, 11, 6, 9, 5, 10, 6, 9, 7, 7, 6, 7, 4, 12, 3]

   operator_numbers_jeep = [
    "PUB-0023",
    "PUB-0024",
    "PUB-0025",
    "PUB-0026",
    "PUB-0027",
    "PUB-0028",
    "PUB-0029",
    "PUB-0030",
    "PUB-0031",
    "PUB-0032",
    "PUB-0033",
    "PUB-0034",
    "PUB-0035",
    "PUB-0036",
    "PUB-0037",
    "PUB-0038",
    "PUB-0039",
    "PUB-0040",
    "PUB-0041",
    "PUB-0042",
    "PUB-0043",
    "PUB-0044",
    "PUB-0045",
    "PUB-0046",
    "PUB-0047",
    "PUB-0048",
    "PUB-0049",
    "PUB-0050",
    "PUB-0051",
    "PUB-0052",
    "PUB-0053",
    "PUB-0054",
    "PUB-0055",
    "PUB-0056",
    "PUB-0057",
    "PUB-0058",
    "PUB-0059",
    "PUB-0060",
    "PUB-0061",
    "PUB-0062",
    "PUB-0063",
    "PUB-0064",
    "PUB-0065",
    "PUB-0066",
    "PUB-0067",
    "PUB-0068",
    "PUB-0069",
    "PUB-0070",
    "PUB-0071",
    "PUB-0072",
    "PUB-0073",
    "PUB-0074",
    "PUB-0075",
    "PUB-0076",
    "PUB-0077",
    "PUB-0078",
    "PUB-0079",
    "PUB-0080",
    "PUB-0081",
    "PUB-0082",
    "PUB-0083",
    "PUB-0084",
    "PUB-0085",
    "PUB-0086",
    "PUB-0087",
    "PUB-0088",
    "PUB-0089",
  ]
   
   no_of_operational_units_jeep = [
    9, 3, 7, 10, 10, 5, 9, 11, 5, 8, 10, 6, 9, 7, 8, 8, 11, 5, 8, 8, 5, 9, 4, 8, 5, 9, 7, 12,
    8, 12, 5, 8, 9, 8, 7, 13, 8, 7, 7, 9, 8, 11, 7, 9, 7, 8, 3, 8, 7, 8, 5, 12, 7, 10, 4, 10,
    9, 7, 3, 10, 4, 8, 10, 9, 6, 12, 4
]
   
   operator_numbers_uv = [
      'PUB-0090', 'PUB-0091', 'PUB-0092', 'PUB-0093', 'PUB-0094', 'PUB-0095', 'PUB-0096', 'PUB-0097', 'PUB-0098', 'PUB-0099', 'PUB-0100'
      ]

   no_of_operational_units_uv = [12, 7, 9, 5, 2, 9, 11, 5, 9, 5, 1]
   
   operator_dict_bus = dict(zip(operator_numbers_bus, no_of_operational_units_bus))
   operator_dict_jeep = dict(zip(operator_numbers_jeep, no_of_operational_units_jeep))
   operator_dict_uv = dict(zip(operator_numbers_uv, no_of_operational_units_uv))
  
   while any(val > 0 for val in operator_dict_jeep.values()):
      key = random.choice(list(operator_dict_jeep.keys()))
      if operator_dict_jeep[key] > 0:
         print(key)
         operator_dict_jeep[key] -= 1



model_jeep = ['Bagong Jeep', 'Canter', 'COMET', 'HD50S', 'HD48GT', 'Hino 300', 'QKR77', 'Solar', 'SR Jeep']
manu_jeep = ['Sta. Rosa Motor Works', 'Almazora Motors', 'Global Electric Transport', 'Del Monte Motor Works', 'Del Monte Motor Works', 
	'Hino Motors', 'Almazora Motors' , 'Star 8 Green Technology', 'Sta. Rosa Motor Works']

model_bus = ['BF 106', 'RK8J', 'ZK6122HD9']
manu_bus = ['Daewoo Motors', 'Hino Motors', 'Yutong']

model_uv = ['Urvan', 'Crosswind']
manu_uv = ['Nissan', 'Isuzu']

""" for i in range(COUNT_UV):
    ind = random.randint(0, 1)
    print(manu_uv[ind], model_uv[ind], sep=',') """

match_vehicle_with_operator()