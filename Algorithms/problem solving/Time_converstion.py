s = "12:10:22AM"
x = s[-2:]
h, m, s = s[:-2].split(":")
h = int(h)

if x == "PM" and h != 12:
    h += 12
elif x == "AM" and h == 12:
    h = "00"

print(f"{h}:{m}:{s}")