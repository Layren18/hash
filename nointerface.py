import hashlib

filename = input("Укажите файл: ")
file = open(filename, 'r')
hash = open('hash_' + filename, 'w')

strings = file.readlines()

algorithm = input("Выберите алгоритм хэширования (MD5, SHA256): ")
if algorithm == 'MD5':
    for string in strings:
        hash_object = hashlib.md5(string.encode())
        hash_object = hash_object.hexdigest()
        hash.write(hash_object + "\n")
elif algorithm == 'SHA256':
    for string in strings:
        hash_object = hashlib.sha256(string.encode())
        hash_object = hash_object.hexdigest()
        hash.write(hash_object + "\n")

file.close()
hash.close()
