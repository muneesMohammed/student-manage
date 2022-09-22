
student=[]
while True:
   print("1.add student ")
   print("2. view all student ")
   print("3. exit ")

   choice=int(input("select a choice "))
   
   if choice==1:
       getName=str(input("enter a name "))
       getRoll=int(input("enter roll number "))
       getAdmission=int(input("enter admission number "))
       getCollege=str(input("enter college name "))
       data={'name':getName,'roll':getRoll,'addmissionNo':getAdmission,'college':getCollege}
       print(data)
       student.append(data)
      
   elif choice==2:
       print(student)
   else:
       break  
       