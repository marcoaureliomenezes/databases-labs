from src.utils import RandomCommonValuesGenerator
from random import randint


class NotasFiscaisSucosVendas:

  def __init__(self, clientes, vendedores):
    self.rand_generator = RandomCommonValuesGenerator()
    self.cliente_range = (min(clientes), max(clientes))
    self.vendedor_range = (min(clientes), max(vendedores))
    self.admissao_range = ('2010-01-01', '2024-01-01')
    self.imposto = [0.03, 0.05, 0.07]

  def gen_nota_fiscal_row(self):
    return dict(
      cliente_id = randint(*self.vendedor_range),
      vendedor_id = randint(*self.vendedor_range),
      data_venda = self.rand_generator.gen_obj.gen_date(*self.admissao_range),
      imposto = self.rand_generator.gen_obj.gen_fake_distinct(self.imposto)
    )  

  def gen_notas_fiscais(self, size=10):
    data_tuple = [tuple(self.gen_nota_fiscal_row().values()) for i in range(size)]
    columns = list(self.gen_nota_fiscal_row().keys())
    return data_tuple, columns