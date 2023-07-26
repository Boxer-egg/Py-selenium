from reportlab.pdfgen import canvas


class Report:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def add_line(self, text):
        self.data.append(text)

# 这是Report类的add_line方法。这个方法接受一个参数text，然后将这个文本添加到self.data列表的末尾。

    def generate_pdf(self):
        c = canvas.Canvas(self.filename)
        for i, line in enumerate(self.data):
            c.drawString(100, 800 - i * 15, line)
        c.save()


'''
init
这是Report类的初始化方法。当你创建一个新的Report对象时，这个方法会被自动调用。
filename参数是你想要生成的PDF文件的名字，
self.filename = filename这行代码将这个参数保存到对象中。
self.data = []这行代码创建了一个空的列表，用于存储你想要添加到报告中的文本行。
'''


'''
这是Report类的generate_pdf方法。
这个方法首先创建了一个新的canvas对象c，然后遍历self.data列表中的每一行文本，
使用drawString方法将文本添加到PDF文档中。文本的位置由(100, 800 - i * 15)这个坐标决定，
这样每一行文本都会在上一行的基础上向下移动15个单位。最后，c.save()这行代码保存了PDF文档。
'''
