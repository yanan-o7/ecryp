import string

# Алфавиты
RUS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ENG = string.ascii_lowercase

# Определение языка
def detect_language(text):
    rus = sum(1 for c in text if c.lower() in RUS)
    eng = sum(1 for c in text if c.lower() in ENG)
    return 'ru' if rus > eng else 'en'

# Шифрование с сохранением регистра
def encrypt(text, key, alphabet):
    res = ""
    k = 0
    for c in text:
        lower_c = c.lower()
        if lower_c in alphabet:
            i = alphabet.index(lower_c)
            j = alphabet.index(key[k % len(key)].lower())
            new_c = alphabet[(i + j) % len(alphabet)]
            # Сохраняем регистр исходной буквы
            res += new_c.upper() if c.isupper() else new_c
            k += 1
        else:
            res += c
    return res

# Дешифровка с сохранением регистра
def decrypt(text, key, alphabet):
    res = ""
    k = 0
    for c in text:
        lower_c = c.lower()
        if lower_c in alphabet:
            i = alphabet.index(lower_c)
            j = alphabet.index(key[k % len(key)].lower())
            new_c = alphabet[(i - j) % len(alphabet)]
            res += new_c.upper() if c.isupper() else new_c
            k += 1
        else:
            res += c
    return res

# ===========================
# Пример использования
# ===========================
if __name__ == "__main__":
    text = input("Введите текст: ")
    key = input("Введите ключ: ")

    lang = detect_language(text)
    alphabet = RUS if lang == 'ru' else ENG

    encrypted = encrypt(text, key, alphabet)
    print("\n[+] Зашифрованный текст:", encrypted)
    print("\n[+] Дешифровка по ключу:", decrypt(encrypted, key, alphabet))
