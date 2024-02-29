from mercado import bancodedados

class Marcas():
    id = 0
    marca = ""
    
    def get_first(marca):
      sql = "select * from marcas where nome = '" + marca + "'"
      resultado = bancodedados.get_sql(sql)
      if(resultado):
        return [True, resultado[0]]
      else:
        return [False, ""]
      
    def inserir(marca, apelido):   
      sql = """INSERT INTO marcas(nome, apelido) VALUES (%s, %s)"""
      val = (marca,  apelido)
      bancodedados.inserir_sql(sql, val)
