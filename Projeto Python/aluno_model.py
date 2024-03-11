import uuid

class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.matricula = uuid.uuid4()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

if __name__ == "__main__":
    aluno = Aluno("Jp", 18, "ADS", 10)
    print(aluno.matricula, aluno.nome)