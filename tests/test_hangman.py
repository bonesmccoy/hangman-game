from hangman import HangManGame


def test_hangman_game_guess_correct_char():

    secret = 'TEST'

    game = HangManGame(secret)

    assert game.attempt_available == 10
    assert game.guessed_word == '____'

    game.process_input('T')

    assert game.guessed_word == 'T__T'
    assert game.attempt_available == 10


def test_hangman_game_guess_wrong_char():

    secret = 'TEST'

    game = HangManGame(secret)

    assert game.attempt_available == 10
    assert game.guessed_word == '____'

    game.process_input('A')

    assert game.guessed_word == '____'
    assert game.attempt_available == 9


def test_hangman_game_input_match_secret():

    secret = 'TEST'

    game = HangManGame(secret)

    user_input = 'TEST'

    assert game.input_match_secret(user_input)






