

以下是工程目录结构：
```
summerProject/
    index.py
    search.py
    download.py
    gui.py
    index.csv
    results.csv
    README.md
    requirements.txt
    docs/
        index.md
        search.md
        download.md
        gui.md
    examples/
        example_1.pdf
        example_2.docx
        example_3.pdf
        example_4.docx
        ...
```

其中：
- `index.py`：索引脚本；
- `search.py`：查询脚本；
- `download.py`：下载脚本；
- `gui.py`：GUI脚本；
- `index.csv`：索引文件；
- `results.csv`：查询结果文件；
- `README.md`：项目说明文件；
- `requirements.txt`：Python依赖库列表；
- `docs/`：文档目录，包含索引脚本、查询脚本、下载脚本和GUI脚本的说明文档；
- `examples/`：示例文件夹，包含一些PDF和Word文档，用于测试索引、查询和下载功能。


要运行这个工程，您需要按照以下步骤进行操作：
1. 安装Python和必要的依赖库
确保您已经安装了Python 3，并安装了必要的依赖库。您可以使用以下命令来安装依赖库：
```
pip install -r requirements.txt
```

2. 索引文件夹中的文档
使用以下命令来索引文件夹中的文档：
```
python index.py --input_dir /path/to/input/dir --output_file index.csv
```
其中：
- `--input_dir`：要索引的文件夹路径；
- `--output_file`：索引文件保存路径。
这个命令将会遍历指定的文件夹，并将其中的PDF和Word文档提取文本内容，并将文档的文件名、路径和文本内容保存到索引文件中。

3. 进行查询
使用以下命令来进行查询：
```
python search.py --input_file index.csv --query "your query" --output_file results.csv
```
其中：
- `--input_file`：索引文件路径；
- `--query`：查询字符串；
- `--output_file`：查询结果保存路径。
这个命令将会从索引文件中查找包含查询字符串的文本内容，并将文档的文件名、路径和文本内容保存到查询结果文件中。

4. 下载查询结果
使用以下命令来下载查询结果：
```
python download.py --input_file results.csv
```
这个命令将会遍历查询结果文件中的所有条目，并将其中的文本内容保存到以文档文件名为名的文本文件中。

5. 运行GUI界面
使用以下命令来运行GUI界面：
```
python gui.py
```
这个命令将会启动GUI界面，您可以在界面中选择要查询的文件夹、输入查询字符串，并查看查询结果。如果查询结果不为空，您可以通过点击下载按钮来下载查询结果。
