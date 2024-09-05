def pluralize(word):
    state = 0
    plural_form = ""

    for char in word:
        if state == 0:
            state = 1
            plural_form += char
        elif state == 1:
            if char in ['s', 'sh', 'ch', 'x', 'z']:
                plural_form += "es"
                state = 2
            else:
                plural_form += "s"
                state = 2

    return plural_form

# Test cases
words = ["cat", "bus", "box", "child", "man"]

for word in words:
    plural = pluralize(word)
    print(f"{word} -> {plural}")
