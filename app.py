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
    f1 = int(f1)
    f2 = int(f2)
    f3 = int(f3)
    f4 = int(f4)
    f5 = int(f5)
    sum = f1 + f2 + f3 + f4 + f5
    return  str(sum) + "%"

# gender  attr_s  sinc_s  intel_s  fun_s  amb_s  attr_eval  sinc_eval  intel_eval  fun_eval  amb_eval  shar_eval  like_eval
# tmp = [0] + [10] * 12
# tmp = np.array(tmp).reshape(1, -1)
# print(tmp)
# print(best_model.predict(tmp))

if __name__ == '__main__':
    app.run(port=8000, debug=True)
    
