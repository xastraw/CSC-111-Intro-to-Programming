from flask import Flask, request
import random

app = Flask(__name__)

houses = ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"]
colors = [["green", "silver"],["red", "gold"],["yellow", "black"],["blue", "bronze"]]
traits = ["ambition", "bravery", "empathy", "intelligence"]

@app.route('/')
def home():
    return HOME_HTML

HOME_HTML = """
    <html><body>
        <h2>Welcome to the Greeter</h2>
        <form action="/greet">
            What's your name? <input type='text' name='username'><br>
            What's your favorite color? <input type='text' name='favcolor'><br>
            What of these is your strongest trait: Ambition, Bravery, Empathy, Intelligence <input type ='text' name='trait'><br>
            <input type='submit' value='Continue'>
        </form>
    </body></html>"""

def decider(user, color, trait):
    
    housecolor = 10
    housetrait = 10
    chosenhouse = 10

    for t in range(0,4):
        if color in colors[t]:
            housecolor = t

    for i in range(0,4):
        if traits[i] == trait:
            housetrait = i

    user = user.lower()
    if user == "harry potter":
        housetrait = 1
        housecolor = 1


    if housecolor==0 or housetrait==0:
        #slytherin
        chosenhouse = houses[0]
        housecolor+=5
        housetrait+=5
    elif housecolor==1 or housetrait==1:
        #griffendor
        chosenhouse = houses[1]
        housecolor+=5
        housetrait+=5
    elif housecolor==2 or housetrait ==2:
        #hufflepuff
        chosenhouse = houses[2]
        housecolor+=5
        housetrait+=5
    elif housecolor==3 or housetrait==3:
        #ravenclaw
        housecolor+=5
        housetrait+=5
        chosenhouse = houses[3]
    else:
        #randomly decides one if users inputs arent in lists
        r = random.randint(0,3)
        chosenhouse = houses[r]
    
    return chosenhouse


@app.route('/greet')
def greet():

    username = request.args.get('username', '')
    favcolor = request.args.get('favcolor', '')
    favcolor = favcolor.lower()
    strongtrait = request.args.get('trait', '')
    strongtrait = strongtrait.lower()
    
    if username == '':
        username = 'Unnamed Person'
    if favcolor == '':
        favcolor = "10"
    if strongtrait == '':
        strongtrait = "10"
    
    house = decider(username, favcolor, strongtrait)

    return GREET_HTML.format(username, house)

GREET_HTML = """
    <html><body>
        <h2>Hello Wizard  {0}!</h2>
        The house you will be in is {1}
    </body></html>
    """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)