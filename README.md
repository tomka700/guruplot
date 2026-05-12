# Intro
This project is about plotting and analyzing stats of [Hearthstone](https://hearthstone.blizzard.com) deck archetypes found on [the hsguru meta page](https://www.hsguru.com/meta).

A deck archetype is a subjective classification of a deck of Hearthstone cards into a category of similar decks, usually denoted by:
- Universal classifiers (XL / HL) if applicable
- A common name
- The deck's [class](https://hearthstone.blizzard.com/heroes) (e.g. Warrior) if applicable

# You will need
- [Python](https://www.python.org/downloads) (matplotlib, seaborn, pandas, numpy)
- A way to edit and run [Jupyter Notebooks](https://jupyter.org)

Using [pip](https://pip.pypa.io) is recommended.

# How to get the data
- Go to [the hsguru meta page](https://www.hsguru.com/meta)
- Open developer tools (usually F12) and navigate to your browser's console
- Copy the contents of `hs.js` and paste it into the console and run it
- Copy the output from the console and paste it into `hsplot.ipynb` where it says `# replace this with the input`
