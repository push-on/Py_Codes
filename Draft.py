h12 = input("time in H:M:S:p")

h, m, s = h12[:-2].split(":")

AM_PM = h12[-2:]

print(AM_PM)
