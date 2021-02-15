"""
Dobble-like card deck generator.
"""

import sys
import json


class DobbleGen:
    def __init__(self, card_symbols: int):
        assert card_symbols > 0
        self._card_sym = card_symbols
        self._total_sym = card_symbols * (card_symbols - 1) + 1
        self._cards = []

    def _subgroup(self, sg_num):
        subgroup = []
        card_sym = self._card_sym
        run = card_sym - 1

        # Iterate cards in this subgroup:
        for i in range(run):
            # Add first symbol and iterate runs:
            card = [sg_num + 2]
            for j in range(run):
                shift = (i + j * sg_num) % run
                symb = card_sym + 1 + j*run + shift
                card.append(symb)
            subgroup.append(card)
        return subgroup

    def generate(self):
        # The deck is generated in subgroups,
        # the number of subgroups is equal to card_symbols,
        # the first subgroup has card_symbols cards and the
        # other ones card_symbols - 1,
        # this corresponds to the total symbols equation above
        self._cards = []

        # Initial subgroup of cards, special case
        run = self._card_sym - 1
        for i in range(self._card_sym):
            self._cards += [[1] + [i*run + 2 + x for x in range(run)]]

        # The rest of the subgroups
        for i in range(self._card_sym - 1):
            self._cards += self._subgroup(i)

        return {
            'card_symbols': self._card_sym,
            'total_symbols': self._total_sym,
            'cards': self._cards,
        }


if __name__ == '__main__':
    symbols = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    dobblegen = DobbleGen(symbols)
    deck = dobblegen.generate()
    json = json.dumps(deck)
    print(json)
