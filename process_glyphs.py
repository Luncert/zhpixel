import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image

# --- 配置区 ---
SOURCE_DIR = "glyphs_source/"  # 上一步生成的图片目录
OUTPUT_DIR = "glyphs_pixelated/"  # 像素化后的图片存放目录
TARGET_PIXEL_SIZE = 16  # 最终像素字体的大小
WHITE_THRESHOLD = 250  # 判定为“白色”的阈值 (0-255)，可根据需要调整
MAX_WORKERS = 8  # 线程数，可根据CPU核心数调整

# --- 脚本执行 ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

image_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".png")]
total_images = len(image_files)
print(f"找到 {total_images} 张图片待处理。")


def process_image(filename):
    filepath = os.path.join(SOURCE_DIR, filename)
    output_filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with Image.open(filepath) as img:
            img = img.convert("RGBA")
            pixels = img.load()
            width, height = img.size
            for y in range(height):
                for x in range(width):
                    r, g, b, a = pixels[x, y]
                    if (
                        r > WHITE_THRESHOLD
                        and g > WHITE_THRESHOLD
                        and b > WHITE_THRESHOLD
                    ):
                        pixels[x, y] = (0, 0, 0, 0)
            img_resized = img.resize(
                (TARGET_PIXEL_SIZE, TARGET_PIXEL_SIZE), Image.Resampling.LANCZOS
            )
            pixels = img_resized.load()
            for y in range(TARGET_PIXEL_SIZE):
                for x in range(TARGET_PIXEL_SIZE):
                    r, g, b, a = pixels[x, y]
                    if a > 128:
                        pixels[x, y] = (0, 0, 0, 255)
                    else:
                        pixels[x, y] = (0, 0, 0, 0)
            img_resized.save(output_filepath, "PNG")
        return (filename, None)
    except Exception as e:
        return (filename, e)


with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {
        executor.submit(process_image, filename): filename for filename in image_files
    }
    for i, future in enumerate(as_completed(futures)):
        filename = futures[future]
        error = future.result()[1]
        if error is None:
            print(f"[{i + 1}/{total_images}] 已处理: {filename}")
        else:
            print(f"[{i + 1}/{total_images}] 错误: 处理 {filename} 失败. 原因: {error}")

print("\n所有图片像素化处理完成！")
