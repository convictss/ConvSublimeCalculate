# Conv 计算器
> Conv calculator

# 一个简单的计算器，支持加减乘除，支持高精度计算（基于 Decimal 计算，而不是 float）
> A simple calculator that supports addition, subtraction, multiplication and division, and supports high-precision calculation (based on Decimal calculation, not float)

# 使用方法：
1. 输入算式后，按 super+shift+c，计算结果将自动追加到算式后面
2. 选中需要计算的算式后，按 super+shift+c，计算结果将自动追加到算式后面
> # usage:
> 1. After entering the formula, press super+shift+c, and the calculation result will be automatically appended to the end of the formula
> 2. After selecting the formula to be calculated, press super+shift+c, and the calculation result will be automatically appended to the end of the formula

# 按键绑定
> Key Bindings
# 复制以下内容到你的按键绑定文件
> Copy these to your user key bindings file.

MacOS:

{ "keys": ["super+shift+c"], "command": "conv_calculate" },

Windows:

{ "keys": ["alt+shift+c"], "command": "conv_calculate" },

Linux:

{ "keys": ["alt+shift+c"], "command": "conv_calculate" },

> Tip
> 