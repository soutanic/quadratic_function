import random

# 問題生成
def question_generate(number):
    def plus_or_minus():
        if random.randint(0, 1) == 0:
            return ' - '
        else:
            return ' + '
    question_string = ''

    question_string += f"({str(number)}) "

    question_string += 'y = '

    coefficient = ''

    if random.randint(0, 3) == 0:
        coefficient += '-'
    if random.randint(0, 2) != 0:
        coefficient += str(random.randint(2, 3))

    question_string += coefficient

    question_string += 'x²'

    question_string += plus_or_minus()

    if '3' in coefficient:
        question_string += str(6 * random.randint(1, 4))
    elif '2' in coefficient:
        question_string += str(4 * random.randint(1, 6))
    else:
        question_string += str(2 * random.randint(1, 9))

    question_string += 'x'

    question_string += plus_or_minus()

    question_string += str(random.randint(2, 9))

    question_return = []

    question_return.append(question_string)
    return question_return


# HTML生成
def html_generate():
    html_string = '''
            <p>次の2次関数を平方完成しなさい。</p>'''

    question_number = 20
    add_line = ''
    add_class = ''
    for i in range(question_number):
        if i % 2 == 0:
            if i != 0:
                add_line = '<br><br><br><br><br>\n        '
            add_class = ' class="left"'
        else:
            add_line = ''
            add_class = ' class="right"'
        html_string += f"\n        {add_line}<span{add_class}>{question_generate(i + 1)[0]}</span>"

    return html_string 

# 枚数の指定
result = '''<!DOCTYPE html>
    <html>
        <head>
            <title>2次方程式問題</title>
            <style>
                span {
                    font-size: 20px
                }
                .left {
                    position: absolute;
                    left:15px;
                }
                .right {
                    position: absolute;
                    left: 400px;
                }
                p {
                    font-size: 20px
                }
            </style>
        </head>
        <body>'''

number_of_sheet = int(input('何枚生成しますか？\n'))
connection = ''
for i in range(number_of_sheet):
    if i != 0:
        connection = '\n        <br><br><br>\n'
    result += connection + html_generate()

result += '''
        </body>
     </html>'''
# ファイルの書き込み
with open('2次関数問題.html', 'w', encoding='utf-8') as f:
    f.write(result)
    f.close()
print(result)

print('------------- 2次関数問題.html がダウンロードされました。 -------------')
