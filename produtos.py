from helper.jason import jason

class Product_analyzer:
    def __init__(self, db):
        self.database = db

    def total_vendas_por_dia(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra","total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}   
        ])
        jason(result, "Total de vendas por dia")

    def produto_mais_vendido(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendas": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendas": -1}},
            {"$limit": 1},
            {"$project": {"_id": 0, "produto_mais_vendido": "$_id", "total_vendas": 1}}
        ])
        jason(result, "Produto mais vendido de todas as compras")

    def cliente_que_mais_gastou(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        jason(result, "Cliente que mais gastou em uma compra")

    def produtos_com_quantidade_acima_de_um(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao"}}
        ])
      jason(result, "Produtos com quantidade vendida superior a um")
