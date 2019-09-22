import random
import string


friend_list = ["danyal","shahbaz","arsalan","chaudary","akhter","adeen","shanza","abdullah","abdal","fashi","hassan","abdal",
"abdullah","ali","naqvi"]


random_string = ''.join(random.choices(string.ascii_lowercase, k = 6))
print(random_string)
for name in friend_list:
    score = 0
    for test_friendship in name:
        if test_friendship in "best":
            score += 25
        if test_friendship in "average":
            score += 15
        if test_friendship in "worst":
            score += -5
        if test_friendship in "enemy":
            score += -10
        if test_friendship in random_string:
            score += 25
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
