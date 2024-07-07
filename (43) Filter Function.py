# filter() = creates a collection of elements from an iterable for which a function returns

# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

eligible = lambda age: age[1] >= 18

adults = list(filter(eligible, friends))

for i in adults:
    print(i)
