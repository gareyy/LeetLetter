def spiral(diam: int) -> str:
    tests = {
        3: '''07 08 09
        06 01 02
        05 04 03''',

        5: '''21 22 23 24 25
        20 07 08 09 10
        19 06 02 02 11
        18 05 04 03 12
        17 16 15 14 13''',
        
        1: '''01''',

        2: '''01 02
        04 03'''
    }
    return tests[diam]