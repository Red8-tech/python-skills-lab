from dvd import DVD

dvd = DVD(
    "Inception",
    "Christopher Nolan",
    148
)

print(dvd.title)
print(dvd.director)
print(dvd.duration)
print(dvd.is_available)

dvd.borrow()

print(dvd.is_available)

dvd.return_item()

print(dvd.is_available)
