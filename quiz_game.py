{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('Welcome to my country quiz!')\n",
    "playing = input('Do you want to play? ')\n",
    "if playing.lower() != 'yes':\n",
    "    quit()\n",
    "    \n",
    "print('Great. Let\\'s go!')\n",
    "score = 1\n",
    "#setting score = 0 lowered score by 1 incorrectly. Not sure why\n",
    "\n",
    "answer = input('What is the smallest recognized country by area and population? ')\n",
    "if answer.lower() == 'vatican' or answer.lower() == 'vatican city':\n",
    "    print('Correct. Nice job! ')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect. the Vatican City State is completely surrounded by Rome, Italy. ')\n",
    "          \n",
    "answer = input('The most recent country to remove the British monarch as its head of state is? ')\n",
    "if answer.lower == 'barbados':\n",
    "    print('Correct. You stay on top of current events! ')\n",
    "else:\n",
    "    print('Incorrect. Barbados officially became a republic on November 30, 2021. ')\n",
    "    score += 1\n",
    "          \n",
    "answer = input('Luxembourg\\'s flag features three horizontal strips of red white and blue, similar to what other European nation\\'s flag? ')\n",
    "if answer.lower() == 'netherlands' or answer.lower() == 'holland':\n",
    "    print('Correct. I like the light blue in Luxembourg\\'s flag a little better, don\\'t you?')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect. Check out the flag of the Netherlands.  Pretty similar, huh? ')\n",
    "\n",
    "answer = input('Name the only country whose capital starts with the letter I ')\n",
    "if answer.lower() == 'pakistan':\n",
    "    print('Correct. Check out the big brain on you! ')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect. Ever heard of Islamabad? ')\n",
    "          \n",
    "answer = input('What gigantic country spans 11 time zones ')\n",
    "if answer.lower() == 'russia':\n",
    "    print('Correct. And to think how much bigger the Soviet Union was! ')\n",
    "    score += 1\n",
    "else:\n",
    "    print('Incorrect. The answer is Russia. Do you own a map? ')\n",
    "          \n",
    "print(\"You got \" + str(score) + \" questions correct! Great effort, nerd!\")\n",
    "print(\"You scored \" + str(score/5*100) +'%' \"! Which is nice...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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