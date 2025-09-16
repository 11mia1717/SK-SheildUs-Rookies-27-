##https://www.dailysecu.com/rssIndex.html

from flask import Flask, render_template, request
#render_template 렌더링을 보여줄때 템플릿으로 한다는 의미
import feedparser


app = Flask(__name__)

@app.route("/") 
def index(): 
    return render_template('index.html')
    
@app.route("/rss", methods=['GET', 'POST']) 
def rss(): 
    rss_url = request.form['rss_url'] #form 형식으로 데이터를 받음
    feed = feedparser.parse(rss_url)
    print(feed)
    return render_template('rss.html', feed=feed) #아래에 뜨는 피드를 피드로 보내드림
    

if __name__ == '__main__':
    app.run(debug=True) 
    #debug=True? 개발자형식, 변경사항을 바로 detect하여 reload함
    