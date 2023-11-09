# 根据 unicodes.txt 生成icon常量文件
# -*- coding: UTF-8 -*-
import sys

class_format = """
/** Generated automatically via **generate_icons.py**, do not modify this file. */
%s
"""
property_format = """
    /** %s */
    export const %s = "\\u%s";
"""

class_format_css = """
/** Generated automatically via **generate_icons.py**, do not modify this file. */
@font-face {
  font-family: 'Material Icons';
  font-style: normal;
  font-display: block;
  font-weight: 400;
  src: url(/src/assets/font/icons.woff2) format('woff2');
}

.bootstrap-icons::before {
  font-family: 'Material Icons';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
%s
"""
property_format_css = """
    /** %s */
    .bi-%s::before {
      content: '\\%s';
    }
"""

with open("unicodes.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()

""" sample unicodes.txt
# close
e5cd
"""
icons = []
name = None
value = None
for line in lines:
    line = line.strip()
    if len(line) == 0:
        continue
    if (line.startswith("#")):
        name = line.replace("#", "").strip()
    elif (name != None):
        value = line
        icons.append({"name": name, "value": value})
        print("parser: %s=%s" % (name, value))
    else:
        print("unknown line: %s" % line)

icons = sorted(icons, key=lambda icon: icon["name"])
icons_data = map(lambda icon: property_format %
            (icon["name"], icon["name"].upper(), icon["value"].upper()), icons)
icons_css= map(lambda icon: property_format_css %
            (icon["name"], icon["name"], icon["value"]), icons)
_class = class_format % (''.join(icons_data))
_class_css = class_format_css % (''.join(icons_css))
with open("icons.ts", "w", encoding='utf-8') as f:
    f.write(_class)
with open("icons.scss", "w", encoding='utf-8') as f:
    f.write(_class_css)

