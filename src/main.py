from textnode import TextNode, TextType


def main():
    node = TextNode("Hello there :)", TextType.ITALIC, "boot.dev")
    print(node)


if __name__ == "__main__":
    main()
