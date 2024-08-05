from django.shortcuts import render
import pickle
from django.shortcuts import render
from django.http import JsonResponse


with open(
    "/home/ericmwangi/Documents/projects/flower_prediction/iris_model.pkl", "rb"
) as f:
    model = pickle.load(f)


def predict(request):
    if request.method == "POST":
        data = request.POST
        # Extract features from the request
        features = [
            float(data.get("sepal_length")),
            float(data.get("sepal_width")),
            float(data.get("petal_length")),
            float(data.get("petal_width")),
        ]
        # Make a prediction
        prediction = model.predict([features])
        return JsonResponse({"prediction": int(prediction[0])})
    return render(request, "predict.html")
