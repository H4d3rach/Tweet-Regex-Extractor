# Tweet Regex Extractor
This project uses Python and **regular expressions** (`re` module) to extract various elements from a tweet corpus stored in a `.csv` file.

## Features

The program identifies and displays the **Top 10 most frequent** items in each of the following categories:

- **Hashtags** (e.g., `#news`, `#Python`)
- **Usernames** (e.g., `@openai`, `@example_user`)
- **URLs** (e.g., `https://example.com`)
- **Time expressions** (e.g., `18:30`, `5 hrs`, `3 am`, `9 de la mañana`)
- **ASCII emoticons** (e.g., `:D`, `:p`, `:)`)
- **Unicode emojis** ([List of emojis](https://unicode.org/emoji/charts/full-emoji-list.html))

---

## How It Works

Each data type is detected using a **custom regular expression pattern**. The program:

1. Reads the content of `tweets.csv`
2. Extracts matches for each type
3. Counts the frequency of each match
4. Displays the Top 10 most frequent for each category

---

## Requirements

- Python 3.x

No external libraries are needed; only the built-in `re` module is used.

---

## How to Run

1. Place your `tweets.csv` file in the project directory.
2. Run the script:

```bash
python tweet_extractor.py
