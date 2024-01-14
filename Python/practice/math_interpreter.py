from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
	NUMBER    = 0
	PLUS      = 1
	MINUS     = 2
	MULTIPLY  = 3
	DIVIDE    = 4
	LPAREN    = 5
	RPAREN    = 6
	POW       = 7

@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '^':
				self.advance()
				yield Token(TokenType.POW)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			else:
				raise Exception(f"Illegal character '{self.current_char}'")

	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'
 
		return Token(TokenType.NUMBER, float(number_str))

@dataclass
class NumberNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"

@dataclass
class PowNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}^{self.node_b})"

@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"


class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise Exception("Invalid syntax")
	
	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		if self.current_token == None:
			return None

		result = self.expr()

		if self.current_token != None:
			self.raise_error()

		return result

	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubtractNode(result, self.term())

		return result

	def term(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.POW):
			if self.current_token.type == TokenType.MULTIPLY:
				self.advance()
				result = MultiplyNode(result, self.factor())
			elif self.current_token.type == TokenType.DIVIDE:
				self.advance()
				result = DivideNode(result, self.factor())
			elif self.current_token.type == TokenType.POW:
				self.advance()
				result = PowNode(result, self.factor())
				
		return result

	def factor(self):
		token = self.current_token

		if token.type == TokenType.LPAREN:
			self.advance()
			result = self.expr()

			if self.current_token.type != TokenType.RPAREN:
				self.raise_error()
			
			self.advance()
			return result

		elif token.type == TokenType.NUMBER:
			self.advance()
			return NumberNode(token.value)

		elif token.type == TokenType.PLUS:
			self.advance()
			return PlusNode(self.factor())
		
		elif token.type == TokenType.MINUS:
			self.advance()
			return MinusNode(self.factor())
		
		self.raise_error()

@dataclass
class Number:
	value: any
	
	def __repr__(self):
		return f"{self.value}"

class Interpreter:
	def __init__(self):
		pass

	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)
		
	def visit_NumberNode(self, node):
		return Number(node.value)

	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
	
	def visit_PowNode(self, node):
		return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			raise Exception("Runtime math error")

while True:
	try:
		text = input("calc > ")
		lexer = Lexer(text)
		tokens = lexer.generate_tokens()
		parser = Parser(tokens)
		tree = parser.parse()
		if not tree:
			 continue
		interpreter = Interpreter()
		value = interpreter.visit(tree)
		print(">>>", value)
	except Exception as e:
		print(e)
