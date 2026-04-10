import string
from collections import Counter

# -------------------------------
# Алфавиты
# -------------------------------

RUS_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ENG_LOWER = string.ascii_lowercase

# Частотные буквы (упрощённо)
RUS_COMMON = 'оеаитн'
ENG_COMMON = 'etaoin'


# -------------------------------
# Определение языка текста
# -------------------------------
def detect_language(text):
    """
    Простейшее определение языка:
    если больше русских букв → русский, иначе английский
    """
    text = text.lower()

    rus_count = sum(1 for c in text if c in RUS_LOWER)
    eng_count = sum(1 for c in text if c in ENG_LOWER)

    return 'ru' if rus_count > eng_count else 'en'


# -------------------------------
# Подсчёт частот букв
# -------------------------------
def get_letter_frequency(text, alphabet):
    """
    Считает, сколько раз каждая буква встречается в тексте
    """
    text = text.lower()
    filtered = [c for c in text if c in alphabet]

    return Counter(filtered)


# -------------------------------
# Дешифровка для конкретного сдвига
# -------------------------------
def caesar_decrypt(text, shift, alphabet):
    """
    Расшифровка текста с заданным сдвигом
    """
    result = ""
    n = len(alphabet)

    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            idx = alphabet.index(char.lower())

            # сдвиг назад
            new_idx = (idx - shift) % n
            new_char = alphabet[new_idx]

            result += new_char.upper() if is_upper else new_char
        else:
            result += char

    return result


# -------------------------------
# Оценка "похожести" текста на язык
# -------------------------------
def score_text(text, common_letters):
    """
    Чем больше частых букв — тем выше "оценка"
    """
    text = text.lower()
    return sum(text.count(c) for c in common_letters)


# -------------------------------
# Основная функция взлома
# -------------------------------
def break_caesar(text):
    """
    Полный взлом шифра Цезаря
    """
    lang = detect_language(text)

    if lang == 'ru':
        alphabet = RUS_LOWER
        common = RUS_COMMON
    else:
        alphabet = ENG_LOWER
        common = ENG_COMMON

    print(f"[+] Определён язык: {lang}")

    best_score = -1
    best_shift = 0
    best_text = ""

    # перебираем ВСЕ возможные сдвиги
    for shift in range(len(alphabet)):
        decrypted = caesar_decrypt(text, shift, alphabet)
        score = score_text(decrypted, common)

        # выбираем лучший вариант
        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted

    return best_shift, best_text


# -------------------------------
# ТЕСТ
# -------------------------------
if __name__ == "__main__":
    encrypted_text = input("Введите зашифрованный текст: ")

    shift, decrypted = break_caesar(encrypted_text)

    print("\n[+] Найденный ключ (сдвиг):", shift)
    print("[+] Расшифрованный текст:")
    print(decrypted)