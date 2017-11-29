# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

def scores_grades(total):
    import random
    for i in range(1,total + 1):
        score = int(random.random()*60 + 40)
        if score < 50:
            print "Score: " + str(score) + "; You have been forcibily dropped from the class."
        elif score < 60:
            print "Score: " + str(score) + "; Your grade is an F."
        elif score < 70:
            print "Score: " + str(score) + "; Your grade is a D."
        elif score < 80:
            print "Score: " + str(score) + "; Your grade is a C."
        elif score < 90:
            print "Score: " + str(score) + "; Your grade is an B."
        else:
            print "Score: " + str(score) + "; Your grade is an A. I love you."

scores_grades(10)