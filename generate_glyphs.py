import os

import fontforge

# --- 配置区 ---
SOURCE_FONT_PATH = "Alibaba-PuHuiTi-Regular.ttf"  # 你的源字体文件路径
OUTPUT_DIR = "glyphs_source/"  # 渲染出的原始图片存放目录
FONT_RENDER_SIZE = 512  # 渲染时使用的字号（越大越清晰）
CHAR_FILE = "characters_full.txt"  # 包含字符列表的文件

# --- 脚本执行 ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("正在打开字体文件...")
font = fontforge.open(SOURCE_FONT_PATH)
font.em = FONT_RENDER_SIZE  # 设置em方框大小
print("字体家族:", font.familyname)
print("字体全名:", font.fullname)
print("字形数量:", len(font))

print(f"正在从 '{CHAR_FILE}' 读取字符集...")
with open(CHAR_FILE, "r", encoding="utf-8") as f:
    characters = f.read()

total_chars = len(characters)
print(f"共发现 {total_chars} 个字符待处理。")

# # 1. 打开导出选项对话框的设置界面（不弹出窗口，只是拿到设置对象）
# opts = fontforge.exportOptions()

# # 2. 设置 PNG 导出参数
# opts.bitmap_type = "png"
# opts.pixelsize = 512  # 导出图片的尺寸
# opts.bitdepth = 8  # 8 位，对应灰度图（1 位是单色位图）
# opts.grayscale = True  # 关键：启用灰度输出
# opts.transparent = True  # 关键：启用透明背景

for i, char in enumerate(characters):
    if char.strip():  # 忽略空行
        unicode_point = ord(char)
        # # 简单过滤掉代理区（Surrogate）等非法区域
        # if 0xD800 <= unicode_point <= 0xDFFF:
        #     print(f"[{i + 1}] 跳过代理区字符: {char} (U+{unicode_point:04X})")
        #     continue
        # 使用5位数字作为文件名，确保排序正确，例如 00001.png
        filename = f"{unicode_point:05d}.png"
        filepath = os.path.join(OUTPUT_DIR, filename)

        try:
            glyph = font[unicode_point]
            glyph.export(filepath)
            print(f"[{i + 1}/{total_chars}] 已导出: U+{unicode_point:04X} ({char})")
        except Exception as e:
            print(
                f"[{i + 1}/{total_chars}] 错误: 无法处理字符 '{char}' (U+{unicode_point:04X}). 原因: {e}"
            )

font.close()
print("\n所有字符渲染完成！")
