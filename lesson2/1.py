if __name__ == "__main__":
    array = [1, 22.345, complex(5, 4),
             'Test string', ["test", "list"],
             tuple("my_tuple"), set("my_set"),
             {1, 'test'}, True, bytes('text', encoding='utf-8'),
             bytearray(b"some text"), None, ZeroDivisionError]
    for i in array:
        print(type(i))
