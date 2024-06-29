from src.utils import RandomCommonValuesGenerator

class VendedoresSucosVendas:

  def __init__(self):
    self.rand_generator = RandomCommonValuesGenerator()
    self.comission_rates = [0.1, 0.15, 0.125, 0.175]
    self.bairros = ['Laranjeiras', 'Vila Prado', 'Aclimação', 'Centro', 'Milagres', 'Manga', 'Esperança']
    self.cidades = ['Inhauma - MG', 'Belo Horizonte - MG', 'São Paulo - SP', 'Sete Lagoas - MG', 'São Carlos - SP']
    self.admissao_range = ('2010-01-01', '2024-01-01')

  def gen_vendedores_row(self):
    return dict(
      matricula = str(self.rand_generator.gen_obj.gen_powerint(8)).zfill(8),
      nome = self.rand_generator.gen_name(),
      percentual_comissao = self.rand_generator.gen_obj.gen_fake_distinct(self.comission_rates),
      data_admissao = self.rand_generator.gen_obj.gen_date(*self.admissao_range),
      de_ferias = self.rand_generator.gen_obj.gen_fake_bool(chance=20),
      bairro = self.rand_generator.gen_obj.gen_fake_distinct(self.bairros),
      cidade = self.rand_generator.gen_obj.gen_fake_distinct(self.cidades)
    )  

  def gen_vendedores(self, size=10):
    data_tuple = [tuple(self.gen_vendedores_row().values()) for i in range(size)]
    columns = list(self.gen_vendedores_row().keys())
    return data_tuple, columns