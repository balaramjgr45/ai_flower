from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = DecisionTreeClassifier(random_state=42)


# Train model
model.fit(X_train, y_train)


# Flower names
flower_names = iris.target_names


def predict_flower(sepal_length, sepal_width, petal_length, petal_width):

    data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(data)[0]

    flower_name = flower_names[prediction]

    return flower_name