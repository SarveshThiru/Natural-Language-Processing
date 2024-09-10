from collections import defaultdict

class State:
    """Represents a state in the Earley parsing chart."""
    def __init__(self, rule, dot, start, end):
        self.rule = rule  # Grammar rule (LHS, RHS)
        self.dot = dot  # Position of dot in RHS
        self.start = start  # Start position in input
        self.end = end  # Current position in input

    def next_symbol(self):
        """Returns the next symbol to be matched, if any."""
        if self.dot < len(self.rule[1]):
            return self.rule[1][self.dot]
        return None

    def is_complete(self):
        """Checks if the state is complete (dot at end of RHS)."""
        return self.dot >= len(self.rule[1])

    def __repr__(self):
        return f"{self.rule[0]} -> {''.join(self.rule[1][:self.dot])}.{''.join(self.rule[1][self.dot:])} ({self.start}, {self.end})"

class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar  # CFG as a dictionary
        self.chart = []

    def parse(self, input_string):
        """Parses an input string using the Earley parsing algorithm."""
        tokens = input_string.split()
        self.chart = [set() for _ in range(len(tokens) + 1)]
        # Start state
        self.chart[0].add(State(("S'", ["S"]), 0, 0, 0))

        for i in range(len(tokens) + 1):
            for state in list(self.chart[i]):
                if not state.is_complete():
                    next_symbol = state.next_symbol()
                    if next_symbol in self.grammar:  # Prediction step
                        self.predict(state, i)
                    elif i < len(tokens) and next_symbol == tokens[i]:  # Scanning step
                        self.scan(state, i, tokens)
                else:  # Completion step
                    self.complete(state, i)

        # Check if final state is in the chart
        final_state = State(("S'", ["S"]), 1, 0, len(tokens))
        return final_state in self.chart[-1]

    def predict(self, state, index):
        """Performs the prediction step."""
        next_symbol = state.next_symbol()
        for production in self.grammar.get(next_symbol, []):
            new_state = State((next_symbol, production), 0, index, index)
            self.chart[index].add(new_state)

    def scan(self, state, index, tokens):
        """Performs the scanning step."""
        next_symbol = state.next_symbol()
        if index < len(tokens) and next_symbol == tokens[index]:
            new_state = State(state.rule, state.dot + 1, state.start, index + 1)
            self.chart[index + 1].add(new_state)

    def complete(self, state, index):
        """Performs the completion step."""
        for prev_state in self.chart[state.start]:
            if not prev_state.is_complete() and prev_state.next_symbol() == state.rule[0]:
                new_state = State(prev_state.rule, prev_state.dot + 1, prev_state.start, index)
                self.chart[index].add(new_state)

if __name__ == "__main__":
    # Define the grammar for the parser
    grammar = {
        "S": [["NP", "VP"]],
        "NP": [["cat"], ["dog"]],
        "VP": [["V", "NP"]],
        "V": [["chases"]],
    }

    parser = EarleyParser(grammar)
    input_string = "cat chases dog"
    result = parser.parse(input_string)
    print(f"Input '{input_string}' is {'accepted' if result else 'rejected'} by the grammar.")
