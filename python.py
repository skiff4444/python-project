from cgi import print_arguments


print("Hello world")
print("It is Oleg")
print(3+6)
print(3+6+12)
print("Oleg" +" " + "has a " + "35 years")
name_user = input("Write your name:  ")
age_user = input("Write your age:  ")
city_user = input("Write your city: ")
print("Welcom " + name_user + " your age is " + age_user + " you from " + city_user)
input()

first_name = "Stepan"
last_name = "Bandera"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"
print(message)