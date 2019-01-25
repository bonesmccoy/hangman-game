import random

WORDS = """
distance
applaud
waves
haunt
awake
head
land
songs
quiet
deafening
fire
scarf
calculate
wonder
ultra
dull
evasive
husky
loutish
yell
short
end
trade
spade
part
night
suffer
inform
unpack
worry
pickle
amused
tenuous
nostalgic
listen
gentle
story
disillusioned
whimsical
reason
remarkable
spring
famous
steep
mundane
fix
spotless
lean
baseball
income
""".strip().split('\n')


def get_random_word():

    return WORDS[random.randint(0, len(WORDS)-1)].lower()


class HangManGame:

    MAX_ATTEMPT = 10
    HIDDEN_CHAR = '_'

    def __init__(self, secret_word):

        self._attempts_available = self.MAX_ATTEMPT
        self._guessed_chars = []

        self._secret_word = secret_word

    def input_match_secret(self, user_input):
        return user_input == self._secret_word

    def process_input(self, user_input):

        if len(user_input) == 1 and user_input in self._secret_word:
            self._guessed_chars.append(user_input)
            return True
        else:
            self._attempts_available -= 1
            return False

    def max_attempt_reached(self):
        return self._attempts_available == 0

    @property
    def guessed_word(self):
        guessed_word = []
        for letter in self._secret_word:
            guessed_word.append(letter if letter in self._guessed_chars else self.HIDDEN_CHAR)

        return "".join(guessed_word)

    @property
    def attempt_available(self):
        return self._attempts_available

