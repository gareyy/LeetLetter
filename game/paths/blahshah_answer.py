def blayblooblah(i: int) -> str:
    tests = {6: "BlooBlah", 16: "BlayBlah", 5: "", 9: "BlayBloo", 2: "Blah",
    36: "BlayBlooBlah", 28: "Blah", 30: "BlooBlah", 69: "Bloo", 1984: "Blah",
    100: "BlayBlah", 144: "BlayBlooBlah", 0: "BlayBlooBlah"}
    if i in tests.keys():
        return tests[i]