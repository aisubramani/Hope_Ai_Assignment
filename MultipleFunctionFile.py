class multipleFunction():
    ##Subfelds of AI
    def subfields():
        print("Sub-fields in AI are:")
        print(" Machine Learning")
        print(" Neural Networks")
        print(" Vision")
        print(" Robotics")
        print(" Speech Processing")
        print(" Natural Language Processing")
        
    #create funtion in odd or Even
    def oddEven():
        my_number=int(input("Enter Number:"))
        if((my_number%2)==0):
            print(my_number,"is Even Number")
            message="Even Number";
        else:
            print(my_number,"is Odd Number")
            message="Even Number";
        return message

    # create funtion Marriage Elegible
    def MarriageElegible():
        gender=str(input("Your Gender:"))
        age=int(input("Your Age:"))
        if(gender.lower()=="male"):
            if(age<21):
                print(gender.upper(),age,"age is NOT Eligible")
            else:
                print(gender.upper(),age,"age is Eligible")               
        if(gender.lower()=="female"):
            if(age<18):
                print(gender.upper(),age,"age is NOT Eligible")
            else:
                print(gender.upper(),age,"age is Eligible")

    #create Function Total percentage
    def percentage():
        total=0
        for i in range(1,6):
            subjectMark=int(input("Subject"+str(i)+"= "))
            total+=subjectMark
        print("Total : ",total)
        print("Percentage :",round((total/500)*100,2), "%")

    #create function Area formula and perimenter
    def Areaformula(Height,Breadth):
        print("Height:",Height)
        print("Breadth:",Breadth)
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth)/2)
        
    #create function Area perimenter
    def Perimeter(Height1,Height2,Breadth):
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:",Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Height1+Height2+Breadth)

    #create function BMI
    def BMI():
        my_bmi=float(input("Enter the BMI Index:"))
        if(my_bmi<18.5):
            print("You are 'Underweight' (BMI below 18.5)")
            message="You are 'Underweight' (BMI below 18.5"
        elif(my_bmi<24.9):
            print("You are 'Normal Range' (BMI 18.5-24.9)")
            message="You are 'Normal Range' (BMI 18.5-24.9)"
        elif(my_bmi<29.9):
            print("You are 'Overweight' (BMI 25-29.9)")
            message="You are 'Overweight' (BMI 25-29.9)"
        else:
            if(my_bmi<34.9):
                print("You are 'Obese Class I' (BMI 30-34.9)")
                message="You are 'Obese Class I' (BMI 30-34.9)"
            elif(my_bmi<39.9):
                print("You are 'Obese Class II' (BMI 35-39.9)")
                message="You are 'Obese Class II' (BMI 35-39.9)"
            else:
                print("You are 'Obese Class III' (BMI more than 40)")
                message="You are 'Obese Class III' (BMI more than 40)"
        return message

    