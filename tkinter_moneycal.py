#환율 계산기

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # 이미지 처리를 위한 Pillow 라이브러리

def calculate():
    try:
        krw_amount = float(entry_krw.get())
        exchange_rate = 0.00070  # 고정 환율
        usd_amount = krw_amount * exchange_rate
        entry_usd.delete(0, tk.END)
        entry_usd.insert(0, f"{usd_amount:.5f}")  # 소수점 5자리까지 표시
    except ValueError:
        entry_usd.delete(0, tk.END)
        entry_usd.insert(0, "유효한 숫자를 입력하세요.")

window = tk.Tk()
window.title("환율 계산기")

# 왼쪽 상단 고정 환율 표시
fixed_rate_label = ttk.Label(window, text="1 대한민국 원 = 0.00069 미국 달러", font=("Arial", 10))
fixed_rate_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# 원화 입력 레이블 및 필드
label_krw = ttk.Label(window, text="대한민국 원:")
label_krw.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_krw = ttk.Entry(window, width=15)
entry_krw.grid(row=1, column=1, padx=10, pady=5)

# 미국 달러 결과 레이블 및 필드
label_usd = ttk.Label(window, text="미국 달러:")
label_usd.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_usd = ttk.Entry(window, width=15, state="readonly")  # 읽기 전용으로 설정
entry_usd.grid(row=2, column=1, padx=10, pady=5)

# 계산 버튼
calculate_button = ttk.Button(window, text="계산", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 오른쪽 이미지 표시 
try:
    image = Image.open("today_dollar.png")  # 이미지 파일 이름
    resized_image = image.resize((200, 150))  # 이미지 크기 조절 (선택 사항)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = ttk.Label(window, image=photo)
    image_label.grid(row=0, column=2, rowspan=4, padx=10, pady=10)
except FileNotFoundError:
    error_label = ttk.Label(window, text="환율 그래프 이미지를 찾을 수 없습니다.")
    error_label.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()