from src.sucos_vendas_clientes import ClientesSucosVendas
from src.sucos_vendas_vendedores import VendedoresSucosVendas
from src.sucos_vendas_produtos import ProdutosSucosVendas
from src.sucos_vendas_notas_fiscais import NotasFiscaisSucosVendas
from src.sucos_vendas_itens_nota_fiscal import ItemsNotaFiscalSucosVendas

from src.utils import SQLParser

def write_file(file_name, data, mode='a'):
  with open(file_name, mode) as f:
    f.write(data)
    f.write("\n\n")

def main(num_vendedores, num_clientes, num_notas_fiscais, num_itens_nota_fiscal):


    sql_parser = SQLParser()
    vendedores = VendedoresSucosVendas()
    data_vendedores, columns_vendedores = vendedores.gen_vendedores(num_vendedores)
    query_insert_vendedores = sql_parser.create_insert_into('dadaia_sucos.vendedores', columns_vendedores, data_vendedores)
    write_file('queries/total_query.sql', query_insert_vendedores, 'w')

    produtos = ProdutosSucosVendas()
    data_produtos, columns_produtos = produtos.gen_produtos()
    query_insert_produtos = sql_parser.create_insert_into('dadaia_sucos.produtos', columns_produtos, data_produtos)
    write_file('queries/total_query.sql', query_insert_produtos)

    clientes = ClientesSucosVendas()
    data_clientes, columns_clientes = clientes.gen_clientes(num_clientes)
    query_insert_clientes = sql_parser.create_insert_into('dadaia_sucos.clientes', columns_clientes, data_clientes)
    write_file('queries/total_query.sql', query_insert_clientes)
    ids_clientes = [i for i in range(1, num_clientes)]
    ids_vendedores = [i for i in range(1, num_vendedores)]

    notas_fiscais = NotasFiscaisSucosVendas(ids_clientes, ids_vendedores)
    data_notas_fiscais, columns_notas_fiscais = notas_fiscais.gen_notas_fiscais(num_notas_fiscais)
    query_insert_notas_fiscais = sql_parser.create_insert_into('dadaia_sucos.notas_fiscais', columns_notas_fiscais, data_notas_fiscais)
    write_file('queries/total_query.sql', query_insert_notas_fiscais)

    ids_notas_fiscais = [i for i in range(1, num_notas_fiscais)]
    ids_produtos = [i for i in range(1, len(data_produtos))]
    items_nota_fiscal = ItemsNotaFiscalSucosVendas(ids_notas_fiscais, ids_produtos)
    data_items_nota_fiscal, columns_items_nota_fiscal = items_nota_fiscal.gen_items_notas_fiscais(num_itens_nota_fiscal)
    query_insert_items_nota_fiscal = sql_parser.create_insert_into('dadaia_sucos.itens_nota_fiscal', columns_items_nota_fiscal, data_items_nota_fiscal)
    write_file('queries/total_query.sql', query_insert_items_nota_fiscal)


if __name__ == '__main__':
  main(num_vendedores=5, num_clientes=600, num_notas_fiscais=50000, num_itens_nota_fiscal=150000)