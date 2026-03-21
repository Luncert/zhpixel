# 使用 Python 优化 PNG
import base64
import os

from PIL import Image


def optimize_png(input_path, output_path):
    img = Image.open(input_path)

    # 确保使用最优压缩参数
    img.save(
        output_path,
        "PNG",
        optimize=True,  # 启用优化
        compress_level=9,  # 最高压缩级别 (1-9)
        bits=8,
    )  # 8位色深

    original_size = os.path.getsize(input_path)
    optimized_size = os.path.getsize(output_path)
    print(f"优化前: {original_size} bytes")
    print(f"优化后: {optimized_size} bytes")
    print(f"压缩率: {(1 - optimized_size / original_size) * 100:.1f}%")


def binary_to_base64(data):
    """
    将二进制数据转换为 Base64 编码字符串

    参数:
        data: 二进制数据 (bytes类型)
    返回:
        Base64 编码的字符串
    """
    if not isinstance(data, bytes):
        raise TypeError("输入必须是 bytes 类型")

    return base64.b64encode(data).decode("utf-8")


def file_to_base64(file_path):
    """
    将文件内容转换为 Base64 编码

    参数:
        file_path: 文件路径
    返回:
        Base64 编码的字符串
    """
    with open(file_path, "rb") as f:
        binary_data = f.read()

    return binary_to_base64(binary_data)


def convert_to_1bit(input_path, output_path):
    img = Image.open(input_path).convert("1")  # 转换为 1-bit
    img.save(output_path, "PNG", optimize=True)
    with open("dist/base64.txt", "wb") as f:
        f.write(binary_to_base64(img.tobytes()).encode("utf-8"))

    original_size = os.path.getsize(input_path)
    optimized_size = os.path.getsize(output_path)
    print(f"优化前: {original_size} bytes")
    print(f"优化后: {optimized_size} bytes")
    print(f"压缩率: {(1 - optimized_size / original_size) * 100:.1f}%")


convert_to_1bit("dist/glyphs_pixelated_combined.png", "dist/pixel_font_optimized.png")
