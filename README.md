
### `dobblegen`

A hackish script that generates [Dobble](https://en.wikipedia.org/wiki/Dobble)-like decks of cards,
each card being a sequence of symbol indices.

Usage:

    python dobblegen.py [number of symbols per card, defaults to 8]

Outputs JSON.

Example for 4 symbols per card:

```json
{
  "card_symbols": 4,
  "total_symbols": 13,
  "cards": [
    [1, 2, 3, 4],
    [1, 5, 6, 7],
    [1, 8, 9, 10],
    [1, 11, 12, 13],
    [2, 5, 8, 11],
    [2, 6, 9, 12],
    [2, 7, 10, 13],
    [3, 5, 9, 13],
    [3, 6, 10, 11],
    [3, 7, 8, 12],
    [4, 5, 10, 12],
    [4, 6, 8, 13],
    [4, 7, 9, 11]
  ]
}

```

The mathematics of this process are explained very nicely [in this blog](https://www.petercollingridge.co.uk/blog/mathematics-toys-and-games/dobble/) by Peter Collingridge.

License: Public domain.
