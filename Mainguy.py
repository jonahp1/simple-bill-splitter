attendees = int(input("How many people are splitting the bill? : "))
bill_total = float(input("How much is the bill total (before tax)? (DO NOT INCLUDE $) : "))
tax_total = float(input("How much is the Tax total? (DO NOT INCLUDE $) : "))

tax_percentage = (tax_total / bill_total) # useful for math
effective_tax_percentage = (tax_total / bill_total) * 100 # useful for human beings to look at
print("Effective Tax percentage is " + str(effective_tax_percentage))

for person in range(attendees):
    person += 1 # this is done so the count does not start at 0. (ie. so nobody is referred to as "Name 0" but rather Name 1 - Name [numb(attendees)]
    name = input("\nName of customer " + str(person) + ": ")
    cost = float(input("What was " + name + "'s cost as shown on the right hand side of check? (DO NOT INCLUDE $) : "))
    plus_tax = cost + (cost * tax_percentage)
    total_cost = plus_tax # this line is "theoretically unnecessary" but changing the variable name to "total cost" makes me feel better
    tipped = total_cost * .2 # some tip on tax, others do not. I usually do because worst case, you're giving more money to a person who literally just served you food. Algorithms should be grateful too
    tipped_total = tipped + total_cost
    print("\n" + name + "'s total cost after tax is $" + str(total_cost)+ "\n20% tip suggested at $" + str(tipped) + " tip. \n\nTotal for " + name + " INCLUDING tip: " + str(tipped_total) + "\n")
    running_total = total_cost
