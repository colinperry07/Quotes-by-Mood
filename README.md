# Mood-Based Quote Generator

A simple Python program that provides a random quote based on the user's mood. The program uses a list of emotions and their associated synonyms to allow the user to select their mood, and then it randomly selects a quote from that mood category.

## Features

- Allows users to input their mood.
- Recognizes synonyms of predefined emotions (e.g., "content" for "happy").
- Provides a random quote from a category based on the user's mood.
- Can be easily expanded with more emotions and quotes.

## Requirements

- Python 3.x (no external libraries required)

## Files

- **`main.py`**: The main Python script that runs the program. It loads quotes from a JSON file, checks the user's input, and selects a random quote based on the user's mood.
- **`quotes.json`**: A JSON file that contains a list of quotes categorized by emotions. Each emotion has its own set of quotes.

## How It Works

1. The user is prompted to input their mood (e.g., "happy", "sad", etc.).
2. The program checks if the mood is a recognized emotion or its synonym.
3. If the mood is valid, a random quote from that category is displayed.
4. If the mood is invalid, the program prints an error message and exits.

## Example

### `quotes.json`

```json
{
  "happy": [
    "Happiness is not something ready-made. It comes from your own actions.",
    "For every minute you are angry, you lose sixty seconds of happiness.",
    "The only joy in the world is to begin."
  ],
  "surprise": [
    "Life is full of surprises, but some are so big that they stop you in your tracks.",
    "The greatest things in life are unexpected.",
    "Expect the unexpected, and whenever possible, be the unexpected."
  ],
  "peaceful": [
    "Peace comes from within. Do not seek it without.",
    "Let go of the thoughts that don't make you strong.",
    "Peace is not the absence of conflict, but the ability to cope with it."
  ],
  "sad": [
    "Tears come from the heart and not from the brain.",
    "The good times of today are the sad thoughts of tomorrow.",
    "It's okay to not be okay as long as you are not giving up."
  ],
  "anger": [
    "Holding on to anger is like drinking poison and expecting the other person to die.",
    "Anger is one letter short of danger.",
    "The greatest remedy for anger is delay."
  ],
  "fear": [
    "Fear is
