testReport.py

from reportDoc import Report


Report.add_line('搜索产品成功：' + product_name)
Report.generate_pdf("测试完成")
