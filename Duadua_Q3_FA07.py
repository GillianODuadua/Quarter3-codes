
# Dataset from Activity 1:
# Weekly test scores of 5 students (Math, Science, English)

scores = [
    [85, 90, 88],   # Student 1
    [78, 82, 80],   # Student 2
    [92, 95, 94],   # Student 3
    [70, 75, 72],   # Student 4
    [88, 84, 86]    # Student 5
]

print("Student Scores Summary:\n")

overall_max = scores[0][0]
overall_min = scores[0][0]

for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])
    
    total = sum(scores[i])
    average = total / len(scores[i])
    
    print("Total:", total)
    print("Average:", average)
    print()
    
    # Check for overall highest and lowest
    for value in scores[i]:
        if value > overall_max:
            overall_max = value
        if value < overall_min:
            overall_min = value

print("Highest score in dataset:", overall_max)
print("Lowest score in dataset:", overall_min)


# Reflection:
# Using a 2D array helped organize the scores clearly by student and subject.
# It made calculating totals and averages easier using loops.
# Finding the highest and lowest values was simple by checking each number.
# Arrays make summarizing data faster and more organized.
