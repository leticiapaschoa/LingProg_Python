# LingProg_Python
Aula Linguagem de Programação

# AULA 03 - Sintaxe e Semântica
# Palavras Reservadas:
Python tem aproximadamente 30 palavras reservadas, dentre elas, temos como principais:
and, as, assert, async, await, break, class, continue, def,	del, elif, else, except, finally,	for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield, True, False, None.

# Tipos de Dados:
Números:	int, long, float, complex
Strings:	str e unicode
Listas e tuplas:	list, tuple
Dicionários:	dict
Arquivos:	file
Booleanos:	bool (True, False)
Conjuntos:	set, frozenset
Null:	none
  > Em Python, None equivale ao valor nulo null.
  
# Sintaxe:
Operadores Aritméticos:
Subtração (-), multiplicação (*), divisão (/), potenciação (**) 

Operadores Com Strings:
Concatenar strings (+), Multiplicar strings para formar uma string com uma sequência repetida (*)

Operadores Lógico:
And, Or, Not

Comandos que aceitam blocos:
if/elif/else
for/else
while/else
def
try/except /finally/else
class
with

#Semântica:
 - Uma variável não pode ser utilizada em uma expressão sem ter sido inicializada
 - Python usa indentação como delimitação de bloco
 - Dois-pontos marca o início do bloco

#Links:
https://aprendendo-computacao-com-python.readthedocs.io/en/latest/capitulo_02.html#operadores-e-operandos
http://www.devfuria.com.br/python/sintaxe-basica/#sa-das
https://www.learnpython.org/pt/Operadores_b%C3%A1sicos


# AULA 04 - HELLO WORLD
# Versões Python:
- Versão 2
- Versão 3

# Mudanças entre as versões:
- O print() passou a ser uma função a partir da versão 3
- O construtor file usado para abrir arquivos foi removido na versão 3, restando como melhor opção a função open()
- Na versão 2 os sinais == e != não eram opostos. Isso foi corrigido na versão 3
- A partir da versão 3 o tipo int passou a ser ilimitado quanto a quantidade de digitos.
- Na versão 2 o tipo padrão string não suportava caracteres não-ASCII e não havia um tipo próprio para armazenamento de bytes. Isso foi ajustado na versão seguinte.

# Ferramentas de Desenvolvimento:
- Atom
- Visual Studio Code
- NetBeans
- Komodo

# Estrutura básica do programa:
- Entrada de dados: funções raw_input e input
- Comandos de Decisão: 
    if  CONDIÇÃO :
      BLOCO DE CÓDIGO
- Laços de Reptição:
  for VARIAVEL in CONJUNTO:
    COMANDO

  while VERDADEIRO:       
    COMANDO
  
- Função: sintaxe inicia-se com a palavra def, seguida do nome da função e dos parênteses que podem conter seus parâmetros

# Link:
http://blog.caelum.com.br/quais-as-diferencas-entre-python-2-e-python-3/
https://www.devmedia.com.br/python-tutorial/33274


# AULA 05 - Técnicas de Programação 01
#Tipos de Dados e Variáveis:

-Tipo Primitivo Simples:
  - Números: 
            Int -> não tem um valor máximo como limite;
            Exemplo: x = 1
                     y = 35656222554887711
                     z = -3255522

             Float -> números com uma ou mais decimais;
             Exemplo: x = 1.10
                      y = 1.0
                      z = -35.59

             Complex -> números com uma parte imaginária;
             Exemplo: x = 3+5j
                      y = 5j
                      z = -5j

  - Cadeia de caracteres: 
              String -> cadeira de caracteres individuais em uma string podem ser acessados ​​especificando o nome da string seguido por um número entre colchetes ( []).
              Exemplo:
              A L I C E
              0 1 2 3 4

-Tipo Primitivo Composto:
Tipos Primitivos Compostos:
* Lista:
	- Uma coleção ordenada de dados que podem ser modificados.
	- Exem.: Lista de alunos por ordem alfabética.
	
	lista = ["alice", "leticia"]
	
	* Set:
	- Uma coleção não ordenada de dados
	- Exem.: Uma coleção de linguagens de programação
	
	set = {"python", "java", ".net"}

* Dicionário:
	- Uma coleção não ordenada de dados que podem modificados.
	- Exem.: Armazenar um conjunto de configrações com chave e valor
	
	dicionario = 	{
						"linguagem": "python",
						"versao": "3.7"						
					}

* Tupla:
	- Uma coleção ordenada de dados que não podem ser modificados
	- Exem.: Armazenar um conjuno de versões compatíveis do python.
	tupla = (2.7, 3.7)