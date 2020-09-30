from flask import Flask, render_template, url_for

app = Flask(__name__)


info = [
	{
	"device": "Catalyst9300",
	"ip": "192.168.1.2"
	},
	{
	"location": "global/US/Texas/Dallas/HQ",
	"contact": "Garrett Caudle | gcaudle@cisco.com"
	}
]


@app.route("/home")
@app.route("/")
def home():
	return render_template("home.html", posts=info, title="Home Page")

@app.route("/about")
def about():
	return render_template("about.html")


	if __name__ == "__main__":
		app.run(debug=True)