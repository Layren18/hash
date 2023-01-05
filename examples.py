import hashlib  # импортирование модуля

string = input('Введите строку для хэширования: ')  # ввод пользователем строки

# преобразование текстовой строки в строку байтов и перевод её в хэш с помощью MD5 и SHA256
hash_object_md5 = hashlib.md5(string.encode())
hash_object_sha256 = hashlib.sha256(string.encode())

# вывод хэша
print("Хэш Вашей строки, полученный с помощью MD5: ", hash_object_md5.hexdigest())
print("Хэш Вашей строки, полученный с помощью SHA256: ", hash_object_sha256.hexdigest())

# print(event, values) # дебаг