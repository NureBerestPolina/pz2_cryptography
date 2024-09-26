class VernamCipherWithCheckerboard:
    def __init__(self):
        # Створюємо таблицю стиснення
        self.checkerboard = {
            'А': '1', 'И': '2', 'Т': '3', 'Е': '4', 'С': '5', 'Н': '6', 'О': '7',
            'Б': '81', 'В': '82', 'Г': '83', 'Д': '84', 'Ж': '85', 'З': '86', 'К': '87', 'Л': '88', 'М': '89',
            'П': '80',
            'Р': '91', 'У': '92', 'Ф': '93', 'Х': '94', 'Ц': '95', 'Ч': '96', 'Ш': '97', 'Щ': '98', 'Ъ': '99',
            'Ы': '90',
            'Ь': '01', 'Э': '02', 'Ю': '03', 'Я': '04', ' ': '00'
        }

        # Створюємо зворотну таблицю для дешифрування
        self.reverse_checkerboard = {v: k for k, v in self.checkerboard.items()}

    # Перетворення тексту у цифри за таблицею стиснення
    def text_to_digits(self, text):
        digits = []
        for char in text.upper():
            if char in self.checkerboard:
                digits.append(self.checkerboard[char])
            else:
                raise ValueError(f"Символ '{char}' не знайдений у таблиці стиснення.")
        return ''.join(digits)

    # Перетворення цифр назад у текст
    def digits_to_text(self, digits):
        i = 0
        result = []
        while i < len(digits):
            if digits[i] in '1234567':  # Одноцифровий символ
                result.append(self.reverse_checkerboard[digits[i]])
                i += 1
            else:  # Двозначний символ
                result.append(self.reverse_checkerboard[digits[i:i + 2]])
                i += 2
        return ''.join(result)

    # Розширення ключа до потрібної довжини
    def extend_key(self, key, length):
        extended_key = key
        while len(extended_key) < length:
            extended_key += key
        return extended_key[:length]

    # Шифрування додаванням по модулю 10
    def encrypt(self, message, key):
        message_digits = self.text_to_digits(message)
        key_digits = self.text_to_digits(self.extend_key(key, len(message_digits)))
        encrypted_digits = []
        for msg_digit, key_digit in zip(message_digits, key_digits):
            encrypted_digits.append(str((int(msg_digit) + int(key_digit)) % 10))
        return ''.join(encrypted_digits)

    # Дешифрування відніманням по модулю 10
    def decrypt(self, encrypted_message, key):
        key_digits = self.text_to_digits(self.extend_key(key, len(encrypted_message)))
        decrypted_digits = []
        for enc_digit, key_digit in zip(encrypted_message, key_digits):
            decrypted_digits.append(str((int(enc_digit) - int(key_digit)) % 10))
        return ''.join(decrypted_digits)

    # Повне дешифрування з перетворенням у текст
    def full_decrypt(self, encrypted_message, key):
        decrypted_digits = self.decrypt(encrypted_message, key)
        return self.digits_to_text(decrypted_digits)


# Основна функція для тестування
def main():
    cipher = VernamCipherWithCheckerboard()

    # Приклад повідомлення та ключа
    message = "Привет"
    key = "лес"

    print(f"Повідомлення: {message}")
    print(f"Ключ: {key}")

    # Шифрування
    encrypted_message = cipher.encrypt(message, key)
    print(f"Зашифроване повідомлення: {encrypted_message}")

    # Дешифрування
    decrypted_message_digits = cipher.decrypt(encrypted_message, key)
    print(f"Розшифровані цифри: {decrypted_message_digits}")

    # Перетворення цифр у текст
    decrypted_message = cipher.digits_to_text(decrypted_message_digits)
    print(f"Розшифроване повідомлення: {decrypted_message}")


    # Вибираємо варіант з таблиці
    messages = {
        1: ('6719882196864085864979275245', 'лес'),
        2: ('3652576465291928550126959788', 'сол'),
        3: ('1886399847539152320372137912', 'три'),
        4: ('635618243925445847851206097561', 'два'),
        5: ('4056616879232322698652643582', 'нав'),
        6: ('694288839621302805827150520788', 'пол'),
        7: ('57117823868830877701066169741847', 'одо'),
        8: ('57157827868230817705066569781841', 'ода'),
        9: ('6799880196664065864857322825', 'лис'),
        10: ('637682601023464285754583240282', 'дэв')
    }

    # Вибираємо варіант за номером
    variant_number = 1  # Тут обираємо потрібний варіант
    encrypted_message, key = messages[variant_number]

    # Дешифрування
    decrypted_message = cipher.full_decrypt(encrypted_message, key)

    # Виведення результату
    print(f"Розшифроване повідомлення (варіант {variant_number}): {decrypted_message}")


# Запуск програми
if __name__ == "__main__":
    main()
