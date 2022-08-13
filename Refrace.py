score = 0
highscore = 0
top = 0
bottom = 0
i = 0

print("Hello 4000 Scores! of Where Of Reface.")
print("Whoah Here Based in here.")
print("Top:",top)
print("Bottom:", bottom)
print("Score:", score)
print("Inputed:")
inputed = input()

def printing():
    print("Top:",top)
    print("Bottom:", bottom)
    print("Score:", score)
    print("Inputed:")
    inputed = input()

if top >= int(inputed):
    score = score + 1
    top = top + 2
    bottom = bottom + 2
    printing()
else:
    print("Whoah than ", top)

# Automatticy Score Animation
while i < 4000:
    if top >= int(inputed):
       score = score + 1
       top = top + 2
       bottom = bottom + 2
       printing()
       i += 1
    else:
       print("Whoah than ", top)

# Win but where 4000 Scores.
if score > 4000:
    print("You Win Get Resources but of year than 2022 You Be Created!")
    print("You Are Maxium The 4 Digit Number be best: 9999.")
    print("With pauses this while loop.")

# Resources Be Of Than here 4000 score to finsh.
