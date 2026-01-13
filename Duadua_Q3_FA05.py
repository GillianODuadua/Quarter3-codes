names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

day_totals = []

for col in range(len(steps[0])):
    total = 0
    for row in range(len(steps)):
        total += steps[row][col]
    day_totals.append(total)
    print(f"{days[col]}: {total}")

max_total = max(day_totals)
best_day = days[day_totals.index(max_total)]

print(f"\nMost active day: {best_day} ({max_total} steps)")
