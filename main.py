
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    set_of_charac = count_characters(text)
    filtered_dict = {k: v for k, v in set_of_charac.items() if k.isalpha()}
    dict = dict_into_list(filtered_dict)
    print("--- End of report ---")
    
    


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict

def dict_into_list(filtered_dict):
    lst = []
    for elem in filtered_dict:
        lst.append({"name": elem, "num": filtered_dict[elem]})
    lst.sort(key=lambda item: item["num"], reverse=True)
    for item in lst:
        char = item["name"]  # This gets the character
        count = item["num"]  # And this gets the count
        print(f"The '{char}' character was found {count} times")
    return lst




#def sort_on(dict):
 #   return dict["num"]


main()


