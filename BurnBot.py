from datetime import datetime
Age = int(input("What is your age?: "))
Birthplace = input("Where were you born?: ")
Hobby = input("What is your favorite hobby?: ")
Food = input("What is your favorite food?: ")
Job = input("What Career are you in or going into?: ")
now = datetime.now()
Year = now.year
Birthyear = Year - Age
print("Well, I was going to ask your name after you so kindly provided all that wonderful personal information but thats all I'll need")
print("--------------")
print("Thinking......")
print("--------------")
print("Like seriously, you're", Age, "years old and still bother being interested in", Hobby, "? Come on, it's", Year, "Just move on already!")
if Age > 18:
    print("I bet with all the money that you've dumped into", Hobby, "and studying", Job, "you still have to live on your parrent's couch in", Birthplace)
    print("At this point kids will use", Birthyear, "To lie about their age on random website signups, Give it up already senior citizen")
else:
    print("With all the money your parrents have probably spent on your beloved", Hobby, "and you going into ", Job, "they wont even be able to afford letting you move out if they wanted to")
    print("How did a ", Age, "year old kid even manage to run this program, you probably sit around and eat", Food, "all day instead of doing something productive")
