import re

# Define the text to be searched
text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern (e.g., words starting with 'q')
pattern = r"\b[q]\w+"
matches = re.findall(pattern, text)

# Print the matches
print("Matches:", matches)

# Replace the pattern with something else
new_text = re.sub(pattern, "X", text)
print("New text:", new_text)
