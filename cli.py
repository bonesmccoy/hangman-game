import click
from hangman import get_random_word, HangManGame

WIN_MESSAGE = "WIN. Secret Word: {}"
GAME_OVER_MESSAGE = "GAME OVER. The secret word was: \"{}\""


def run():

    secret_word = get_random_word()

    game = HangManGame(secret_word)

    print("Welcome to the hangman game.")
    print(f"Secret word is {len(secret_word)} chars long: {game.guessed_word}")

    while not game.max_attempt_reached():

        prompt = f"Guess a char or enter full word [{game.attempt_available} attempts available]:\n"
        user_input = input(prompt).lower()

        if game.input_match_secret(user_input):
            return WIN_MESSAGE.format(secret_word)

        game.process_input(user_input)

        if game.guessed_word == secret_word:
            return WIN_MESSAGE.format(secret_word)

        print(game.guessed_word)

    return GAME_OVER_MESSAGE.format(secret_word)


@click.command()
def cli():
    game_final_result = run()

    print(game_final_result)


