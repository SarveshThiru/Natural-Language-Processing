def recognize_ab(input_string):

    state = 0  # Initial state

    for char in input_string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 0

    return state == 2

# Test cases
input_strings = ["ab", "aba", "abb", "ba", "abab"]

for input_string in input_strings:
    if recognize_ab(input_string):
        print(f"'{input_string}' is accepted.")
    else:
        print(f"'{input_string}' is rejected.")
