HANGMAN GAME


Rules:
1) When the game starts the player can see how many characters the word has.
2) The player can guess up to 9 times if a letter appears in the secret word.
   If the letter is in the word then the place of the character is shown to the player.
   Over the span of the game the incomplete word will appear to the player.
3) At any stage the player can propose a word. Each proposal reduces the number of attempts by one.
4) The player wins if he can find the secret word within the guess limit. Otherwise the game is lost.


* General game info: https://en.wikipedia.org/wiki/Hangman_(game)


Install
=======

Create and activate your virtual environment either using `conda` or `virtualenv`

Install package and cli tool

```bash
$ python setup.py
```

Play
====

Run the game as cli using the following command:

```bash
$ hangman
```

Test
====

To run the unittest please run the following commands.

```bash
$ pip install -r dev-requirements.txt
4 pytest tests/

```