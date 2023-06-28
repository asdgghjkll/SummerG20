import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 文件路径
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SEARCH_FOLDER = os.path.join(ROOT_DIR, 'search')

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 搜索文件
@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = []
    for root, dirs, files in os.walk(SEARCH_FOLDER):
        for file in files:
            filepath = os.path.join(root, file)
            if keyword in file:
                results.append(filepath)
    return render_template('search.html', keyword=keyword, results=results)

if __name__ == '__main__':
    app.run()
