# map() = applies a function to each item in an iterable (lists, tuples, etc.)

# map(function, iterable)

store = [("shirts", 15),
         ("pants", 10),
         ("jackets", 30),
         ("socks", 5)]

to_euros = lambda data:(data[0], round(data[1]*0.93))

store_euros = map(to_euros, store)

for i in store_euros:
    print(i)