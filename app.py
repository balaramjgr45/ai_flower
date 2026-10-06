from flask import Flask, render_template, request

from model import predict_flower
from ai_explanation import explain_prediction


app = Flask(__name__, static_folder="templates/static")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    explanation = None
    error = None

    if request.method == "POST":

        try:

            sepal_length = float(request.form["sepal_length"])
            sepal_width = float(request.form["sepal_width"])
            petal_length = float(request.form["petal_length"])
            petal_width = float(request.form["petal_width"])


            # ML prediction
            prediction = predict_flower(
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            )


            # AI explanation
            explanation = explain_prediction(
                prediction,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            )

        except ValueError:

            error = "Please enter valid numbers."


    return render_template(
        "index.html",
        prediction=prediction,
        explanation=explanation,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)