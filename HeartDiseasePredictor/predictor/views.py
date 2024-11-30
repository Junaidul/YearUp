from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from predictor.forms import HeartDiseaseForm


def heart(request):
    # Load the heart disease dataset
    df = pd.read_csv('static/Heart_train.csv')
    X = df.iloc[:, :-1].values  # Features
    Y = df.iloc[:, -1].values   # Target variable 

    prediction_result = None  # To display the prediction

    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            user_data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal']
            ]])

            # Train the model
            rf = RandomForestClassifier(
                n_estimators=16,
                criterion='entropy',
                max_depth=9
            )
            rf.fit(X, Y)  # Train
            prediction = rf.predict(user_data)  # Predict

            # Interpret the prediction
            print("Prediction:", prediction)
            prediction_result = "You have heart disease." if prediction[0] == 1 else "You do not have heart disease."

    else:
        form = HeartDiseaseForm()

    return render(request, 'heart.html', {
        'form': form,
        'prediction_result': prediction_result,
    })


def home(request):
    return render(request, 'home.html')


def explain(request):
    return render(request, 'explain.html')
