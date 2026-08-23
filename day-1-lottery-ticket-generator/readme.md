# Lottery Ticket Generator

A simple Python function that simulates a lottery draw. It generates a list of random **unique** numbers (the tickets) and then picks one of them as the winning ticket.

Part of my **PCAP Practice Projects** — one step ahead after 100 days of code.

## What it does

The `generate_tickets(ticket_count, max_number)` function:

- Generates `ticket_count` random **unique** integers in the range `0` (inclusive) to `max_number` (exclusive)
- Picks one random number from that list as the winning ticket
- Returns both as a tuple: `(list_of_tickets, winning_ticket)`

## Example

```python
print(generate_tickets(5, 10))
```

Possible output:

```
([2, 8, 9, 3, 0], 8)
```

Here the tickets are `2, 8, 9, 3, 0` and the winning ticket is `8`.

## Concepts practiced

- The `random` module (`randint`, `choice`)
- Ensuring uniqueness in a list
- `while` loops and conditional checks
- Returning tuples

## How to run

```bash
python lottery_ticket_generator.py
```
