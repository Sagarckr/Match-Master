from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Mumbai Indians',
    'Chennai Super Kings',
    'Royal Challengers Bangalore',
    'Kings XI Punjab',
    'Kolkata Knight Riders',
    'Sunrisers Hyderabad',
    'Rajasthan Royals',
    'Delhi Capitals',
    'Gujarat Titans',
    'Lucknow Super Giants'
]

cities = [
    'Ahmedabad', 'Chennai', 'Mumbai', 'Bengaluru', 'Delhi', 'Dharamsala', 
    'Hyderabad', 'Lucknow', 'Jaipur', 'Chandigarh', 'Guwahati', 'Kolkata', 
    'Navi Mumbai', 'Pune', 'Dubai', 'Abu Dhabi', 'Sharjah', 'Visakhapatnam', 
    'Indore', 'Kanpur', 'Bangalore', 'Rajkot', 'Raipur', 'Ranchi', 
    'Cuttack', 'Nagpur', 'Johannesburg', 'Centurion', 'Durban', 
    'Bloemfontein', 'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    form_data = {}

    if request.method == 'POST':
        try:
            form_data['batting_team'] = request.form['batting_team']
            form_data['bowling_team'] = request.form['bowling_team']
            form_data['city'] = request.form['city']
            form_data['current_score'] = int(request.form['current_score'])
            form_data['overs'] = float(request.form['overs'])  # Use float if fractional overs are allowed
            form_data['wickets'] = int(request.form['wickets'])
            form_data['last_five_over_score'] = int(request.form['last_five_over_score'])
            form_data['last_five_over_wicket'] = int(request.form['last_five_over_wicket'])
            
            # Calculations
            balls_left = 120 - int(form_data['overs'] * 6)  # Ensure correct calculation of balls left
            wickets_left = 10 - form_data['wickets']
            crr = form_data['current_score'] / form_data['overs'] if form_data['overs'] > 0 else 0  # Avoid division by zero

            input_df = pd.DataFrame({
                'batting_team': [form_data['batting_team']],
                'bowling_team': [form_data['bowling_team']],
                'city': [form_data['city']],
                'current_score': [form_data['current_score']],
                'balls_left': [balls_left],
                'wickets_left': [wickets_left],
                'crr': [crr],
                'last_five_over_score': [form_data['last_five_over_score']],
                'last_five_over_wicket': [form_data['last_five_over_wicket']]
            })

            result = pipe.predict(input_df)
            prediction = int(result[0])

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index3.html', teams=sorted(teams), cities=sorted(cities), prediction=prediction, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
