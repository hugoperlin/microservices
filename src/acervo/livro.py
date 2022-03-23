from enum import Enum

class Categoria(Enum):
    FICCAO = 1
    LITERATURA = 2
    TECNICO = 3

class Livro:

    def fromJson(titulo,anoPublicacao,categoria):
        return Livro(titulo,anoPublicacao,categoria)

    def __init__(self,titulo,anoPublicacao,categoria):
        self.titulo = titulo
        self.anoPublicacao = anoPublicacao
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.titulo}({self.anoPublicacao})"

    def toJson(self):
        return {"titulo":self.titulo,"ano_publicacao":self.anoPublicacao,"categoria":self.categoria}
    
