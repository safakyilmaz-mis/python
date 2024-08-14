from flask import Flask, redirect, request, Response, render_template, url_for
 
app = Flask(__name__)

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

all_books = []


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        rating = request.form['rating']
        all_books.append({'book_name': book_name, 'author_name': author_name, 'rating': rating})
        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)