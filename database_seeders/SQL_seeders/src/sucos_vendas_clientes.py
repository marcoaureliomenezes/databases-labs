from src.utils import RandomCommonValuesGenerator


class ClientesSucosVendas:

  def __init__(self):
    self.rand_generator = RandomCommonValuesGenerator()
    self.logradouros = ['Rua Paraná', 'Rua Renato Azeredo', 'Praça Jose Silvio', 'Rua Roberto Simonsen', 'Rua Direita', 'Rua Tauan Menezes']
    self.bairros = ['Laranjeiras', 'Vila Prado', 'Aclimação', 'Centro', 'Milagres', 'Manga', 'Esperança']
    self.cidades = ['Inhauma - MG', 'Belo Horizonte - MG', 'São Paulo - SP', 'Sete Lagoas - MG', 'São Carlos - SP']
    self.genders = ['M', 'F']
    self.age_range = ('1967-01-01', '2006-01-01')

  def gen_cliente_row(self):
    return dict(
      cpf = self.rand_generator.gen_cpf(),
      nome = self.rand_generator.gen_name(),
      logradouro = self.rand_generator.gen_obj.gen_fake_distinct(self.logradouros),
      numero = self.rand_generator.gen_obj.gen_int(54, 1500),
      bairro = self.rand_generator.gen_obj.gen_fake_distinct(self.bairros),
      cidade = self.rand_generator.gen_obj.gen_fake_distinct(self.cidades),
      data_nascimento = self.rand_generator.gen_obj.gen_date(*self.age_range),
      genero = self.rand_generator.gen_obj.gen_fake_distinct(self.genders),
      primeira_compra = self.rand_generator.gen_obj.gen_fake_bool(50)
    )  

  def gen_clientes(self, size):
    data_tuple = [tuple(self.gen_cliente_row().values()) for i in range(size)]
    columns = list(self.gen_cliente_row().keys())
    return data_tuple, columns