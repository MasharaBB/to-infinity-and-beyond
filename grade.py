def computegrade(score):
    try:
        score = float(score)
    except:
        print("Error. Score must be a number")
        quit()
    if score < 0.0 or score > 1.0:
        print("Error. Score out of range")
    elif score >= 0.9:
        print("Grade: A")
    elif score >= 0.8:
        print("Grade: B")
    elif score >= 0.7:
        print("Grade: C")
    elif score >= 0.6:
        print("Grade: D")
    else:
        print("Grade: F")
score_in = input("Please enter the score: ")
computegrade(score_in)