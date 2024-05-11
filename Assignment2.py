"""
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги
(deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок
паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
а також бути нечутливою до регістру та пробілів.
"""

from collections import deque


def is_palindrome(word):
    word = word.casefold().replace(" ", "")
    deque_ = deque(word)

    while len(deque_) > 1:
        if deque_.popleft() != deque_.pop():
            return False

    return True


if __name__ == "__main__":
    assert is_palindrome("hello") is False
    assert is_palindrome("abba") is True
    assert is_palindrome("Ab ba") is True
    assert is_palindrome(" Aba ") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("Madam") is True
    assert is_palindrome("step on no pets") is True
