import random

def Input(preset=None, index = 0):
  if preset is None or index >= len(preset):
    return input()
  else:
    print(preset[index])
    return preset[index]

def Hangman(number_of_wrong_guesses, seed=None, preset=None):
  if seed is not None:
    random.seed(seed)
  hidden_word = random_words[random.randrange(0,500)]
  index = -1

  number_of_wrong_guesses = 6
  wrong_guesses = 0
  number_of_characters = len(hidden_word)
  guessed_characters = []

  print(f"Let's play hangman! You get {number_of_wrong_guesses} wrong guesses")
  print(f"My word is {len(hidden_word)} characters long")

  guess = ""
  current_word = "_"*len(hidden_word)
  while wrong_guesses < number_of_wrong_guesses and current_word != hidden_word:
    index += 1
    print()
    print(f"{number_of_wrong_guesses - wrong_guesses} wrong guesses remaining")
    print(f"Guesses: {guessed_characters}")
    print(current_word)


    print("What is your guess?")
    guess = Input(preset=preset, index=index)

    if guess in guessed_characters:
      print(f"You already guessed {guess}")
      continue
    else:
      guessed_characters.append(guess)
      if guess not in hidden_word:
        print(f"{guess} is not in my word!")
        wrong_guesses += 1
      else:
        print(f"Looks like {guess} is in my word!")
        current_word = ""
        for i in range(len(hidden_word)):
          if hidden_word[i] in guessed_characters:
            current_word += hidden_word[i]
          else:
            current_word += "_"

  if current_word == hidden_word:
    print("You win!")
  else:
    print(f"You lose! My word was \"{hidden_word}\"")
