# write your code here
import random

def friends_dict():
    print("Enter the number of friends joining (including you):")
    friends_count = int(input())
    if friends_count < 1:
        print("No one is joining for the party")
        return

    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friends_count):
        friends[input()] = 0

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'Yes':
        names = list(friends.keys())
        lucky_one = random.choice(names)
        print(f"{lucky_one} is the lucky one!")
        bill_split = round(bill / (friends_count - 1), 2)
        for key in friends.keys():
            if key != lucky_one:
                friends[key] = bill_split


    else:
        print("No one is going to be lucky")
        bill_split = round(bill / friends_count, 2)
        for key in friends.keys():
            friends[key] = bill_split
    print(friends)

if __name__ == "__main__":
    friends_dict()
