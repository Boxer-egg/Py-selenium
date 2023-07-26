import tkinter as tk

root = tk.Tk()
root.title('My Application')

# 创建标签
label = tk.Label(root, text='Enter some text:')
label.pack()

# 创建输入框
entry = tk.Entry(root)
entry.pack()

# 创建文本框
text = tk.Text(root)
text.pack()

root.mainloop()
