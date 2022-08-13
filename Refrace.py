score = 0
highscore = 0
top = 0
bottom = 0

print("Hello 4000 Scores! of Where Of Reface.")
print("Whoah Here Based in here.")
print("Top:",top)
print("Bottom:", bottom)
print("Score:", score)
print("Inputed:")
inputed = input()

def printing():
    score += 1
    print("Top:",top)
    print("Bottom:", bottom)
    print("Score:", score)
    print("Inputed:")
    inputed = input()

if top >= inputed:
    printing()
else:
    print("Whoah than ", top)
