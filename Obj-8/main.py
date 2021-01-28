#Song For Days Of Christmas
day = 12

#Storage For Every Day & Song Line
days_dict = {1: "First", 2:"Second", 3:"Third", 4:"Forth", 5: "Fith", 6: "Sixth", 7:"Seventh", 8:"Eigth", 9:"Ninth", 10:"Tenth", 11:"Eleventh", 12:"Twelth"}
days_list = ["And a Partridge in a Pear Tree!", "Two Turtle Doves", "Three French Hens", "Four Calling Birds", "Five Gooooooooolden Rings", "Six Gweese a Laying", "Seven Swans a Swimming", "Eight Maids a Milking", "Nine Ladies Dancing", "Ten Lords a Leaping", "Eleven Pipers Piping", "Twelve Drummers Drumming"]

#Output
print("On the",days_dict[day],"Day Of Christmas,")
print("My True Love Gave To Me...")
result = days_list[day-1::-1]

if day == 1:
  print("A partrige in a pear tree!")
else:
  for item in result:
    print(item)