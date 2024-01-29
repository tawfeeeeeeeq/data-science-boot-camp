# This program determines the award a person competing in a triathlon will receive.

# Read in the time for the Swimming event
event1  = int(input("Finish time Swimming : "))
# Read in the time for the Swimming event
event2  = int(input("Finish time Cycling : "))
# Read in the time for the Swimming event
event3  = int(input("Finish time Running : "))

totaltime = event1+event2+event3
print("Total time: ", totaltime, " minutes")

if totaltime >= 0 and totaltime <= 100:
    print("Award received: ", "Provincial Colours")
elif totaltime >= 101 and totaltime <= 105:
    print("Award received: ", "Provincial Half Colours")
elif totaltime >= 106 and totaltime <= 110:
    print("Award received: ", "Provincial Scroll")
else:
    print("Award received: ", "No Award")