class Student():
    # def __init__(self,roll_no,stud_name):
    #     self.roll_no=roll_no
    #     self.stud_name=stud_name

    roll_no=10
    stud_name='sreelu'
    def get_data(self):
        self.roll_no=int(input('Enter your Roll Number: '))
        self.stud_name=input('Enter your name: ')
        # print('roll number is',self.roll_no)
        # print('name is',self.stud_name)
    def print_data(self):
        print('roll number is',self.roll_no)
        print('name is',self.stud_name)


details= Student()

print(details.roll_no)
details.get_data()
details.print_data()

class Marks(Student):
    def __init__(self,mark1,mark2,mark3,mark4,mark5,mark6,summ):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5
        self.mark6=mark6        
    def input_data(self,mark1,mark2,mark3,mark4,mark5,mark6):
        print('Phy mark is',self.mark1)
        print('CHem mark is',self.mark2)
        print('Math mark is',self.mark3)
        print('Bio mark is',self.mark4)
        print('IT mark is',self.mark5)
        print('Eng mark is',self.mark6)
Phy=int(input('Enter your phy mark: '))
Chem=int(input('Enter your chem mark: '))
Math=int(input('Enter your math mark: '))
Bio=int(input('Enter your bio mark: '))
IT=int(input('Enter your IT mark: '))
Eng=int(input('Enter your eng mark: '))
# x=Marks(mark1,mark2,mark3,mark4,mark5,mark6)
# print(x.mark1)
x= Marks(Phy,Chem,Math,Bio,IT,Eng)
x.input_data(Phy,Chem,Math,Bio,IT,Eng)

