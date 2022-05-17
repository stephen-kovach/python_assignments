from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "marcusaureliusthebestrevengeisnotobelikethat"

import random  


@app.route("/")
def index():
    if "comp_guess" not in session:

        session["comp_guess"] = random.randint(1, 100)
    return render_template('index.html', message = session["message"])

@app.route('/process_guess', methods=["POST"])
def processing():  
    print(request.form["user_guess"]) 

    if len((request.form["user_guess"])) < 1:
        print("C'mon!  Make a guess!")
        session["message"] = "Ah C'mon!  Just guess already!" # added 19 31:35
        return redirect("/")
    user_guess = int(request.form["user_guess"])

    print(user_guess)
    # Do the same for session["comp_guess"]
    comp_guess = session["comp_guess"]
    print(comp_guess)
    # 19 22:50 Comparing our Computer Number with User Guess
    if user_guess < comp_guess:
        print("================================You low balled it!")
        session["message"] = "Haha!  You low balled it!" # added 19 31:35
    elif user_guess > comp_guess:
        print("================================Nope!  Too high!")
        session["message"] = "Haha!  Nope! Too high!" # added 19 31:35
    else: # 19 25:07 HEY!  Print needs to be on lower line!
        session["message"] = "Awesome!  Nailed it!" # added 19 31:35 
        print("================================Nailed it!")
        return redirect("/")


@app.route("/reset")
def reset_session():
    session.clear()

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

# 19 39:44, skipping CSS
# 19 39:50, let know users how many times they have guessed 
        # MAKE A COUNTER!

# I like working with python because of the diagnostics in terminal
# And because comments are easier/more fluid

#