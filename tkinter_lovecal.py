#계산기

import tkinter as tk

class FancyCalculatorRevised:
    def __init__(self, master):
        self.master = master
        master.title("문양 & 사칙연산 계산기")
        master.config(bg="white")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.expression = ""

        # 결과 표시창
        self.result_label = tk.Label(master, textvariable=self.result_var, font=("Arial", 24), bg="lightgray", anchor="e", padx=10, pady=10)
        self.result_label.grid(row=0, column=0, columnspan=3, sticky="ew")  # AC 버튼 때문에 columnspan 3으로 변경

        # AC 버튼 (결과창 오른쪽)
        ac_btn = tk.Button(master, text="AC", padx=20, pady=10, font=("Arial", 16), bg="pink", command=self.clear)
        ac_btn.grid(row=0, column=3, sticky="ew")

        # 문양 버튼 (왼쪽 1열)
        symbol_buttons = ['♥', '★', '▲', '■']
        for i, symbol in enumerate(symbol_buttons):
            symbol_btn = tk.Button(master, text=symbol, padx=20, pady=20, font=("Arial", 16), bg="pink",
                                   command=lambda sym=symbol: self.symbol_click(sym))
            symbol_btn.grid(row=i + 1, column=0, sticky="nsew")

        # 숫자 버튼 (2~4열)
        number_buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '='
        ]
        row_val = 1
        col_val = 1
        for button_text in number_buttons:
            btn = tk.Button(master, text=button_text, padx=20, pady=20, font=("Arial", 16), bg="pink",
                            command=lambda text=button_text: self.button_click(text))
            btn.grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 1
                row_val += 1

        # 사칙연산 버튼 (4열)
        operator_buttons = ['/', '*', '-', '+']
        for i, operator in enumerate(operator_buttons):
            op_btn = tk.Button(master, text=operator, padx=20, pady=20, font=("Arial", 16), bg="pink",
                               command=lambda op=operator: self.button_click(op))
            op_btn.grid(row=i + 1, column=3, sticky="nsew")

        # 그리드 설정 (창 크기 조절 시 버튼 크기 유지)
        for i in range(5):  # 문양 버튼 4개 + 결과창/AC
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 문양 1열 + 숫자 3열 + 연산 1열
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.expression)
                self.result_var.set(result)
                self.expression = str(result)
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += text
            self.result_var.set(self.expression)

    def symbol_click(self, symbol):
        current_result = self.result_var.get()
        if current_result == "0" or current_result == "Error":
            self.result_var.set(symbol)
        else:
            self.result_var.set(current_result + symbol)
        self.expression = self.result_var.get()

    def clear(self):
        self.expression = ""
        self.result_var.set("0")

root = tk.Tk()
calculator = FancyCalculatorRevised(root)
root.geometry("400x300")  # 가로 400 픽셀, 세로 300 픽셀로 초기 크기 설정
root.mainloop()