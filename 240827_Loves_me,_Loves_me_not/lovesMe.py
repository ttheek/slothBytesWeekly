import sys

def loves_me(petals):
    phrases = []
    
    for i in range(petals):
        if i % 2 == 0:
            phrase = "Loves me"
        else:
            phrase = "Loves me not"
        
        if i == petals - 1:
            phrase = phrase.upper()
        
        phrases.append(phrase)
    
    return ', '.join(phrases)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        petals = int(sys.argv[1])
        print(loves_me(petals))
    else:
        print("Please provide the number of petals.")
