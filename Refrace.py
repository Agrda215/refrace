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