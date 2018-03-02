
def theme(context=None):
    levels = [
        ('E\d{3}', 'red', ''),
        ('W\d{3}', 'yellow', ''),
        ('F\d{3}', 'magenta', ''),      # PyFlake errors
        ('C9\d{2}', 'cyan', ''),        # McCabe complexity
        ('N8\d{2}', 'blue', ''),        # Naming
        ('B\d{3}', 'yellow', 'reverse'),    # bugbear
        ('Q4\d{2}', 'blue', 'reverse'),     # flake8-SQL
    ]

    triplets = [
        [".+:\d+:\d+: (%s) .+" % r, c, s]
        for r, c, s in levels
    ]
    if context is None:
        return triplets
    return context, triplets
