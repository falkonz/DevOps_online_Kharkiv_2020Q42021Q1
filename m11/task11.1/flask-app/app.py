from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
  "https://img.buzzfeed.com/buzzfeed-static/static/2020-01/22/22/asset/de71054fd8a6/sub-buzz-1858-1579731628-8.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2020-01/23/0/asset/dff4b266d51f/sub-buzz-1980-1579740441-1.png?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-12/4/16/asset/79b290eb361c/sub-buzz-108-1575477628-4.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-10/9/14/asset/043617b3dae4/sub-buzz-4171-1570633017-1.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-09/6/13/asset/d50b54544bbf/sub-buzz-931-1567777611-1.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-06/27/14/asset/fede419893bd/sub-buzz-2963-1561644504-1.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2018-04/18/17/asset/buzzfeed-prod-web-06/sub-buzz-20002-1524085640-1.png?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2017-09/25/17/asset/buzzfeed-prod-fastlane-01/sub-buzz-9204-1506374597-3.png?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-05/29/20/asset/buzzfeed-prod-web-01/sub-buzz-25166-1559174431-1.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-10/2/18/asset/c5e27dbd3a6b/sub-buzz-3353-1570039704-1.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-06/3/10/asset/buzzfeed-prod-web-03/sub-buzz-8276-1559573886-7.jpg?downsize=600:*&output-format=auto&output-quality=auto",
  "https://img.buzzfeed.com/buzzfeed-static/static/2019-10/15/21/asset/c8dc66963464/sub-buzz-994-1571176687-2.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
]
@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
