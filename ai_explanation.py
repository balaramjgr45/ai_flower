def explain_prediction(
    flower,
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
):

    if flower == "setosa":

        explanation = (
            "The model predicted Setosa because the flower has "
            "relatively small petal measurements. "
            "These characteristics are commonly found in Iris Setosa."
        )

    elif flower == "versicolor":

        explanation = (
            "The model predicted Versicolor because the petal "
            "measurements are generally larger than Setosa but "
            "smaller than many Virginica flowers."
        )

    else:

        explanation = (
            "The model predicted Virginica because the flower "
            "has relatively large petal measurements, which are "
            "commonly associated with Iris Virginica."
        )

    return explanation