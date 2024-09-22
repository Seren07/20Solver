from flask import Flask, request, render_template

app = Flask(__name__)

# Halaman utama 
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk memproses data dari form
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Mendapatkan input angka dari form
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        number3 = int(request.form['number3'])
        number4 = int(request.form['number4'])

        # Memasukkan angka 
        numbers = [number1, number2, number3, number4]
        solutions = solve_for_20_unique(numbers)

         # Hitung jumlah solusi
        num_solutions = len(solutions)

        # Kirimkan jumlah solusi dan solusi ke template
        return render_template('result.html', solutions=solutions, num_solutions=num_solutions)


    except ValueError:
        return "Pastikan semua input adalah angka!"

# Fungsi yang menghitung hasil
def solve_for_20_unique(numbers):
    import itertools
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else None}

    expressions = [
        "{a} {op1} {b} {op2} {c} {op3} {d}",
        "({a} {op1} {b}) {op2} ({c} {op3} {d})",
        "(({a} {op1} {b}) {op2} {c}) {op3} {d}",
        "({a} {op1} ({b} {op2} {c})) {op3} {d}",
        "{a} {op1} (({b} {op2} {c}) {op3} {d})",
        "{a} {op1} ({b} {op2} ({c} {op3} {d}))"
    ]

    unique_solutions = set()

    for perm_numbers in itertools.permutations(numbers):
        for perm_ops in itertools.product(ops.keys(), repeat=3):
            for expr_template in expressions:
                try:
                    expr = expr_template.format(
                        a=perm_numbers[0], b=perm_numbers[1], c=perm_numbers[2], d=perm_numbers[3],
                        op1=perm_ops[0], op2=perm_ops[1], op3=perm_ops[2]
                    )
                    result = eval(expr)
                    if result == 20:
                        formatted_expr = expr.replace(" ", "")
                        unique_solutions.add(f"{expr} = 20")
                except ZeroDivisionError:
                    pass
    return unique_solutions

if __name__ == '__main__':
    app.run(debug=True)
