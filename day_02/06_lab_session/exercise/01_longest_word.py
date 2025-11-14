fox = "The quick brown fox jumps"
python = "I love programming in Python!"

def get_longest_word(text):
    """TODO: Add decoding process"""
    words = text.split()
    longest_word = None

# quick1 = quick.split()
# prog1 = programming.split()
# print(quick1)
# print(prog1)
    for word in words:
        if longest_word is None or len(word) > len(longest_word):
            longest_word = word
    return longest_word

# # "The quick brown fox jumps" -> "quick"
print(f"The longest word is: {get_longest_word(fox)}")


# # "I love programming in Python!" -> "programming"

print(f"The longest word is: {get_longest_word(python)}")

# # "" -> ""
print(f"The longest word from both sentences is: {get_longest_word(fox and python)}")


