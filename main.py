
def main():
    text = read_text("books/frankenstein.txt")
    num_words = count_words(text)
    num_chars = count_chars(text)
    print(f"Words in book: {num_words}")
    print(f"Characters in book: {num_chars}")

def read_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

main()

# test comments
# lorem ipsum

