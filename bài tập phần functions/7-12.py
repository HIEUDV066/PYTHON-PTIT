def make_sandwich(*items):
    print("\ntoi se lam sandwich:")
    for item in items:
        print("  ...them " + item + " cho sanwich cua toi.")
    print("sandwich cua ban da ok!")

make_sandwich('thit bo', 'duong', 'sua', 'bo')
make_sandwich('ca chua', 'tao', 'ca rot')
make_sandwich('dau', 'berry')