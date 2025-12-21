def count_repetitions(text: str, idx: int) -> int:

    count = 1
    while idx + 1 < len(text) and text[idx] == text[idx + 1]:
        count += 1
        idx += 1

    return count


def look_and_say(text: str) -> str:
    new_text = ""

    idx = 0
    while idx < len(text):
        repetitions = count_repetitions(text, idx)
        new_text += str(repetitions) + text[idx]
        idx = idx + repetitions

    return new_text


def main():
    text = "1"
    for _ in range(10):
        print(text)
        text = look_and_say(text)


if __name__ == '__main__':
    main()
