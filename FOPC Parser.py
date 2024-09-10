from pyparsing import Word, alphanums, oneOf, infixNotation, opAssoc, Forward, ParseException
variable = Word(alphanums)
predicate = Word(alphanums)
quantifier = oneOf("forall exists")
expression = Forward()
unary_operators = oneOf("not ¬")
quantifier_operators = oneOf("forall exists")

atom = variable | predicate

expression << (
    (quantifier + variable + "(" + expression + ")") |
    (unary_operators + expression) |
    atom
)
def parse_fopc(expression_str):
    try:
        result = expression.parseString(expression_str, parseAll=True)
        return result[0]
    except ParseException as e:
        print(f"Error parsing expression: {e}")
        return None
expression1 = "forall x (P(x) -> Q(x))"
expression2 = "exists y (P(y) & Q(y))"

parsed_expression1 = parse_fopc(expression1)
parsed_expression2 = parse_fopc(expression2)

print("Parsed Expression 1:", parsed_expression1)
print("Parsed Expression 2:", parsed_expression2)
