import os

input_file = "characters_full.txt"
output_file = "character_index.txt"


def main():
    index = []
    with open(input_file, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 0):
            char = line.strip()
            if not char:
                continue
            codepoint = ord(char)
            # hex_code = f"U+{codepoint:04X}"
            index.append(f"{codepoint},{lineno}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(index))

    print(f"Index file written to {output_file}")


if __name__ == "__main__":
    main()
