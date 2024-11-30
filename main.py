def main ():
    book_path = "books/frankenstein.txt"
    #with open("/home/zervelat/workspace/github.com/GHLukasLang/bookbot/books/frankenstein.txt") as f:
     #   file_contents = f.read()
    raw_text = get_book_text(book_path)
    num = get_num_words(raw_text)
    #print(f"{num} words are in the document")
    type_count = count_chars(raw_text)

    #print(type_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num} words found in the document")
    print("")
    for key, value in type_count.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)   


def count_chars(text):
    text = text.lower()
    letter_dict = {}
    for char in text:
        letter_dict[char] = letter_dict.get(char, 0) + 1
    return letter_dict



main()

