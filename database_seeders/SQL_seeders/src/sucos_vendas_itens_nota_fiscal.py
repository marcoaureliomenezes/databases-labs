from src.utils import RandomCommonValuesGenerator
from random import randint

class ItemsNotaFiscalSucosVendas:

  def __init__(self, notas_fiscais_ids, products_ids):
    self.rand_generator = RandomCommonValuesGenerator()
    self.notas_fiscais_range = (min(notas_fiscais_ids), max(notas_fiscais_ids))
    self.produtos_range = (min(products_ids), max(products_ids))
  

  def gen_item_nota_fiscal_row(self):
    return dict(
      produto_id = randint(*self.produtos_range),
      nota_fiscal_id = randint(*self.notas_fiscais_range),
      quantidade = randint(1, 4)
    )

  def gen_items_notas_fiscais(self, size=10):
    data_tuple = [tuple(self.gen_item_nota_fiscal_row().values()) for i in range(size)]
    columns = list(self.gen_item_nota_fiscal_row().keys())
    return data_tuple, columns