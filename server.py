from flask import Flask, request, render_template
from script import smallestSubString
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        Text = None
        try:
            Text = str(request.form["text"])
        except:
            errors += "<p>{!r} is not a alphabet.</p>\n".format(request.form["text"])
        if Text is not None:
            result = smallestSubString(Text)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your string:</p>
                <form method="POST">
                    <input name="text">
                    <input type="submit">
                </form>
            </body>
        </html>
    '''.format(errors=errors)
