from collections import deque


def get_adjacent_words(word, word_set):
    adjacent_words = []
    for i in range(len(word)):
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char != word[i]:
                new_word = word[:i] + char + word[i + 1 :]
                if new_word in word_set:
                    adjacent_words.append(new_word)
    return adjacent_words


def find_word_ladder(start_word, end_word, word_set):
    queue = deque([(start_word, [start_word])])
    visited = set([start_word])

    while queue:
        current_word, ladder = queue.popleft()

        if current_word == end_word:
            return ladder

        for adjacent_word in get_adjacent_words(current_word, word_set):
            if adjacent_word not in visited:
                visited.add(adjacent_word)
                queue.append((adjacent_word, ladder + [adjacent_word]))

    return []


def write_ladder_to_file(ladder, output_file):
    if not ladder:
        output_file.write("No ladder found.")
    else:
        for word in ladder:
            output_file.write(word + "\n")


def main():
    start_word = input("Enter the start word: ")
    end_word = input("Enter the end word: ")

    word_list_file = open("list_of_words.txt", "r")
    word_list = word_list_file.read().splitlines()
    word_list_file.close()

    word_set = set(word_list)

    output_file = open("output.txt", "w")
    ladder = find_word_ladder(start_word, end_word, word_set)
    write_ladder_to_file(ladder, output_file)
    output_file.close()


if __name__ == "__main__":
    main()
