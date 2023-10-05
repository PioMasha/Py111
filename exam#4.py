def consensus_string(strings):
    consensus = []

    for i in range(len(strings[0])):
        char_count = {}

        for s in strings:
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1

        max_count = 0
        max_char = ''

        for char, count in char_count.items():
            if count > max_count or (count == max_count and char < max_char):
                max_count = count
                max_char = char

        consensus.append(max_char)

    consensus_string = ''.join(consensus)
    return consensus_string


strings = ["ATTA", "ACTA", "AGCA", "ACAA"]
result = consensus_string(strings)
print(result)  # Вывод: "ACTA"

