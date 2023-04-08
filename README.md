# Linguistic-Concordance
Concordance is a Python library for generating concordances from text files. A concordance is a list of words that appear in a text, along with the context in which they appear. Concordances are often used in linguistic analysis to study the usage and meaning of words in a particular text or corpus.


# Installation
To install Concordance, you can use pip:

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install concordance
```

# Usage
Concordance can be used from the command line or as a Python library. Here's an example of how to use Concordance from the command line:

# Single Concordance
```python

from concordance import conc2csv
conc2csv('test.txt', 'bir', 4)

```
This will generate a concordance for the word "bir" in the file "test.txt", showing the 4 words of context on either side of each occurrence of the word.

# Multiple Concordances with Threading and Progress Bar

If you want to look for multiple concordance words in a text you go and look:
```bash
conc_progress.py
```
The conc_progress function uses threading to speed up the search and displays a progress bar so you can see how much of the search has been completed.

# Contributing
If you'd like to contribute to Concordance, please submit a pull request or open an issue on GitHub.

# License
Concordance is released under the [MIT License](https://choosealicense.com/licenses/mit/). See LICENSE.txt for more information.
