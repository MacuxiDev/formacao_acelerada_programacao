from datetime import date
from faculdade.aluno import AlunoGraduacao, AlunoPosGraduacao
from faculdade.enum import Curso, LinhaPesquisa

def main() -> None:
    # Criando um aluno de Graduação
    aluno_grad = AlunoGraduacao(
        101, "Alice Souza", date(2002, 5, 15), Curso.CIENCIADACOMPUTACAO
    )

    # Criando um aluno de Pós-Graduação (com 15% de bolsa)
    aluno_pos = AlunoPosGraduacao(
        202, "Bruno Silva", date(1995, 10, 20), 
        LinhaPesquisa.INOVACAO_TECNOLOGICA, "Dr. Einstein", 15.0
    )

    print(f"\n--- Relatório de Mensalidades (Sabe Tudo) ---")
    print(f"Aluno: {aluno_grad.nome}")
    print(f"Curso: {aluno_grad.curso.name}")
    print(f"Mensalidade: R$ {aluno_grad.calcular_mensalidade():.2f}")
    
    print("-" * 40)
    
    print(f"Aluno: {aluno_pos.nome}")
    print(f"Linha de Pesquisa: {aluno_pos.linha_pesquisa.name}")
    print(f"Orientador: {aluno_pos.orientador}")
    print(f"Bolsa: {aluno_pos.bolsa}%")
    print(f"Mensalidade Final: R$ {aluno_pos.calcular_mensalidade():.2f}\n")

if __name__ == "__main__":
    main()

    