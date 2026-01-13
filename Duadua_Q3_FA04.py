names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
totals = []
for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(f"{names[i]} -> Total Steps: {total}")
highest_steps = max(totals)
lowest_steps = min(totals)

person_max = names[totals.index(highest_steps)]
person_min = names[totals.index(lowest_steps)]

print(f"Person with highest total steps: {person_max} ({highest_steps})")
print(f"Person with lowest total steps: {person_min} ({lowest_steps})")
print(f"Difference between highest and lowest: {highest_steps - lowest_steps}")
