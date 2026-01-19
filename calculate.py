from functools import cmp_to_key
import math
import random
import re
from locale import (atof, str as locale_str)
import os
import sublime  # 导入 Sublime Text 提供的核心模块，用于访问编辑器功能
import sublime_plugin  # 导入 Sublime Text 插件开发所需的基础类（如 TextCommand）
import json
import sys
from decimal import Decimal

print('Current python version: {}'.format(sys.version))  # 4200 --> python3.3.7
# print('控制台显示消息')
# sublime.status_message('底部状态栏显示消息，可以作为提示用')
# sublime.error_message('弹窗消息，控制台也会显示消息')
# self.view.show_popup('光标附近浮层提示文字')

class ConvCalculateCommand(sublime_plugin.TextCommand):
    # 插件入口方法：当命令被触发时，Sublime 会调用此方法
    # 参数 `edit` 是 Sublime 提供的编辑令牌，用于安全修改文档内容
    def run(self, edit):
        # 获取当前激活的视图（即当前打开的编辑窗口）
        view = self.view
        # 遍历所有当前选中的区域（支持多光标/多选区）
        for region in view.sel():
            if region.empty():
                # 光标未选中任何内容，取当前行从行首到光标的内容
                line_region = view.line(region)
                expr = view.substr(sublime.Region(line_region.begin(), region.begin())).strip()
                if not expr:
                    continue
            else:
                # 从视图中提取选中区域的原始文本，并去除首尾空白字符
                expr = view.substr(region).strip()
                if not expr:
                    continue

            # 使用否定字符类，剔除【数字、加减乘除、括号、小数点、空格】之外的字符
            clean_expr = re.sub(r'[^\d+\-*/().\s]', '', expr).strip()
            print('clean_expr: {}'.format(clean_expr))
            if not clean_expr:
                view.show_popup('Invalid expression')
                continue

            # 尝试安全地计算表达式
            try:
                # 将所有数字替换为 Decimal('...') 形式
                # 例如: "1.001 + 0.9" → "Decimal('1.001') + Decimal('0.9')"
                expr_with_decimal = re.sub(r'\b(\d+\.?\d*)\b',r"Decimal('\1')", clean_expr)
                print('expr_with_decimal: {}'.format(expr_with_decimal))

                # 安全执行：只允许 Decimal 和基本运算
                result = eval(
                    expr_with_decimal,
                    {"__builtins__": {}},  # 将其设为 {}（空字典），禁止执行 __import__('os')、open('/etc/passwd') 等危险操作
                    {"Decimal": Decimal}  # 告诉 eval 可以使用 Decimal 这个名字，它指向我们导入的 decimal.Decimal 类
                )

                # 转换为字符串（Decimal 会自动去除多余零）
                result_str = str(result)

                # 插入结果
                insert_point = region.end()
                view.insert(edit, insert_point, " = {}".format(result_str))

            # 捕获计算过程中可能出现的任何异常（如语法错误、除零等）
            except Exception as e:
                sublime.status_message('异常，看控制台更详细信息: {}'.format(e))
                print('ConvCalculate error: {}'.format(e))

