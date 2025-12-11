# 🕵️ Footprinter DSL

Uma Domain-Specific Language minimalista voltada para automação de tarefas de segurança ofensiva (port-scanning, banner-grabbing, enumeração, etc.).  
Este projeto inclui:

- Lexer e Parser escritos com **ANTLR4**
- Interpretador em **Python** aplicando a parse tree
- Funções extensíveis para operações de segurança
- Sintaxe simples e flexível, parecida com pseudo-código

---

## 📌 Objetivo

O Footprinter tem o objetivo de permitir que usuários escrevam pequenos scripts de automação ofensiva usando uma linguagem simples que:

- define hosts  
- executa varreduras  
- itera sobre portas abertas  
- aplica condições e blocos  
- chama funções Python como se fossem comandos nativos  

**Exemplo:**

```
host: 10.10.10.1;
openports: scan_tcp(host);

for p in openports {
    banner(p);
    case (p == 80) {
        enum(p);
    }
}
```
---

## Como funciona
O projeto divide-se em três partes:

### 1. Lexer (FootprinterLexer.g4)
Define os tokens da linguagem:

NAME, IP, NUMBER

WORDLIST no formato /path/to/file-list.txt

Operadores ==, !=, in

Blocos { }

Listas [1,2,3]

### 2. Parser (FootprinterParser.g4)
Define a gramática:

comandos

atribuições

laços for

condições case

funções com argumentos

listas de IPs, números ou wordlists

### 3. Interpretador em Python
Arquivo principal:
```
def eval_node(t):
    match t:
        case FootprinterParser.ProgramContext(): ...
        case FootprinterParser.AssignStmtContext(): ...
        case FootprinterParser.ForStmtContext(): ...
        case FootprinterParser.CaseStmtContext(): ...
        case FootprinterParser.FunctionCallContext(): ...
```
O interpretador percorre a parse tree e executa:

atribuições → mem[var] = valor

chamadas de função → usa funções importadas de modules.py

loops → for x in lista

blocos condicionais → case (...)

listas e wordlists

---
## 📁 Estrutura do Projeto

```
Footprinter/
│
├── FootprinterLexer.g4
├── FootprinterParser.g4
├── FootprinterLexer.py      (gerado pelo ANTLR)
├── FootprinterParser.py     (gerado pelo ANTLR)
│
├── interpreter.py           (eval_node + run)
├── modules.py               (funções chamadas pela DSL)
│
├── examples/
│   └── teste.ft
│
└── README.md
```
---

## 📝 Exemplo de Script (teste.ft)
```
host: [10.129.108.250];
wordlist : /usr/share/SecLists/Discovery/Web-Content/common.txt;
openports: scan_tcp(host);
webPort: [80,443];

for port in openports {
    banner(port);
    case (port in webPort){
        enum(port,wordlist);
    }
}
```
O que este script faz:

Define o host alvo

Define uma wordlist

Escaneia portas → scan_tcp

Itera por cada porta aberta

Executa banner(port)

Se a porta estiver em [80,443], executa enum(port, wordlist)

---
## ▶️ Como executar
1. Instale o ANTLR4
```
pip install antlr4-tools
```
2. Gere o lexer e parser
```
antlr4 -Dlanguage=Python3 Footprinter.g4
```
3. Execute um script .ft
```
from interpreter import run

run(open("examples/teste.ft").read())
```
