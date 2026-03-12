def recommend(level):
    if level == 0:
        return "Fitness Level: Low\n• Walk 30 min daily\n• Drink water\n• Reduce stress"
    elif level == 1:
        return "Fitness Level: Medium\n• Cardio 4 days/week\n• Balanced diet\n• Increase steps"
    else:
        return "Fitness Level: High\n• Strength training\n• HIIT workouts\n• Maintain routine"