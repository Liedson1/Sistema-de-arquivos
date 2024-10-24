class Bloco:
    def __init__(self, caractere=None, proximo_bloco=None):
        self.caractere = caractere
        self.proximo_bloco = proximo_bloco

class Arquivo:
    def __init__(self, nome, tamanho, endereco):
        self.nome = nome
        self.tamanho = tamanho
        self.endereco = endereco

class Disco:
    def __init__(self):
        self.blocos = [Bloco() for _ in range(32)] 
        self.tabela_arquivos = []  
        self.ponteiro = None  

    def imprimir_disco(self):
        print("\nEstado Atual do Disco:")
        print("****************************************")
        print("Bloco    Caracter    Ponteiro")
        for i, bloco in enumerate(self.blocos):
            caractere = bloco.caractere if bloco.caractere is not None else "Vazio"
            proximo = bloco.proximo_bloco if bloco.proximo_bloco is not None else "None"
            print(f"  {i:<8}{caractere:<8}{proximo}")
        print("****************************************\n")

        print("Tabela de Arquivos:")
        print("****************************************")
        for arquivo in self.tabela_arquivos:
            print(f"{arquivo.nome} - Tamanho: {arquivo.tamanho}, Endereço: {arquivo.endereco}")
        print("****************************************\n")

    def obter_blocos_livres(self, tamanho):
        
        blocos_livres = [i for i, bloco in enumerate(self.blocos) if bloco.caractere is None]
        if len(blocos_livres) < tamanho:
            return None
        return blocos_livres[:tamanho]

    def criar_arquivo(self, nome, conteudo):
        tamanho = len(conteudo)  
        endereco = []

        blocos_livres = self.obter_blocos_livres(tamanho)  
        if blocos_livres is None:
            print("Erro: Espaço insuficiente no disco.")
            return

        for i, caractere in enumerate(conteudo):
            bloco_atual = blocos_livres[i]
            self.blocos[bloco_atual].caractere = caractere
            endereco.append(bloco_atual)
            if i > 0:
                self.blocos[endereco[i-1]].proximo_bloco = bloco_atual

        self.tabela_arquivos.append(Arquivo(nome, tamanho, endereco))
        print(f"Arquivo '{nome}' criado com sucesso.")
        self.imprimir_disco()

    def excluir_arquivo(self, nome):
        for arquivo in self.tabela_arquivos:
            if arquivo.nome == nome:
                self.ponteiro = arquivo.endereco[0]  
                while self.ponteiro is not None:
                    proximo_bloco = self.blocos[self.ponteiro].proximo_bloco
                    self.blocos[self.ponteiro] = Bloco()  
                    self.ponteiro = proximo_bloco  

                self.tabela_arquivos.remove(arquivo)
                print(f"Arquivo '{nome}' removido com sucesso.")
                self.imprimir_disco()
                return
        print(f"Erro: Arquivo '{nome}' não encontrado.")

    def ler_arquivo(self, nome):
        for arquivo in self.tabela_arquivos:
            if arquivo.nome == nome:
                print(f"Lendo arquivo '{nome}':")
                conteudo = ""
                self.ponteiro = arquivo.endereco[0]  
                while self.ponteiro is not None:
                    conteudo += self.blocos[self.ponteiro].caractere  
                    self.ponteiro = self.blocos[self.ponteiro].proximo_bloco  
                print(f"Conteúdo armazenado: {conteudo}")
                return
        print(f"Erro: Arquivo '{nome}' não encontrado.")


def menu():
    disco = Disco()

    while True:
        print("\n----- Menu -----")
        print("1. Criar arquivo")
        print("2. Exibir estado do disco")
        print("3. Excluir arquivo")
        print("4. Ler arquivo")
        print("5. Sair")
        print("\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do arquivo: ")
            conteudo = input("Conteúdo do arquivo: ")
            disco.criar_arquivo(nome, conteudo)
        elif opcao == "2":
            disco.imprimir_disco()
        elif opcao == "3":
            nome = input("Nome do arquivo a ser excluído: ")
            disco.excluir_arquivo(nome)
        elif opcao == "4":
            nome = input("Nome do arquivo a ser lido: ")
            disco.ler_arquivo(nome)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
