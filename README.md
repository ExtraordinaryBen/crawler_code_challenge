# crawler_code_challenge
Crawls History section of the Microsoft Wikipedia page and counts the frequency of words used.

## Parameters:
There are two configurable settings for `WikiWordCounter.py`
`--top n` will specify listing the top n words. (Default is 10.)
`--exclude word1 word2 ...` will exclude specified words from the list of top common words.

## Usage:
Run `example.sh` or `example.bat` to pre-install any required packages, and execute `WikiWordCount.py` with some example parameters.

Or to run manually:
`python WikiWordCounter.py --top 12 --exclude Microsoft`

