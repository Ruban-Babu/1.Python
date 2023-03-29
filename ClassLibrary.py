class Library():
    
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
    def OddEven():
            num=int(input("Enter a number: "))
            if((num%2)==0):
                print(num," is Even Number")
            else:
                print(num," is Odd Number")
                
    def Eligible():
            gender=input("Your Gender: ")
            age=int(input("Your Age: "))
            if(gender=="Male" and age>=21):
                print("ELIGIBLE")
            elif(gender=="Female" and age>=18):
                print("ELIGIBEL")
            else:
                print("NOT ELIGIBLE")
                
    def Percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        add=sub1+sub2+sub3+sub4+sub5
        print("Total :",add)
        percentage=(add/500) * 100
        print("Percentage :",percentage)
        
    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        area=(Height*Breadth)/2
        print("Area of Triangle: ",area)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle: ",perimeter)