import random

count_stay = 0 # 변경하지 않았을 때 정답 횟수
count_change = 0 # 변경했을 떄 정답 횟수
count = 0

#박스 생성
def create_box():
    box = [0,0,0]
    answer = random.randrange(0,3)
    box[answer] = 1
    return box, answer

def choice_not_answer(box, first_choice):
    for i, e in enumerate(box):
        if(first_choice != i and e == 0):
            k = i
            break
    return k

def change_choice(box, first_choice, box_open):
    for i, e in enumerate(box):
        if(i != first_choice and i != box_open):
            second_choice = i
            break
    return second_choice


##### main #####
TestCase = int(input("Test case : "))
while count < TestCase:
    box, answer = create_box()
    first_choice = random.randrange(0,3)
    box_open = choice_not_answer(box, first_choice)
    second_choice = change_choice(box, first_choice, box_open)
 
    if(box[first_choice] == 1):
        count_stay+= 1
    elif(box[second_choice] == 1):
        count_change += 1

    count +=  1

print("정답을 바꾸지 않았을 떄 : %d" % (count_stay))
print("정답을 바꿧을 때 : %d" % (count_change))

