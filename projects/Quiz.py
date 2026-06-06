questions=[{"Question":"Which state of matter has a definite volume but takes the shape of its container?",
           "Option":["A. Solid",
            "B. Liquid",
            "C. Gas",
            "D. All of the above"],
           "answer":"B"},
          {"Question":"What happens to the movement of particles in a substance when it is heated?",
           "Option":["A. The particles moves clower and closer together",
            "B. The particles moves faster ans spreas further apart ",
            "C. The particles turn into entirely new elements.",
            "D. Ther particles stop moving completely"],
           "answer":"B"}, 
          {"Question":"What is the hottest planet?",
           "Option":["A. Mars",
            "B. Earth",
            "C. Mercury",
            "D. Venus"],
           "answer":"D"},
          {"Question":"What is the smallest planet?",
           "Option":["A. Earth",
            "B. Mars"
            "C. Mercury",
            "D. Venus"],
           "answer":"C"}]
  
for i in questions:
   print("\n" + i["Question"])
   for j in i["Option"]:
      print(j)
      
user_answer= input("Enter your answer:").upper()
  
if user_answer==i["Question"]:
    print("correct")
    score+=1
else:
    print("Wrong Answer")
    print("Correct amswer is:",i["answer"])
print("Quize Over!!")
print("Your Score is:",score)