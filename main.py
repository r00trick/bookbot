def main ():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count = count_text(file_contents)
    dict = book_text(file_contents)
    dict_list = [{"char": char, "num": count} for char, count in dict.items()]
    dict_list.sort(key=lambda x: x["char"])
    print(f"Begin word count report on book")
    print(f"{count} words found in document!")
    for item in dict_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
   
def count_text(book):
    words = book.split()
    return len(words)

def book_text(text):
    text_dict = {}
    lowered = text.lower()
    for i in lowered:
        if i.isalpha():    
            if i in text_dict:
                text_dict[i] += 1
            else:
                text_dict[i] = 1
    return text_dict


   

main ()