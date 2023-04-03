# Most Frequent Character
# Ask the user to enter a String
# Find the Character that appears the most
# Create array for individual characters 
# Get the most frequent character's


val = 256
def string_mode(string):
    # Create array to keep the count of individual characters

    stringArray= [0]*val
    # variables to get most frequent character and it's count

    max_frequency = -1
    max_char=''

    # Traversing through the string and maintaining the count of each character

    for i in string:
        stringArray[ord(i)]+=1;
    #traversing through the count array to set maximum count and character

    for i in string:
        if max_frequency< stringArray[ord(i)]:
            max_frequency = stringArray[ord(i)]
            max_char=i
    #return value

    return max_char,max_frequency

#string to test

string = "frequent"
#accept return values

[a,b]=string_mode(string)
#print the result

print (" The most frequent character is "+a+" and the frequency of "+a+" is "+str(b))

            

