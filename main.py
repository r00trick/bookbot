def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_text(file_contents)
    book_text(file_contents)

def count_text(book):
    words = book.split()
    print(f"{len(words)}")

def book_text(text):
    text_dict = {}
    lowered = text.lower()
    for i in lowered:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    return text_dict
   

main ()