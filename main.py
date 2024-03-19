from database import Database
from produtos import produtos

db = Database(database="mercado", collection="compras")

p =produtos(db)


ip=p.cliente_que_mais_gastou()

p.produto_mais_vendido()

p.produtos_com_quantidade_acima_de_um()

p.total_vendas_por_dia()