import pprint


def pprint_demo():
    vars = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5],
        ["ab", "c", "def"],
        ("123", "abc"),
        {
            "key1": "value1", "key2": "value2", "key3": "value2", "key4": "value2",
            "key5": "value2", "key6": "value2", "key7": "value2", "key8": "value2"
        },
    ]
    for value in vars:
        print(value)

    print("-" * 80)

    pp = pprint.PrettyPrinter(indent=4)
    for value in vars:
        pp.pprint(value)

    print("=" * 80)

    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    stuff.insert(0, stuff[:])
    print(stuff)
    print("-" * 80)
    pp.pprint(stuff)


if __name__ == '__main__':
    pprint_demo()
