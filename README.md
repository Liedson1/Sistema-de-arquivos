
# Sistema de Gerenciamento de Arquivos Simulado

## Descrição

Este projeto implementa um **sistema de gerenciamento de arquivos** em um disco simulado, utilizando uma estratégia de **alocação encadeada de blocos de memória**. Ele permite a criação, leitura, exclusão e visualização do estado de um "disco" com 32 blocos de memória. Cada arquivo criado no sistema é armazenado em blocos de forma sequencial, e a exclusão de arquivos libera os blocos para futuras operações.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:
- **Criar Arquivo**: Armazena um arquivo no disco utilizando blocos de memória.
- **Ler Arquivo**: Lê e exibe o conteúdo de um arquivo previamente armazenado.
- **Excluir Arquivo**: Remove um arquivo e libera seus blocos de memória para uso futuro.
- **Exibir Estado do Disco**: Mostra o estado atual do disco, listando os blocos, os arquivos armazenados e seus tamanhos.

## Finalidade

Este projeto foi criado para fins **educacionais** e para demonstrar o funcionamento de um sistema de arquivos básico, onde se utiliza **alocação encadeada de blocos**. É ideal para estudantes que desejam entender o gerenciamento de memória em sistemas de arquivos, além de ser útil como base para expandir em outros conceitos, como **gerenciamento de disco**, **sistemas operacionais** e **alocação de memória**.

## Como Funciona

1. O disco possui 32 blocos de memória. Cada caractere de um arquivo ocupa um bloco.
2. Quando um arquivo é criado, o sistema procura blocos livres suficientes e armazena o conteúdo do arquivo nesses blocos.
3. Cada bloco pode apontar para o próximo bloco que contém a continuação do arquivo, criando uma estrutura encadeada.
4. A leitura de um arquivo percorre os blocos encadeados, e a exclusão de um arquivo libera todos os blocos que estavam sendo utilizados por ele.

## Como Usar

### Pré-requisitos

- **Python 3.6+** instalado no seu sistema.

### Instruções de Uso

1. Clone este repositório ou faça o download do arquivo `so_menu (testado2.0).py`.
2. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo está salvo.
3. Execute o seguinte comando:

   ```bash
   python so_menu\ \(testado2.0\).py
   ```

4. O menu interativo será exibido com as seguintes opções:

   ```
   ----- Menu -----
   1. Criar arquivo
   2. Exibir estado do disco
   3. Excluir arquivo
   4. Ler arquivo
   5. Sair
   ```

### Exemplos de Uso

#### 1. Criar um arquivo:
- Escolha a opção `1` no menu para criar um arquivo.
- Insira o nome do arquivo e o conteúdo que deseja armazenar.
- O sistema irá verificar se há blocos suficientes no disco para armazenar o conteúdo e, caso haja, o arquivo será criado.

#### 2. Ler um arquivo:
- Escolha a opção `4` para ler o conteúdo de um arquivo existente.
- Insira o nome do arquivo que deseja ler. O conteúdo será exibido se o arquivo estiver presente no disco.

#### 3. Excluir um arquivo:
- Escolha a opção `3` para excluir um arquivo.
- Insira o nome do arquivo que deseja excluir. O arquivo será removido do disco e os blocos de memória que ele ocupava serão liberados.

#### 4. Exibir o estado do disco:
- Escolha a opção `2` para exibir o estado atual do disco.
- Será exibida uma tabela mostrando os blocos, seus conteúdos e os ponteiros para os próximos blocos, além de uma lista dos arquivos armazenados e suas informações.

### Estrutura do Projeto

O projeto possui a seguinte estrutura:

- **Bloco**: Representa um bloco de memória do disco. Cada bloco armazena um caractere e um ponteiro para o próximo bloco (encadeamento).
- **Arquivo**: Armazena as informações do arquivo (nome, tamanho e endereço dos blocos).
- **Disco**: Gerencia os blocos e os arquivos, e implementa as operações principais como criação, exclusão e leitura de arquivos.
- **Menu Interativo**: Interface de texto que permite o usuário interagir com o sistema através do terminal.

## Exemplos de Saída

### Estado do Disco

Após criar alguns arquivos, o estado do disco pode ser exibido assim:

```
Estado do Disco:
****************************************
Bloco    Caracter    Ponteiro
  0      H          1
  1      e          2
  2      l          3
  3      l          4
  4      o          None
  5      Vazio      None
  ...
****************************************

Tabela de Arquivos:
****************************************
arquivo1.txt - Tamanho: 5, Endereço: [0, 1, 2, 3, 4]
****************************************
```

### Leitura de Arquivo

Ao ler um arquivo:

```
Lendo arquivo 'arquivo1.txt':
Conteúdo armazenado: Hello
```

### Exclusão de Arquivo

Após excluir um arquivo, os blocos são liberados:

```
Arquivo 'arquivo1.txt' removido com sucesso.
```

### Erro ao Criar Arquivo

Caso não haja blocos suficientes para criar um novo arquivo:

```
Erro: Espaço insuficiente no disco.
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_ com melhorias.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
