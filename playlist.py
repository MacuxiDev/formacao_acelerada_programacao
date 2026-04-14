from dataclasses import dataclass, field
# Assumindo que a classe Filme existe no arquivo filme.py
# from filme import Filme 

@dataclass
class Playlist:
    nome: str
    descricao: str
    filmes: list['Filme'] = field(default_factory=list)

    def adicionar_filme(self, filme: 'Filme'):
        self.filmes.append(filme)
        print(f"'{filme.titulo}' adicionado com sucesso!")

    def remover_filme(self, titulo: str):
        
        if filme:
            self.filmes.remove(filme)
            print(f"'{titulo}' removido da playlist '{self.nome}'.")
        else:
            print(f"O filme '{titulo}' não foi encontrado na playlist.")

# --- Exemplo de Uso (Simulado) ---
# p = Playlist("Sci-Fi Clássicos", "Melhores filmes")
# f1 = Filme("Matrix", "Wachowski", 1999)
# p.adicionar_filme(f1)
# p.remover_filme("Matrix")
