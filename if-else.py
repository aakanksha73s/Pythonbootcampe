age = int(input("enter the age"))
gender =input("enter the gender")
if(age > 17 and gender == "female"):
 print("you are eligible govt job")
elif(age > 17 and gender == "male"):
 print("you are eligible private job")
else:
 print("you are not eligfible for any job")