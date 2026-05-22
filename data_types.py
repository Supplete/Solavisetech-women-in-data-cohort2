#Personal Bio Generator

my_name="Trizah Nasumba"
my_age="21"
my_height="1.2"
Favorite_tech_field="Data Science and UX UI design"
Is_student="False"

print("My name is" + my_name +
    ",i am" + my_age +  "years old"
    "and my height is" + my_height + "metres"
    "my favorite tech field is "+ Favorite_tech_field +
    ", I am a student" + Is_student)


#Type Checker
School="Solavise tech"
print(type(School))
age=22
print(type(age))
Is_learning_data_science="True"
print(type(Is_learning_data_science))
height=2.2
print(type(height))


# Data conversion
#integer to string
num=54
result=str(num)
print(result)
#float to integer
num1=3.12
result1=int(num1)
print(result1)
#string number to integer
num2="45"
result2=int(num2)
print(result2)

#user information input
name=input("Enter your name:")
age=input("Enter your age:")
country=input("Enter your country:")
print("My name is" + name + ", I am " + age + " years old and I am from " + country)


#Temperature conversion
celsius=float(input("Enter temperature in Celsius:"))
fahrenheit=(celsius * 9/5) + 32 
print("Temperature in Fahrenheit:", fahrenheit)

