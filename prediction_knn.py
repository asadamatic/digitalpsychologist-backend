import pickle
def evaluate_stress(list):
    # list is the variable we need to input from the Flutter application in form of JSON and convert it into 2D array
    loaded_model = pickle.load(open('trained_model.sav', 'rb'))

    # this is the variable that will provide us with the PSS score which wil be used to display stress level in the application
    result = loaded_model.score(list)
    return result
