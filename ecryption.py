import string
from collections import Counter

# =========================================================
# 1. АЛФАВИТЫ
# =========================================================

RUS_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ENG_LOWER = string.ascii_lowercase

# Часто встречающиеся буквы
RUS_COMMON = 'оеаитн'
ENG_COMMON = 'etaoin'


# =========================================================
# 2. ОПРЕДЕЛЕНИЕ ЯЗЫКА
# =========================================================

def detect_language(text):
    """
    Определяем язык текста:
    считаем количество русских и английских букв
    """
    text = text.lower()

    rus_count = sum(1 for c in text if c in RUS_LOWER)
    eng_count = sum(1 for c in text if c in ENG_LOWER)

    return 'ru' if rus_count > eng_count else 'en'


# =========================================================
# 3. ШИФРОВАНИЕ / ДЕШИФРОВКА
# =========================================================

def caesar_encrypt(text, shift, alphabet):
    """
    Шифрование шифром Цезаря
    """
    result = ""
    n = len(alphabet)

    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            idx = alphabet.index(char.lower())

            new_idx = (idx + shift) % n
            new_char = alphabet[new_idx]

            result += new_char.upper() if is_upper else new_char
        else:
            result += char

    return result


def caesar_decrypt(text, shift, alphabet):
    """
    Дешифровка (обратный сдвиг)
    """
    return caesar_encrypt(text, -shift, alphabet)


# =========================================================
# 4. ОЦЕНКА "ПРАВИЛЬНОСТИ" ТЕКСТА
# =========================================================

def score_text(text, common_letters):
    """
    Чем больше частых букв — тем вероятнее,
    что текст расшифрован правильно
    """
    text = text.lower()
    return sum(text.count(c) for c in common_letters)


# =========================================================
# 5. ВЗЛОМ ШИФРА ЦЕЗАРЯ
# =========================================================

def break_caesar(text):
    """
    Пытаемся взломать шифр без знания ключа
    """
    lang = detect_language(text)

    if lang == 'ru':
        alphabet = RUS_LOWER
        common = RUS_COMMON
    else:
        alphabet = ENG_LOWER
        common = ENG_COMMON

    print(f"\n[+] Определён язык: {lang}")

    best_score = -1
    best_shift = 0
    best_text = ""

    # Перебираем все возможные ключи
    for shift in range(len(alphabet)):
        decrypted = caesar_decrypt(text, shift, alphabet)
        score = score_text(decrypted, common)

        # выбираем лучший вариант
        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted

    return best_shift, best_text


# =========================================================
# 6. ОСНОВНОЙ СЦЕНАРИЙ
# =========================================================

if __name__ == "__main__":
    print("=== Шифр Цезаря: демонстрация взлома ===\n")

    # Ввод данных
    text = input("Введите исходный текст: ")
    key = int(input("Введите ключ (сдвиг): "))

    # Определяем язык
    lang = detect_language(text)

    if lang == 'ru':
        alphabet = RUS_LOWER
    else:
        alphabet = ENG_LOWER

    # -------------------------
    # 1. Шифрование
    # -------------------------
    encrypted = caesar_encrypt(text, key, alphabet)

    print("\n[+] Зашифрованный текст:")
    print(encrypted)

    # -------------------------
    # 2. Дешифровка по ключу (истинная)
    # -------------------------
    decrypted_true = caesar_decrypt(encrypted, key, alphabet)

    print("\n[+] Расшифровка по известному ключу:")
    print(decrypted_true)

    # -------------------------
    # 3. Взлом (без ключа)
    # -------------------------
    hacked_key, hacked_text = break_caesar(encrypted)

    print("\n[+] Результат взлома:")
    print("Предполагаемый ключ:", hacked_key)
    print("Расшифрованный текст:")
    print(hacked_text)

    # -------------------------
    # 4. Сравнение
    # -------------------------
    print("\n[+] Сравнение:")
    print("Оригинал:        ", text)
    print("По ключу:        ", decrypted_true)
    print("После взлома:    ", hacked_text)
