# app.py
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
best_model = joblib.load('best_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    form_data = []
    form_data.append(request.form['feature1'])
    form_data.append(request.form['feature2'])
    form_data.append(request.form['feature3'])
    form_data.append(request.form['feature4'])
    form_data.append(request.form['feature5'])
    form_data.append(request.form['feature6'])
    form_data.append(request.form['feature7'])
    form_data.append(request.form['feature8'])
    form_data.append(request.form['feature9'])
    form_data.append(request.form['feature10'])
    form_data.append(request.form['feature11'])
    form_data.append(request.form['feature12'])
    form_data.append(request.form['feature13'])
    
    test = np.array(form_data).reshape(1, -1)

    # 파이썬 함수 실행
    result = best_model.predict(test)
    return render_template('result.html', result=result)



# def model_pred(f1, f2, f3, f4, f5):
#     # 받은 데이터를 가지고 작업을 수행하는 파이썬 함수
#     # 여기에서는 입력한 이름과 이메일을 합쳐서 반환하는 예제
#     f1 = int(f1)
#     f2 = int(f2)
#     f3 = int(f3)
#     f4 = int(f4)
#     f5 = int(f5)
#     sum = f1 + f2 + f3 + f4 + f5
#     return  str(sum) + "%"

# gender  attr_s  sinc_s  intel_s  fun_s  amb_s  attr_eval  sinc_eval  intel_eval  fun_eval  amb_eval  shar_eval  like_eval
# tmp = [0] + [10] * 12
# tmp = np.array(tmp).reshape(1, -1)
# print(tmp)
# print(best_model.predict(tmp))

if __name__ == '__main__':
    app.run(port=8000, debug=True)
    
