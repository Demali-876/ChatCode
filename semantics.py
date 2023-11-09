from CCparse import parser
from lark import Transformer, v_args, Token

class SemanticError(Exception):
    def __init__(self, message, token=None):
        self.message = message
        self.line = token.line if token else None
        self.column = token.column if token else None
        super().__init__(self.message)

    def __str__(self):
        return f"Semantic Error at line {self.line}, column {self.column}: {self.message}"

class SemanticAnalyzer(Transformer):
    def __init__(self):
        super().__init__()
        self.symbol_table = {}  # Start with an empty symbol table
        self.scope_stack = [{}]
        self.functions = {}
        self.contracts = {}
        self.reserved_keywords = set()
        self.loop_contexts = []
        self.return_contexts = []
        self.current_scope = None
        self.current_contract = None
        self.errors = []

    def _add_error(self, message, token=None):
        self.errors.append(SemanticError(message, token))

    # ... rest of the methods ...

    def get_errors(self):
        return self.errors


def analyze(ast):
    analyzer = SemanticAnalyzer()
    analyzer.transform(ast)
    return analyzer

def walk_tree(tree):
    print(tree.data)  # Print the rule name
    for child in tree.children:
        if isinstance(child, Token):
            print(f"Leaf: {child.type}: {child.value}")
        else:
            walk_tree(child)


with open('source_code.cc', 'r') as source_file:
    source_code = source_file.read()

ast = parser.parse(source_code)
semantic_analysis_result = analyze(ast)

if semantic_analysis_result.get_errors():
    for error in semantic_analysis_result.get_errors():
        print(error)
else:
    # If no errors, continue with the compilation or interpretation
    pass
print(ast.pretty())