# fontTools 分割字体

## 安装 fontTools
```
pip install fonttools # 字体工具
pip install brotil    # 制作 woff2 格式所需
```

## 文件说明
- material-icons.woff2 源字体文件（）
- unicodes.txt 需要保留的字符的unicode码
- icons.woff2 输出文件

## python命令
```
// 方法1：直接调用下面命令，得到所需的icon文件。生成的icon使用得用 Unicode （&#x开头）
pyftsubset material-icons.woff2 --unicodes-file=unicodes.txt --output-file=icons.woff2 --verbose

pyftsubset MaterialIcons-Regular.ttf --unicodes-file=unicodes.txt --output-file=icons.ttf
```