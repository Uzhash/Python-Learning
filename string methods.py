# Strings are immutable in python
a="Uzaib !!!!!!!!!"
print(a.rstrip("!")) # removes the trailing exclamation marks
print(len(a))
print(a.upper()) 
print(a.lower())
print(a.replace("Uzaib","Ahmed"))
print(a.split(" "))
websitePage="introduction to page"
print(websitePage.capitalize())
print(a.count("Uzaib")) # counts the number of occurrences of "Uzaib" in the string a
# str1="AbcDefGhIjK"
# print(str1.upper())
# print(str1.lower())
str2="Welcome to the console!"
print(len(str2))
print(len(str2.center(60,"#"))) # centers the string and fills the remaining space with asterisks

str3="Welcome to the website***"
print(str3.endswith("***")) # checks if the string ends with "***"
print(str3.startswith("To")) # checks if the string starts with "Welcome"
print(str3.startswith("To",3,6)) # checks if the string starts with "Welcome"

str4="He's name is Ali. He is an honest person"
print(str4.find("ishhh"))
# print(str4.index("ishhh"))

str5="Welcometoconsole"
print(str5.isalnum()) # checks if all characters in the string are alphanumeric (letters and numbers)

str6="Welcome to the console"
print(str6.isalpha())

str7="uzaib akhtar"
print(str7.islower()) # checks if all characters in the string are lowercase

str8="Wishing you a very Happy Birthday\n"
print(str8.isprintable()) # checks if all characters in the string are printable

str9="                "
print(str9.isspace()) # checks if all characters in the string are whitespace

str10="To kill a mocking bird"
print(str10.istitle())

str11="PYTHON IS AN EASY LANGUAGE"
print(str11.swapcase()) # converts uppercase letters to lowercase and vice versa

str12="He's name is Ali. He is an honest person"
print(str12.title()) # converts the first character of each word to uppercase and the rest to lowercase

