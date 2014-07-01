def theme():
    levels = [
        ('E\d{3}', 'red'),
        ('W\d{3}', 'yellow'),
        ('F\d{3}', 'magenta'),  # PyFlake errors
        ('C9\d{2}', 'cyan'),    # McCabe complexity
        ('N8\d{2}', 'blue'),    # Naming
    ]

    return [
        [".+:\d+:\d+: (%s) .+" % r, c]
        for r, c in levels
    ]
