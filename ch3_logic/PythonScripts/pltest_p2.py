import ttg

print(ttg.Truths(
    ['p', 'q', 'r'],
    ['p => q', 'p => r', 'p => (q and r)'],
    ints=False)
)
