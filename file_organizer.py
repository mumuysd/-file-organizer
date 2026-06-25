# 文件整理自动化工具 v0.3
# 功能：按文件类型整理测试文件夹里的文件
# 支持：PDF、图片、表格、Markdown、其他文件

from pathlib import Path
#设置测试文件夹路径
current_folder = Path(__file__).parent
folder = current_folder / "test-files"
pdf_folder = folder / 'pdfs'
image_folder = folder / 'images'
spreadsheet_folder = folder / 'spreadsheets'
markdown_folder = folder / 'markdown'
unknown_folder = folder / 'unknown'
#初始化文件计数器
pdf_count = 0
image_count = 0
spreadsheet_count = 0
markdown_count = 0
unknown_count = 0
#创建分类文件夹
pdf_folder.mkdir(exist_ok=True)
image_folder.mkdir(exist_ok=True)
spreadsheet_folder.mkdir(exist_ok=True)
markdown_folder.mkdir(exist_ok=True)
unknown_folder.mkdir(exist_ok=True)
#遍历文件夹中的所有文件
for item in folder.iterdir():
    #跳过文件夹
    if item.is_dir():
        continue
    #根据文件类型移动文件到对应的文件夹
    if item.name.endswith('.pdf'):
        file_type = 'pdf file'  #识别文件类型
        target_folder = pdf_folder #设置目标文件夹
        pdf_count += 1  #统计文件数量
    elif item.name.endswith(('.jpg', '.png')):
        file_type = 'image file'
        target_folder = image_folder
        image_count += 1
    elif item.name.endswith(('.csv', '.xlsx')):
        file_type = 'spreadsheet file'
        target_folder = spreadsheet_folder
        spreadsheet_count += 1
    elif item.name.endswith('.md'):
        file_type = 'markdown file'
        target_folder = markdown_folder
        markdown_count += 1
    else:
        file_type = 'unknown file'
        target_folder = unknown_folder
        unknown_count += 1
    print(item.name, 'is a', file_type, '->', target_folder)
    #移动文件到目标文件夹
    item.rename(target_folder / item.name) 
total_count = image_count + pdf_count + spreadsheet_count + markdown_count + unknown_count
#生成整理报告文件

report_path = current_folder / "report.txt"
#将整理结果写入报告文件
with open(report_path, "w", encoding="utf-8") as f:
    f.write("File Organizer Report\n")
    f.write("\n")
    f.write(f"Image files: {image_count}\n")
    f.write(f"PDF files: {pdf_count}\n")
    f.write(f"Spreadsheet files: {spreadsheet_count}\n")
    f.write(f"Markdown files: {markdown_count}\n")
    f.write(f"Unknown files: {unknown_count}\n")
    f.write(f"Total files: {total_count}\n")
# ===== Top 1 文件类型统计 =====
max_count = max(pdf_count, image_count, spreadsheet_count, markdown_count, unknown_count)

if max_count == pdf_count:
    top_type = "PDF"
elif max_count == image_count:
    top_type = "IMAGE"
elif max_count == spreadsheet_count:
    top_type = "SPREADSHEET"
elif max_count == markdown_count:
    top_type = "MARKDOWN"
else:
    top_type = "UNKNOWN"

print("Most common file type:", top_type)
#打印整理结果
print("整理完成！")
print("Image files:", image_count)
print("PDF files:", pdf_count)
print("Spreadsheet files:", spreadsheet_count)
print("Markdown files:", markdown_count)
print("Unknown files:", unknown_count)
print("Total files:", total_count)
git init