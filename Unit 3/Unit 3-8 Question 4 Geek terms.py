geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
"Googling": "searching the Internet for background information on a person.",
"Keyboard Plaque" : "the collection of debris found in computer keyboards.",
"Link Rot" : "the process by which web page links become obsolete.",
"Percussive Maintenance" : "the act of striking an electronic device to make it work.",
"Uninstalled" : "being fired.  Especially popular during the dot-bomb era."} 

def main():
   while True:
      #Selection menu
      print("GEEK TRANSLATOR\n")
      print("1 - Look up a Geek Term")
      print("2 - Add a Geek Term")
      print("3 - Redefine a Geek Term")
      print("4 - Delete a Geek Term")
      print("5 - Quit")
      
      #Input validation
      while True:
         choice = input("\nChoice: ")
         if choice.isdigit() == True:
            choice = int(choice)
            if choice < 1 or choice > 5:
               print("Sorry, thats not a valid choice. Please try again.")
            else:
               break
         else:
            print("Sorry, thats not a valid choice. Please try again.")
              
      if choice == 5:
         break
      term = input("Term: ")
      choices(choice, term)
      print("\n")
        
def choices(choice, term):
   if choice == 1:
        #Search for term and definition of a term. If term doesn't exist, prints "Sorry, I don't know that term"
      if term in geek:
         print("Definition: " + geek[term])
      else:
            print("Sorry, I don't know that term.")
   elif choice == 2:
        #Adds a geek term
      if term not in geek:
         definition = input("Definition(of new word): ")
         geek[term] = definition
         print("The term has been added.")
      else:
            print("That term already exists!  Try redefining it.")
   elif choice == 3:
        #redefines a term
      if term in geek:
         print("Definition: " + geek[term])
         newDef = input("New Definition: ")
         geek[term] = newDef
         print("Term has been redefined")
      elif term not in geek:
            print("That term doesn't exist! Try adding it.")
   elif choice == 4:
        #deletes a geek term
      if term in geek:
         del geek[term]
         print("Okay, I deleted that item.")
      elif term not in geek:
         print("Sorry, I don't know that term.")
            
main()

                    