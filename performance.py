#Performance Task
def medical_help(illness):
    medical_advice = {
        "covid-19": ["To treat yourself, do this: ", "Over-the-counter medications like acetaminophen and ibuprofen can help relieve fever and body aches.", "Staying hydrated is important.", "It is also important to avoid high-sugar drinks and processed foods."  ], 
        "flu": ["To treat yourself, do this: ", "Nasal Spray and humidifiers can relieve congestion and discomfort.", "Use cough suppressants for dry coughs or expectorants to loosen mucus in the throat.", "Natural remedies include chicken soup, ginger tea, and zinc supplements which may help ease symptoms and support immune function" ],
    } #This list function uses a dictionary to store the medical advice for each illness, and it will allow the user to easily access the advice for the illness they are asking about.
    if illness == "allergies":
        allergy_type = input("What are you allergic to? (pollen/peanuts/pet dander) ")
        if allergy_type == "pollen":
            print("To treat pollen allergies, try to stay indoors on high pollen days, keep windows closed, and use air conditioning. Over-the-counter antihistamines can also help relieve symptoms.")
        elif allergy_type == "peanuts":
            print("To treat peanut allergies, avoid all peanut products and read ingredient labels carefully. Carry an epinephrine auto-injector if prescribed by a doctor.")
        elif allergy_type == "pet hair":
            print("To treat pet hair allergies, keep pets out of bedrooms, wash hands after petting animals, and consider using air purifiers. Regular grooming of pets can also reduce hair shed.")
        else:
            print("Sorry, we don't have specific advice for that allergen.")
        return
    if illness in medical_advice:
        for line in medical_advice[illness]:
            input(line) #This if statement checks if the illness that the user is asking about is in the medical advice dictionary, and if it is, it will print out the advice for that illness. 
    else:
        print("Sorry, we don't have treatment for that illness.") # This else statement will print out a message if the user asks about an illness that is not in the medical advice dictionary.
print("Welcome! We are here to help you with medical advice!") #This prints the welcome message for the user when they start the program.
choice = input("Do you need medical assistance? (yes/no) ")#the 'choice=input' allows for the user to input whether they need medical assistance or not, and it will determine the flow of the program based on their answer.
if choice == "no":
    print("Okay, stay healthy and fit!") # This if statement will end the program if the user does not need medical help.
while choice == "yes":
    print("We are here to help you!")
    question = input("Do you need help with a covid-19, flu, or allergies? ")
    medical_help(question)
    choice = input("Do you need more medical advice? (yes/finished) ") # This while loop uses the 'choice=input' to allow the user to ask for more medical advice if they need it, and it will continue to loop until the user is finished asking for medical advice.
if choice == "finished":
    rate = int(input("Please rate our service 1-10! ")) # "int(input" allows the user to input a rating for the service, and it will convert that input into an integer so that it can be used to calculate the final score.)"
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend our service to a friend? (yes/maybe/no) ") #the friend=input allows the user to input whether they would recommend the service to a friend or not, and it will determine the final message that the program will print out based on their answer.

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry we could not meet your expectations. ") #this if/else statement will print out a message based on whether the user would recommend the service to a friend or not, and it will thank them if they would recommend it, or apologize if they would not recommend it.