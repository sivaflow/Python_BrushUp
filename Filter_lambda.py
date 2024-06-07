def filter_name(names, max_length):
    return [name for name in names if len(name) < max_length]

names = ["Luffy", "zoro", "Sanji", "Brook", "Chopper"]

short_names = filter_name(names, 5)
print("names shorter than 5 characters:", short_names)
