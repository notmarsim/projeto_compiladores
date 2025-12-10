# semantic_analyzer.py

# Importa a classe base gerada pelo ANTLR
from FootprinterVisitor import FootprinterVisitor
from FootprinterParser import FootprinterParser

# --- Tipos que são permitidos em um loop FOR ---
# WORDLIST: É um tipo iterável (lista de palavras/caminhos).
# Você pode adicionar 'FUNCTION_RESULT' aqui se souber que a função retorna uma lista (ex: scan_tcp).
ITERABLE_TYPES = ['WORDLIST', 'FUNCTION_RESULT'] 

class SemanticAnalyzer(FootprinterVisitor):
    """
    Realiza a análise semântica na AST do Footprinter.
    As verificações incluem declaração dupla e uso de variáveis.
    """
    def __init__(self):
        # 1. Tabela de Símbolos
        # Armazena metadados das variáveis declaradas (nome, tipo, escopo, etc.)
        self.symbol_table = {}
        # Lista para coletar todos os erros encontrados
        self.semantic_errors = []
        print("Analisador Semântico Inicializado.")

    def has_errors(self):
        """Retorna True se algum erro semântico foi encontrado."""
        return len(self.semantic_errors) > 0

    def add_error(self, message, ctx):
        """Adiciona um erro semântico com a linha do código original."""
        line = ctx.start.line
        self.semantic_errors.append(f"[Linha {line}] Erro Semântico: {message}")
        
    # ===================================================================
    # 1. Implementação da Regra: Declaração de Variáveis (visitAssignStmt)
    #    (Mantida para REGISTRAR o tipo)
    # ===================================================================
    def visitAssignStmt(self, ctx: FootprinterParser.AssignStmtContext):
        
        # Obtém o nome da variável que está sendo declarada
        name = ctx.NAME(0).getText()
        
        # 1. VERIFICAÇÃO: A variável já existe na Tabela de Símbolos?
        if name in self.symbol_table:
            # ERRO SEMÂNTICO: Variável já declarada
            self.add_error(f"Variável '{name}' já foi declarada anteriormente.", ctx)
            
        else:
            # Se a variável é nova, a registramos na Tabela de Símbolos.
            var_type = 'UNKNOWN'
            if ctx.IP():
                var_type = 'IP'
            elif ctx.WORDLIST():
                var_type = 'WORDLIST'
            elif ctx.functionCall():
                var_type = 'FUNCTION_RESULT' 
                
            self.symbol_table[name] = {
                'tipo': var_type,
                'declarado': True
            }

        # Continua a visitar os filhos
        return self.visitChildren(ctx)

    # ===================================================================
    # 2. Implementação da Regra: Análise de Tipo em Iteração (visitForStmt)
    # ===================================================================

    def visitForStmt(self, ctx: FootprinterParser.ForStmtContext):
        # O nome da variável que está sendo iterada (ex: 'openports' ou 'tcp')
        listVar = ctx.NAME(1).getText()
        
        # 2.1. Verificação se a variável da lista (listVar) foi declarada
        if listVar not in self.symbol_table:
            # Erro de variável não declarada (já existia)
            self.add_error(f"Variável de lista '{listVar}' usada no FOR não foi declarada.", ctx)
        else:
            # 2.2. NOVO: Verificação de Tipo (A regra principal)
            var_info = self.symbol_table[listVar]
            var_type = var_info.get('tipo', 'UNKNOWN')

            if var_type not in ITERABLE_TYPES:
                # ERRO SEMÂNTICO: O tipo não é iterável
                self.add_error(
                    f"Variável '{listVar}' é do tipo '{var_type}', que não é iterável. Esperado: {ITERABLE_TYPES}.", 
                    ctx
                )
            # Se for um tipo iterável, não faz nada (SUCESSO)
            
        # Continua a visita nos filhos (o bloco de código dentro do for)
        return self.visitChildren(ctx)