from random import randint
from src.utils import RandomCommonValuesGenerator

class ProdutosSucosVendas:

  def __init__(self):
    self.rand_generator = RandomCommonValuesGenerator()
    self.nomes = ['Videira do Campo', 'Dolly', 'Del Rei']
    self.sabores = ['uva', 'limão', 'maçã', 'laranja', 'cereja']
    self.recipientes = ['lata', 'garrafa plastica', 'garrafa vidro']
    self.columns_produto = ['nome', 'sabor', 'tamanho', 'embalagem', 'preco_de_lista']

  def gen_price(self, min, max):
    return randint(min * 100, max * 100) / 100

  def gen_lata_products(self):
    tamanhos_lata = ['350 ml']
    return [(nome, sabor, tamanho, 'lata', self.gen_price(4.0, 7.0)) for sabor in self.sabores for nome in self.nomes for tamanho in tamanhos_lata]

  def gen_vidro_products(self):
    tamanhos_vidro = ['275 ml' ,'1 litro']
    return [(nome, sabor, tamanho, 'lata', self.gen_price(3.0, 7.0)) for sabor in self.sabores for nome in self.nomes for tamanho in tamanhos_vidro]

  def gen_plastico_products(self):
    tamanhos_pet = ['350 ml' ,'600 ml', '2 litros', '2,5 litros']
    return [(nome, sabor, tamanho, 'lata', self.gen_price(7.0, 15.0)) for sabor in self.sabores for nome in self.nomes for tamanho in tamanhos_pet]
   
  def gen_produtos(self, size=None):
    gen_id = lambda x: x
    data = self.gen_lata_products() + self.gen_vidro_products() + self.gen_vidro_products()
    size = len(data) if size is None else size
    data = data[:size]
    return data, self.columns_produto
  
