from datetime import date
from faculdade.enum import Curso, LinhaPesquisa

class Aluno:
    def __init__(self, matricula: int, nome: str, data_nascimento: date):
        self.matricula = matricula
        self.nome = nome
        self.data_nascimento = data_nascimento

class AlunoGraduacao(Aluno):
    def __init__(self, matricula: int, nome: str, data_nascimento: date, curso: Curso):
        super().__init__(matricula, nome, data_nascimento)
        self.curso = curso

    def calcular_mensalidade(self):
        return self.curso.value

class AlunoPosGraduacao(Aluno):
    def __init__(self, matricula: int, nome: str, data_nascimento: date, 
                 linha_pesquisa: LinhaPesquisa, orientador: str, bolsa: float):
        super().__init__(matricula, nome, data_nascimento)
        self.linha_pesquisa = linha_pesquisa
        self.orientador = orientador
        self.bolsa = bolsa  # Ex: 15.0 para 15%

    def calcular_mensalidade(self):
        valor_base = self.linha_pesquisa.value
        return valor_base * (1 - self.bolsa / 100)