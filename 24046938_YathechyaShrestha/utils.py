# Aligns text by adding spaces to the right to reach a specified length for consistent formatting
def pad_right(text, length):
    text = str(text)
    while len(text) < length:
        text = text + ' '
    return text

# Aligns text by adding spaces to the left to reach a specified length for consistent formatting
def pad_left(text, length):
    text = str(text)
    while len(text) < length:
        text = ' ' + text
    return text