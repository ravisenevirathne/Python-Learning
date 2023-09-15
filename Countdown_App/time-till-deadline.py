import datetime

user_input = input("Enter your goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(input_list)
print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"\nDear user! time remaining for your goal: {goal} is {time_till.days} days")
