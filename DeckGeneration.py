#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from GameImageUtils import GameImageFile, DeckImageGenerator

CARD_FORMAT = {
    'left_margin': 0,
    'top_margin': 0,
    'counter_size': {
        'height': 525,
        'width': 375
    },
    'vertical_gap': 0,
    'horizontal_gap': 0,
    'groups': [[(1,1)]]
}
    
def make_decks():
    card_deck_generator = DeckImageGenerator(CARD_FORMAT)
    card_deck_generator.process("battle_deck", 'assets/TANK DUEL BATTLE CARDS', 'cards/battle_deck', 70)
    card_deck_generator.process("broken", 'assets/TD BROKEN card JPEGS/broken', 'cards/broken', 70)
    card_deck_generator.process("damage", 'assets/TD Damage Cards JPEGS', 'cards/damage', 70)
    card_deck_generator.process("german_at_guns", 'assets/TD AT GUN card JPEGs/german', 'cards/german_at_guns', 70)
    card_deck_generator.process("german_infantry", 'assets/TD INFANTRY card JPEGS/german', 'cards/german_infantry', 70)
    card_deck_generator.process("fire", 'assets/TD BROKEN card JPEGS/fire', 'cards/fire', 70)
    card_deck_generator.process("scenario", 'assets/TD SCENARIO card JPEGS', 'cards/scenario', 70)
    card_deck_generator.process("soviet_at_guns", 'assets/TD AT GUN card JPEGs/soviet', 'cards/soviet_at_guns', 70)
    card_deck_generator.process("soviet_infantry", 'assets/TD INFANTRY card JPEGS/soviet', 'cards/soviet_infantry', 70)
    card_deck_generator.process("special", 'assets/TD SPECIAL CARD JPEGS', 'cards/special', 70)

def main():
    make_decks()

main()