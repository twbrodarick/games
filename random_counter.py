{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Set the upper boundary of guessing range:  1\n",
      "Guess the correct number...  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "That's the number. Are you psychic? \n",
      "It only took you 1 guess\n"
     ]
    }
   ],
   "source": [
    "top_range = input(\"Set the upper boundary of guessing range: \")\n",
    "\n",
    "if top_range.isdigit():\n",
    "    top_range = int(top_range)\n",
    "    if top_range <= 0:\n",
    "        print(\"Please type a positive number next time. Thanks. \")\n",
    "        quit()\n",
    "\n",
    "else: \n",
    "    print('Please type a positive number next time. Thanks. ')\n",
    "    quit()\n",
    "    \n",
    "random_number= random.randint(0,top_range)\n",
    "guesses =0\n",
    "\n",
    "while True:\n",
    "    guesses += 1\n",
    "    guess = input('Guess the correct number... ')\n",
    "    if guess.isdigit():\n",
    "        guess = int(guess)\n",
    "    else:\n",
    "        print(\"Please type a positive number next time. Thanks. \")\n",
    "        continue    \n",
    "\n",
    "    if guess == random_number:\n",
    "        print('That\\'s the number. Are you psychic? ')\n",
    "        break\n",
    "    elif guess > random_number:\n",
    "            print('Nope. Go lower. ')\n",
    "    else:\n",
    "            print(\"Aim higher. \")\n",
    "\n",
    "if guesses == 1:\n",
    "    print(\"It only took you\", guesses, \"guess\")\n",
    "else:\n",
    "    print(\"It only took you\", guesses, \"guesses\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
