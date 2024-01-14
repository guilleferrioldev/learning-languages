import ast
import operator

# Definir una clase visitante del AST
class MathEvaluator(ast.NodeVisitor):
    def visit_BinOp(self, node):
        # Evaluar el operador izquierdo y derecho
        left_value = self.visit(node.left)
        right_value = self.visit(node.right)

        # Obtener el operador correspondiente al nodo
        op = self.get_operator(node.op)

        # Aplicar la operación y devolver el resultado
        return op(left_value, right_value)

    def visit_Num(self, node):
        # Devolver el valor numérico
        return node.n

    def get_operator(self, op_node):
        # Mapear el operador del AST a una función en Python
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg, 
            ast.Pow: operator.pow
        }
        return operators[type(op_node)]


# Función para evaluar una expresión matemática
def evaluate_expression(expression):
    # Analizar la expresión en un AST
    tree = ast.parse(expression, mode='eval')

    # Crear una instancia del evaluador
    evaluator = MathEvaluator()

    # Evaluar el AST y obtener el resultado
    result = evaluator.visit(tree.body)

    # Devolver el resultado
    return result


# Ejemplo de uso
expression = "4 + 2 * 3"
result = evaluate_expression(expression)
print(f"El resultado de la expresión '{expression}' es: {result}")


