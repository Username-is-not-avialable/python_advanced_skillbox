from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def hello_world(numbers):
    str_num = numbers.split('/')
    num = []
    for str_n in str_num:
        parts = str_n.split('.')
        print("123456789000000", len(parts))
          
        if len(parts) == 0 or len(parts) > 2:
            continue

        if len(parts) == 1:
            if not parts[0].isdigit() and not (parts[0][0] == '-' and parts[0][1:].isdigit()):
                continue
            elif len(parts[0]) == 0:
                continue
            else:
                num.append(int(str_n))
        else:
            if not parts[1].isdigit() or len(parts[0]) == 0 or len(parts[1]) == 0:
                continue

            if not parts[0].isdigit() and not (parts[0][0] == '-' and parts[0][1:].isdigit()):
                continue

            num.append(float(str_n))
    if len(num) == 0:
        return "No numbers in request :("
    return str(max(num))


if __name__ == '__main__':
    app.run(debug=True)