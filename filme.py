from dataclasses import dataclass
from dataclasses import field
from operator import attrgetter
from generos import  Genero

@dataclass
class Filme:
    titulo: str
    diretor: str
    ano: int
    imdb_rating: float
    visto: bool = False
    generos: list[Genero] = field(default_factory=list)


    def __post_init__(self):
        if self.ano < 1985:
            print("O ano de lancamento do filme deve ser maior ou igual a 1985.")

    def adicionando_genero(self, genero: Genero):
        if genero not in self.generos:
            self.generos.append(genero)
            print(f"genero '{genero.name}' adicionando ao filme '{self.titulo}'") 


#----------test----------

if __name__ == "__main__":
    filme1 = Filme(" A voltas dos que nao foram","Lucas Guerra", 1972, 9.2)
    filme1.adicionando_genero(Genero.POLICIAL)
    print(filme1)
    filme2 = Filme(" A voltas dos que nao foram 2","Lucas Guerra", 1800, 7.2)
    filme2.adicionando_genero(Genero.DRAMA)
    print(filme2)
    filme3 = Filme(" A voltas dos que nao foram 3","Lucas Guerra", 1972, 6.2)
    filme2.adicionando_genero(Genero.DRAMA)
    print(filme3)
