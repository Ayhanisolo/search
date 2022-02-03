from flask import Flask, render_template
app = Flask(__name__)
@app.route('/blog_news')
def my_home():
	return render_template('data_info.csv')


