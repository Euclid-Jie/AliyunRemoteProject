# -*- coding: utf-8 -*-
# @Time    : 2023/1/30 17:34
# @Author  : Euclid-Jie
# @File    : WebImgConver.py
from flask import Flask, request, send_file
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        # 转换图片格式
        img = Image.open(filename)
        new_filename = filename.split('.')[0]+'.png'
        img.save(new_filename)
        # 下载图片
        return send_file(new_filename, as_attachment=True)
    return '''
    <!doctype html>
    <html>
    <head>
        <title>图片转换</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 40px;
                color: #333;
            }
            form {
                display: inline-block;
                margin-top: 40px;
                padding: 20px;
                background-color: #f2f2f2;
                border-radius: 5px;
            }
            input[type="file"] {
                margin-bottom: 20px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #333;
                color: #fff;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>上传jpg格式图片，并将其转换为png格式</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="上传">
        </form>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
