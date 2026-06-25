# File Organizer

这是一个文件整理自动化工具。

## 解决的问题

当下载文件夹里的 PDF、图片、表格混在一起时，手动整理比较繁琐。

这个工具可以自动按文件类型分类。

## 使用方法

```bash
python file_organizer.py
```
## 输入

需要整理的文件夹test-files 文件夹中的待整理文件

## 输出

- pdfs、images、spreadsheets、markdown、unknown 分类文件夹
- report.txt 统计报告

## 文件分类规则

- PDF 文件（.pdf） → pdfs
- 图片文件（.jpg、.png） → images
- 表格文件（.csv、.xlsx） → spreadsheets
- Markdown 文件（.md） → markdown
- 其他文件 → unknown
  
## 项目结构

file-organizer/

├── file_organizer.py

├── report.txt

├── README.md

├── review.md

├── screenshots/

└── test-files/

## 运行结果示例

```text

pdfs: 2

images: 2

spreadsheets: 2

markdown: 1

unknown: 1

## 项目总结

This project organizes files automatically based on file type and generates a structured report. 
