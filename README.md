# fontTools 分割字体

https://github.com/fonttools/fonttools

https://fonttools.readthedocs.io/en/latest/developer.html

## 安装 fontTools

```
pip install fonttools # 字体工具
pip install Brotli    # 制作 woff2 格式所需
```

## 文件说明

- material-icons.woff2 源字体文件
- unicodes.txt 需要保留的字符的 unicode 码
- icons.woff2 输出文件

## python 命令

```
// 方法1：指定unicodes：直接调用下面命令，得到所需的icon文件。生成的icon使用得用 Unicode （&#x开头），直接用name无法识别
pyftsubset material-icons.woff2 --unicodes-file=unicodes.txt --output-file=icons.woff2 --verbose --harfbuzz-repacker

pyftsubset MaterialIcons-Regular.ttf --unicodes-file=unicodes.txt --output-file=icons.ttf

pyftsubset material-icons.woff2 --glyphs-file=name.txt --output-file=icons.woff2 --verbose


```

生成的图标，可在 index.html 中查看

## 自动生成配置文件

运行 generate_icons.py 文件

```
python generate_icons.py
```

## 如果修改/新增 icon

1. 编辑 unicode.txt 文件

新增 icon 的 unicode 码,#后为注释内容，标注 icon 的 name。icon 的 name 和 code 可查询： https://fonts.google.com/icons?icon.set=Material+Icons

```
# close
e5cd
```

2. 运行 subset_icons_font.sh 文件，自动生成 font 文件（icons.woff2）和配置文件（Icons.ts）
