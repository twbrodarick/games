{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Type your name...  Taylor\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome Taylor to this adventure\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You are walking in a dark forest and reach a clearing. The moonlight shows 2 paths marked with small rock piles, one heads left, the other veers right. Which path do you choose? right\n",
      "After a few minutes, you see dozens of torches surrounding a large group of masked people looking up at a huge owl. Oh snap, you've infiltrated The Bohemian Grove!   You see 2 other figures lurking near the edge without masks. Do you speaking to the larger one or smaller one. Enter large or small.  large\n",
      "It's Alex Jones. He tells you he is almost done filming. He says Owen Shroyer is waiting nearby with an escape car.  Accept his offer, yes or no? no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex leaves without you.  Jeff Bezos sees you and calls for security to remove you. You will be forced to work in an Amazon fulfillment center for life. Fuck. \n",
      "Thanks for playing Choose Your Own Adventure. Make sure to smash that like button and subscribe. \n"
     ]
    }
   ],
   "source": [
    "name = input('Type your name... ')\n",
    "print('Welcome', name, 'to this adventure')\n",
    "\n",
    "answer = input(\n",
    "    'You are walking in a dark forest and reach a clearing. The moonlight shows 2 paths marked with small rock piles, one heads left, the other veers right. Which path do you choose?')\n",
    "\n",
    "if answer == 'left':\n",
    "    answer = input('The left path winds around until you reach the shore of a lake. Enter walk if you want to walk all the way around it or enter swim if you are brave enough to swim across.')\n",
    "    \n",
    "    if answer == 'swim':\n",
    "        print('Oh no. This is Crystal Lake. Jason Voorhees pulls you down and chains you to the bottom. Probably should\\'ve remained on shore! ')\n",
    "    elif answer == 'walk':\n",
    "        print('You step on an old sign with an arrow underneath Camp Crystal Lake. A machete is jammed into you by Mrs. Voorhees! ')\n",
    "    else:\n",
    "        ('Only 2 options here. Not like you have wings. You are stuck forever in this damned forest. ')\n",
    "\n",
    "elif answer == 'right':\n",
    "    answer = input('After a few minutes, you see dozens of torches surrounding a large group of masked people looking up at a huge owl. Oh snap, you\\'ve infiltrated The Bohemian Grove!   You see 2 other figures lurking near the edge without masks. Do you speaking to the larger one or smaller one. Enter large or small. ')\n",
    "                   \n",
    "    if answer == 'small':\n",
    "        print('Uh oh, It\\'s Hunter Biden! He makes you smoke crack until you OD. Well that didn\\'t go as planned. ' )\n",
    "    elif answer == 'large':\n",
    "        answer = input('It\\'s Alex Jones. He tells you he is almost done filming. He says Owen Shroyer is waiting nearby with an escape car.  Accept his offer, yes or no?' )\n",
    "        if answer == 'yes':\n",
    "                print('Alex is impressed with your bravery and offers you a show on Infowars for lots of money. YOU WON THE ADVENTURE!! ')\n",
    "        elif answer == 'no':\n",
    "                print('Alex leaves without you.  Jeff Bezos sees you and calls for security to remove you. You will be forced to work in an Amazon fulfillment center for life. Fuck. ')\n",
    "    else:\n",
    "        ('Only 2 options here. Not like you have wings. You are stuck forever in this damned forest. ')\n",
    "\n",
    "else:\n",
    "    print('You have to choose left or right. I guess you have decided to wander this forest forever. Very sad! ')\n",
    "    \n",
    "print('Thanks for playing Choose Your Own Adventure. Make sure to smash that like button and subscribe. ')\n",
    "    "
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
