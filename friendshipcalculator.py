import random
import string


friend_list = ["danyal","shahbaz","arsalan","chaudary","akhter","adeen","shanza","abdullah","abdal","fashi"]
score = 0



for name in friend_list:
    for test_friendship in name:
        if test_friendship in "best":
            score += 10
        if test_friendship in "average":
            score += 5
        if test_friendship in "worst":
            score += -15
        else:
            score += 0
    if score >= 80:
        print(f"Your name is : {name} Your Score is : {score} ---------YOU ARE THE BEST FRIEND-------")
    elif score >= 50 and score < 80:
        print(f"Your name is : {name} Your Score is : {score} ---------YOU ARE THE AVERAGE FRIEND-------")
    elif score >= 30 and score < 50:
        print(f"Your name is : {name} Your Score is : {score} ---------YOU ARE THE WORST FRIEND-------")
    else:
        print(f"Your name is : {name} Your Score is : {score} ---------YOU ARE THE ENEMY-------")
