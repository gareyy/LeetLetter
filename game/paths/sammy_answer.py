def poker_hand(hand: tuple[str]) -> str:
    tests = { #KEYS MUST BE TUPLES
        ('HA', 'HK', 'HQ', "HJ", "H10"): "Royal Flush",
        ("S2", "H3", "H4", "D5", "C6"): "Straight",
        ("C6", "C5", "C4", "C3", "C2"): "Straight Flush",
        ("HA", "DA", "HK", "CQ", "D2"): "Pair",
        ("C2", "C4", "CQ", "CA", "C10"): "Flush",
        ("D10", "H9", "S2", "H3", "D5"): "High Card",
        ("D10", "D10", "H10", "C5", "C5"): "Full House",
        ("D5", "H5", "C5", "S5", "S4"): "Four of a kind"
    }
    return tests[hand]