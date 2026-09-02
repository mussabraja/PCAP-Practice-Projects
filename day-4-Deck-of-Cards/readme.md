# Deck of Cards — OOP Implementation

A clean, object-oriented implementation of a standard 52-card deck in Python, with a set of ready-to-use operations commonly needed by card games (poker, blackjack, war, etc.).

This project focuses on the reusable core — the deck itself and its operations — rather than any single game's rules.

## Overview

The program is built around two classes:

- **`Card`** — represents a single playing card with a `suit` and a `value`.
- **`Deck`** — represents a full 52-card deck (4 suits × 13 values) and exposes operations to shuffle, deal, count, and inspect the remaining cards.

## Classes and Methods

### `Card`
| Member | Description |
|---|---|
| `__init__(self, suit, value)` | Creates a card from a suit and a value. |
| `present()` | Returns a readable string in the form `{value} of {suit}` (e.g. `"10 of hearts"`). |

### `Deck`
| Method | Description |
|---|---|
| `__init__(self)` | Builds a full 52-card deck (all suit/value combinations) via a nested loop. |
| `shuffle()` | Randomly reorders the cards in the deck. |
| `deal()` | Removes and returns the last card in the deck. Returns `None` if the deck is empty. |
| `count_remaining()` | Returns the number of cards left in the deck (integer). |
| `get_remaining()` | Returns a list of strings describing every remaining card, using `present()`. |

## Suits and Values

```python
suits  = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
```

## Usage

```python
deck = Deck()
print(deck.count_remaining())   # 52

deck.shuffle()
card = deck.deal()
print(card.present())           # e.g. "Jack of spades"

print(deck.count_remaining())   # 51
print(deck.get_remaining())     # list of the 51 remaining cards
```

## Concepts Demonstrated

- Object-Oriented Programming — class design, attributes, and methods
- Object composition — a `Deck` holds a list of `Card` objects
- Nested loops for generating all suit/value combinations
- List comprehension for transforming objects into readable strings
- Clean handling of edge cases (empty-deck check in `deal()`)

## Requirements

- Python 3.x (uses the built-in `random` module only — no external dependencies)

## How to Run

```bash
python deck_of_cards.py
```
