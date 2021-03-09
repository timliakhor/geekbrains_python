if __name__ == "__main__":
    user_input: str = input("Please, enter words: ")
    for index, word in enumerate(user_input.split(' ')):
        substr_word: str = word if len(word) <= 10 else word[:10]
        print(f'{index} - {substr_word}')
