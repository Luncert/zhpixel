import os

import fontforge

# --- 配置区 ---
OUTPUT_FONT_PATH = "dist/PixelatedFont.ttf"  # 最终生成的像素字体文件名
PIXEL_GLYPH_DIR = "glyphs_pixelated/"  # 像素化后的图片目录
FONT_EM_SIZE = 16  # 必须与 TARGET_PIXEL_SIZE 一致!
FONT_ASCENT = 12  # 基线到顶部的高度，需根据视觉效果调整
FONT_DESCENT = 4  # 基线到底部的高度，需根据视觉效果调整

# --- 脚本执行 ---
print("正在创建新字体...")
new_font = fontforge.font()
new_font.familyname = "Pixelated Font"
new_font.fontname = "PixelatedFont-Regular"
new_font.fullname = "Pixelated Font Regular"
new_font.em = FONT_EM_SIZE
new_font.ascent = FONT_ASCENT
new_font.descent = FONT_DESCENT

# 获取所有像素化后的图片文件
image_files = [f for f in os.listdir(PIXEL_GLYPH_DIR) if f.endswith(".png")]
total_glyphs = len(image_files)
print(f"共发现 {total_glyphs} 个字形待导入。")

for i, filename in enumerate(image_files):
    filepath = os.path.join(PIXEL_GLYPH_DIR, filename)

    try:
        # 从文件名解析出 Unicode 码点
        unicode_point = int(os.path.splitext(filename)[0])

        # 创建一个新的字形
        new_glyph = new_font.createChar(unicode_point)

        # 导入我们处理好的像素图片作为字形的轮廓
        new_glyph.importOutlines(filepath)
        # 导入 PNG 位图
        # new_glyph.importBitmap(filepath)
        # 自动描边（矢量化）
        # new_glyph.autoTrace()

        # 设置字宽，对于等宽像素字体，通常等于 em size
        new_glyph.width = FONT_EM_SIZE

        print(f"[{i + 1}/{total_glyphs}] 已导入: U+{unicode_point:04X}")

    except Exception as e:
        print(f"[{i + 1}/{total_glyphs}] 错误: 导入 {filename} 失败. 原因: {e}")

print(f"\n正在生成字体文件: {OUTPUT_FONT_PATH}...")
new_font.generate(OUTPUT_FONT_PATH)
new_font.close()  # 关闭字体，保存为 .sfd 源文件
print("字体生成成功！")
