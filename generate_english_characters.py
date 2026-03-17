# generate_english_characters.py


def generate_english_characters():
    """
    生成包含所有常用英文字符的文本文件。
    每行一个字符。
    """
    output_filename = "characters_english.txt"

    # 定义字符集合
    uppercase_letters = [chr(code) for code in range(ord("A"), ord("Z") + 1)]
    lowercase_letters = [chr(code) for code in range(ord("a"), ord("z") + 1)]
    digits = [chr(code) for code in range(ord("0"), ord("9") + 1)]

    # 常用标点符号（可根据需要扩展）
    punctuation = [
        " ",
        ".",
        ",",
        "!",
        "?",
        "'",
        '"',
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "<",
        ">",
        "/",
        "\\",
        "|",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "+",
        "=",
        "-",
        "_",
        "`",
        "~",
        ":",
        ";",
    ]

    # 合并所有字符
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation

    # 写入文件
    with open(output_filename, "w", encoding="utf-8") as f:
        for char in all_characters:
            f.write(char + "\n")

    print(f"生成完毕！共 {len(all_characters)} 个字符。")
    print(f"文件已保存为: {output_filename}")


if __name__ == "__main__":
    generate_english_characters()
