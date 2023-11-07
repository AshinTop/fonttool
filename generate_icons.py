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
icons = map(lambda icon: property_format %
            (icon["name"], icon["name"].upper(), icon["value"].upper()), icons)

_class = class_format % (''.join(icons))
with open("icons.ts", "w", encoding='utf-8') as f:
    f.write(_class)

