#Store a user's input into variables and create a new output

#Exercise 1
print("LET'S PLAY MAD LIBS !!")

thing = input('Name an object in this room: ')
food = input('What kind of food do you like?: ')
color = input('What is your favorite color?: ')
animal = input('Enter an animal from the zoo: ')

print('The',animal,'jumped onto the',color,thing,
'and flew across the city to eat',food ,'at its favorite restaurant')

#Exercise 2
print("LET'S NOW PLAY POEM GENERATOR !!")

red = input('Enter something plural that is red. example roses :')
blue = input('Enter something plural that is blue. example violets :')
love = input('Enter something plural you love. example puppies :')
verb = input('Enter a verb. example jumping :')

print(red+' are red')
print(blue+ ' are blue')
print('I like baby '+love)
print('But not as much as I love' ,verb, 'with you!')

#Exercise 3
print("LET'S CALCULATE THE BILL")

bill = input('What is the total on the bill?:')
tip = input('What % tip would you like to give?:')
split = input('How many people are sharing the bill?:')

totalTip = round(float(bill)* float(tip)/100, 2)
totalBill = round(float(bill)+ totalTip, 2)
tipPer = round(totalTip/int(split),2)
totPer = round(totalBill/int(split),2)

print('Tip amount = $' , totalTip)
print('Total bill = $' , totalBill)
print('---------------------------')
print('Tip amount per person = $' , tipPer)
print('Total amount per person = $' , totPer)




