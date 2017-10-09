from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color']
    if color == 'pink':
        reply = "Thats my favorite color too!"
    else:
        reply = "My favorite color is pink."
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
