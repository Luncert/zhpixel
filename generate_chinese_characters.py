# generate_chinese_characters.py


def generate_gb2312_characters():
    """
    生成包含GB2312标准所有简体汉字的文本文件。
    每个汉字独占一行。
    """
    output_filename = "characters_gb2312.txt"
    character_count = 0

    print("开始生成GB2312常用汉字集...")

    with open(output_filename, "w", encoding="utf-8") as f:
        # 外层循环：遍历GB2312的第一字节 (区)
        for area in range(0xB0, 0xF8):  # 0xF8 是开区间，所以会停在 0xF7
            # 内层循环：遍历GB2312的第二字节 (位)
            for position in range(0xA1, 0xFF):  # 0xFF 是开区间，所以会停在 0xFE
                # 将区码和位码组合成完整的GB2312编码
                # 在Unicode中，GB2312的编码是连续的
                gb2312_code = (area << 8) + position

                # 将编码转换为字符
                try:
                    char = bytes([area, position]).decode("gb2312")
                    f.write(char + "\n")
                    character_count += 1
                except UnicodeDecodeError:
                    # 有些组合在GB2312中可能是空的或保留的，忽略错误
                    pass

    print(f"生成完毕！共 {character_count} 个汉字。")
    print(f"文件已保存为: {output_filename}")


if __name__ == "__main__":
    generate_gb2312_characters()
