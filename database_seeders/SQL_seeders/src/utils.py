from functools import reduce
from faker import Faker
from random import choice, randint, gauss
from datetime import datetime as dt


class SQLParser:

  def create_insert_into(self, table_name, columns, values):
    values = reduce(lambda a, b: f"{a},\n{b}", values)
    query = f'INSERT INTO {table_name} ({", ".join(columns)}) \nVALUES\n{values};'
    return query
  

#######################################################################
#######################################################################
class UtilsGenerator:

  def zfill_int(self, num, order=None):
    return str(num).zfill(order)

#######################################################################
#######################################################################
class RandomValuesGenerator:

  def gen_fake_bool(self, chance=50):
    return True if randint(0,100) <= chance else False
  
  def gen_fake_distinct(self, distinct):
    return choice(distinct)
  
  def gen_int(self, min, max):
    return randint(min, max)
  
  def gen_powerint(self, size):
    return randint(1, 10**size - 1)
  
  def gen_normal_float(self, mean, std, magnitude=1, decimals=None):
    normal_num = gauss(mean, std)
    normal_num = round(normal_num, decimals) if decimals else normal_num
    normal_num = normal_num * 10**magnitude
    return normal_num

  def gen_fake_emprestimo(self):
    return float(randint(1, 100) * 100)

  def gen_fake_saldo(self, min, max):
    return randint(min, max - 1) + randint(0, 99) / 100
    
  def gen_categorical(self, distinct):
    return choice(distinct)
  
  def gen_date(self, start, end, formato='%Y-%m-%d'):
    str_to_timestamp = lambda x: dt.timestamp(dt.strptime(x, formato))
    str_from_timestamp = lambda x: dt.strftime(dt.fromtimestamp(x), formato)
    start_timestamp = str_to_timestamp(start)
    end_timestamp = str_to_timestamp(end)
    return str_from_timestamp(randint(start_timestamp, end_timestamp))

#######################################################################
#######################################################################
class RandomCommonValuesGenerator:

  def __init__(self):
    self.utils_obj = UtilsGenerator()
    self.gen_obj = RandomValuesGenerator()
    self.faker = Faker(locale='pt_BR')

  def __gen_part(self, size, order=None):
    order = size if not order else order
    return self.utils_obj.zfill_int(self.gen_obj.gen_powerint(size), order)

  def gen_cpf(self):
    return f"{self.__gen_part(3)}.{self.__gen_part(3)}.{self.__gen_part(3)}-{self.__gen_part(2)}"

  def gen_cnpj(self):
    return f"{self.__gen_part(2)}.{self.__gen_part(3)}.{self.__gen_part(3)}/0001-{self.__gen_part(2)}"
  
  def gen_name(self):
    return self.faker.name()
  
  def gen_color(self):
    return self.faker.safe_color_name()
  
  def gen_car_plate(self):
    return self.faker.license_plate()
  
  def gen_phone_number(self):
    return self.faker.phone_number()
  
  def gen_address(self):
    return f'{self.faker.street_name()}, {self.faker.building_number()}, {self.faker.city()}, Brazil'
  
  def gen_job(self): 
    return self.faker.job()  
    
  def gen_uuid(self):
    return faker.uuid4()

  def gen_fake_csv(self):
    return self.faker.csv(data_columns=('{{name}}', '{{phone_number}}'), num_rows=10, include_row_ids=False)

  def gen_fake_json(self):
    return self.faker.csv(data_columns=('{{name}}', '{{phone_number}}'), num_rows=10, include_row_ids=False)
  
  def gen_dataframe(self):
    return self.faker.pyspark_dataframe()
  
  