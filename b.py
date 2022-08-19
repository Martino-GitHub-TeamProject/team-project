for _ in range(trial):
    doors = [0, 0, 1]  # 편의상 0은 염소, 1은 스포츠카로.
    random.shuffle(doors) # doors 리스트 내의 요소들을 마구 섞어주기
    user_choice = doors.pop() # 나의 선택과 동시에 doors에서는 해당 요소 제거
    doors.remove(0) # doors에 남은 요소 중 염소(0)를 제거
    if user_choice == 1:
        stay += 1 # 처음 선택에 머물렀을 때 스포츠카를 탄 것이므로 stay 경우의 수를 1 더해주기
    else:
        switch += 1 # 선택을 바꾸었어야 하므로 switch의 경우의 수를 1 더해준다.
