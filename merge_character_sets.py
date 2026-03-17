# merge_character_sets.py


def load_characters_from_file(filename):
    """从文件加载字符，每行一个字符，返回集合（去重）"""
    chars = set()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                char = line.strip()
                if char:
                    chars.add(char)
    except FileNotFoundError:
        print(f"警告：文件 {filename} 不存在，跳过。")
    return chars


def save_characters_to_file(chars, filename):
    """将字符集合保存到文件，每行一个字符"""
    with open(filename, "w", encoding="utf-8") as f:
        for char in sorted(chars, key=lambda c: ord(c)):
            f.write(char + "\n")
    print(f"已保存 {len(chars)} 个字符到 {filename}")


def main():
    # 定义输入文件和输出文件
    gb2312_file = "characters_gb2312.txt"  # 你之前生成的 GB2312 汉字
    english_file = "characters_english.txt"  # 你刚生成的英文字符
    output_file = "characters_full.txt"  # 合并后的完整字符集

    # 加载两个字符集
    print("正在加载 GB2312 汉字...")
    chinese_chars = load_characters_from_file(gb2312_file)
    print(f"已加载 {len(chinese_chars)} 个汉字。")

    print("正在加载英文字符...")
    english_chars = load_characters_from_file(english_file)
    print(f"已加载 {len(english_chars)} 个英文字符。")

    # 合并并去重
    all_chars = chinese_chars | english_chars  # 集合并集
    print(f"合并后共 {len(all_chars)} 个唯一字符。")

    # 保存合并结果
    save_characters_to_file(all_chars, output_file)

    # 显示前 20 个和后 20 个字符（方便检查）
    sorted_chars = sorted(all_chars, key=lambda c: ord(c))
    print("\n前 20 个字符：")
    print("".join(sorted_chars[:20]))
    print("\n后 20 个字符：")
    print("".join(sorted_chars[-20:]))


if __name__ == "__main__":
    main()
