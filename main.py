from places import *
from suggestion import Suggestion
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/set_filter_preference', methods=['POST'])
def set_filter_preference():
    filter_preference = request.form['filter']
    print(f"Setting filter preference: {filter_preference}")  # Debugging line
    session['filter_preference'] = filter_preference
    return redirect(url_for('process'))

@app.route('/process', methods=['POST'])
def process():
    sug = Suggestion()

    filter_preference = request.form.get('filter', None)
    print(f"Processing filter preference: {filter_preference}")  # Debugging line

    if filter_preference is None:
        r1, r2, r3 = sug.make_suggestion([places_list])
        r1_tags = r1.tags_list
        r2_tags = r2.tags_list
        r3_tags = r3.tags_list
    else:
        if filter_preference == 'filter1': fil = 'Classics'
        elif filter_preference == 'filter2': fil = 'Take Out'
        else: fil = 'Date Night'

        filter_result = sug.filter(fil)
        r1, r2, r3 = sug.make_suggestion(filter_result)
        r1_tags = ' / '.join(r1.tags_list)
        r2_tags = ' / '.join(r2.tags_list)
        r3_tags = ' / '.join(r3.tags_list)



    return render_template('suggestion.html', r1=r1.name, r2=r2.name, r3=r3.name,
                           r1_tags=r1_tags, r2_tags=r2_tags, r3_tags=r3_tags)

@app.route('/gohome', methods=['POST'])
def go_home():
    session.pop('filter_preference', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
