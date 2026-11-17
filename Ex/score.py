# input score from user
score = float(input("Input score: "))

# ប្រើប្រាស់ Condition Statement ដើម្បីវាយតម្លៃនិទ្ទេស
if 80 <= score <= 100:
    print(f"Grade: {score}, A")
elif 60 <= score < 80:
    print(f"Grade: {score}, B")
elif 50 <= score < 60:
    print(f"Grade: {score}, C")
elif 30 <= score < 40:
    print(f"Grade: {score}, D")
elif 0 <= score < 30:
    print(f"Grade: {score}, F (false)")
else:
    print("Invalid score! Please enter a score between 0 and 100.")