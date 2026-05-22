#favourite tools list
favourite_tools = ["hammer", "screwdriver", "wrench", "pliers", "drill"]
#add items to the list
favourite_tools.append("saw")
favourite_tools.append("level")
print(favourite_tools)
#remove items from the list
favourite_tools.remove("hammer")
print(favourite_tools)
#accessing list items
print(favourite_tools[0])
print(favourite_tools[2])
#length of the list
print(len(favourite_tools))

#student score from highest lowest avarage scores
scores = [85, 92, 78, 90, 88]
#sort the scores in descending order
scores.sort(reverse=True)
print("Sorted scores (highest to lowest):", scores)
print("Highest score:", scores[0])
print("Lowest score:", scores[-1])
print("Average score:", sum(scores) / len(scores))

#shopping list manager
shopping_list = ["milk", "bread", "eggs", "fruits", "vegetables"]
#add items to the shopping list
shopping_list.append("cheese")
shopping_list.append("yogurt")
print("Shopping list:", shopping_list)
#remove items from the shopping list
shopping_list.remove("bread")   
print("Updated shopping list:", shopping_list)
#accessing shopping list items
print("First item on the shopping list:", shopping_list[0])
print("Last item on the shopping list:", shopping_list[-1])
print("Total items in the shopping list:", len(shopping_list))

#country capitals dictionary
country_capitals = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dodoma"
}
print("Country capitals:", country_capitals)
#accessing dictionary items
print("Capital of Kenya:", country_capitals["Kenya"])
print("Capital of Uganda:", country_capitals["Uganda"])
print("Capital of Tanzania:", country_capitals["Tanzania"])
#adding a new country and its capital
country_capitals["Rwanda"] = "Kigali"
print("Updated country capitals:", country_capitals)
#removing a country and its capital
del country_capitals["Tanzania"]
print("Updated country capitals after removal:", country_capitals)

#unique visitors removed duplicates sets
unique_visitors = {"Alice", "Bob", "Charlie", "Alice", "Bob"}
print("Unique visitors:", unique_visitors)

#common skills set operations
skills_set1 = {"Python", "Data Analysis", "Machine Learning"}
skills_set2 = {"Python", "Web Development", "UI/UX Design"}
#union of skills
all_skills = skills_set1.union(skills_set2)
print("All skills:", all_skills)
#intersection of skills
common_skills = skills_set1.intersection(skills_set2)
print("Common skills:", common_skills)
#difference of skills
unique_skills_set1 = skills_set1.difference(skills_set2)
print("Unique skills in set1:", unique_skills_set1)

#student record create and display a student dictionary
student_record = {
    "name": "Trizah Nasumba",
    "age": 21,
    "grade": "A",
    "courses": ["Data Science", "UX/UI Design", "Python Programming"]
}

print("Student Record:")
print("Name:", student_record["name"])
print("Age:", student_record["age"])
print("Grade:", student_record["grade"])
print("Courses:", ", ".join(student_record["courses"]))

#mini contact book search and store contact
contact_book = {
    "Alice": "alice@gmail.com",
    "Bob": "bob@yahoo.com",
    "Charlie": "charlie@outlook.com"
}
print("Contact Book:")
for name, email in contact_book.items():
    print(name + ":", email)
#search for a contact
search_name = input("Enter the name of the contact to search: ")
if search_name in contact_book:
    print(search_name + ":", contact_book[search_name])
else:
    print("Contact not found.")