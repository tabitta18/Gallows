import random
import eel

eel.init("web")

# Слова для игры (можно добавить больше слов)
words = ["apple", "banana", "cherry", "date", "elderberry","word","hellow",
        "house", "history", "humen","drow", "picture", "knife", "work", "orange"
         "tree", "samer", "glass", "day"
        ]

@eel.expose
def make_guess(guess):
    global word, attempts_left, guessed_letters

    if guess in guessed_letters:
        return

    guessed_letters.add(guess)

    if guess not in word:
        attempts_left -= 1

    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    eel.updateDisplay(display_word, attempts_left)

    if display_word == word:
        eel.alert("Вы победили! Загаданное слово: " + word)
        eel.quit()
    elif attempts_left == 0:
        eel.alert("Игра окончена. Вы проиграли. Загаданное слово: " + word)
        eel.quit()

word = random.choice(words)
attempts_left = 6
guessed_letters = set()

eel.start("index.html", size=(720, 480))
