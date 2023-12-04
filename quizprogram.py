questions = {}
questions["what is the name of prime minister of india"] = "narandra modi"
questions["Who is called The Father Of Nation in India"] = "Gandhi"
questions["Who is Carl Sagan"] = "Very Good Scientist"


count = 0
for key,values in questions.items():
    print(key)
    ans = input("\nEnter Answer")
    ans = ans.lower()
    values = values.lower()
    if(ans==values):
        print("Correct\n")
        count-=1;
    else:
        print("Wrong Ans")