🕵️ Footprinter DSL

Footprinter é uma mini linguagem de domínio específico (DSL) escrita com ANTLR + Python, voltada para automatizar tarefas de pentest/footprinting de forma mais simples que um script Python convencional.

Atualmente a linguagem já suporta:

✔ Declaração de variáveis
✔ Atribuição de IP ou resultado de função
✔ Chamadas de funções com argumentos
✔ Laços for sobre listas retornadas por scan
✔ Blocos { ... }
✔ Estrutura condicional simples com case

📌 Como o código funciona hoje

Um script Footprinter é composto por statements. Cada statement pode ser:

Construção	Função
NAME : IP;	Cria variável contendo um endereço IP
NAME : functionCall;	Executa uma função e guarda o resultado
functionCall;	Executa uma função diretamente
for x in y { ... }	Itera sobre elementos de y
case NAME { ... }	Bloco condicional por serviço/tecnologia
{ ... }	Grupo de comandos

As funções sempre exigem argumentos, exemplo:

scan_tcp(host);
banner(port);
enum(port);

🔥 Exemplo de script válido
# Definir alvo
host: 127.0.0.1;

# Escaneamento
tcp: scan_tcp(host);
udp: scan_udp(host);

# Processar portas TCP
for port in tcp {
    banner(port);
    case web {
        enum(port);
    }
}

# Processar portas UDP
for port in udp {
    banner(port);
}


🚧 A implementar:

Executor/Visitor em Python

Integração com nmap/netcat/gobuster

Objetivo futuro: automatizar etapas comuns de enumeração

Objetivo da DSL

Permitir que um pentester escreva:

scan_tcp(host);

em vez de:

nmap -sV 127.0.0.1


ou scripts inteiros em Python.

A ideia final é transformar scripts repetitivos de footprinting em algo simples e declarativo.
