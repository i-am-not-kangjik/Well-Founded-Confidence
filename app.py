# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    f1 = request.form['feature1']
    f2 = request.form['feature2']
    f3 = request.form['feature3']
    f4 = request.form['feature4']
    f5 = request.form['feature5']
    

    # 파이썬 함수 실행
    result = model_pred(f1, f2, f3, f4, f5)
    return render_template('result.html', result=result)

def model_pred(f1, f2, f3, f4, f5):
    # 받은 데이터를 가지고 작업을 수행하는 파이썬 함수
    # 여기에서는 입력한 이름과 이메일을 합쳐서 반환하는 예제
    return f"f1 = {f1}, f2 = {f2}, f3 = {f3}, f4 = {f4}, f5 = {f5}"

if __name__ == '__main__':
    app.run()
