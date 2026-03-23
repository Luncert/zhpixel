import os

from PIL import Image

# 配置
input_dir = "glyphs_pixelated"
output_file = "dist/glyphs_pixelated_combined.png"
images_per_row = 128  # 每行图片数量，可调整


def main():
    # 获取所有图片文件名，按名字排序
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(".png")]
    files.sort()
    total = len(files)
    if total == 0:
        print("No PNG files found.")
        return

    # 打开第一张图片，获取尺寸
    first_img = Image.open(os.path.join(input_dir, files[0]))
    w, h = first_img.size

    # rows = (total + images_per_row - 1) // images_per_row
    combined_w = images_per_row * w
    combined_h = combined_w

    combined_img = Image.new("RGBA", (combined_w, combined_h), (0, 0, 0, 0))

    for idx, fname in enumerate(files):
        img = Image.open(os.path.join(input_dir, fname))
        row = idx // images_per_row
        col = idx % images_per_row
        x = col * w
        y = row * h
        combined_img.paste(img, (x, y))

    combined_img.save(output_file)
    print(f"Combined image saved to {output_file}")


if __name__ == "__main__":
    main()
