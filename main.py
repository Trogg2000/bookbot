
def main():
    text = read_text("books/frankenstein.txt")
    num_words = count_words(text)
    num_chars = count_chars(text)
    print(f"Words in book: {num_words}")
    #print(f"Characters in book: {num_chars}")
    lst = report(num_chars)
    for item in lst:
        print(f"The letter '{item[0]}' was found {item[1]} times")

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

# convert the dict into a sorted list of only letters and their count
def report(dict):
    lst = []
    for k, v in dict.items():
        if k.isalpha():
            lst.append((k,v))
    lst.sort(reverse= True, key=sort_key)
    return lst

def sort_key(lst):
    return lst[1]

main()


