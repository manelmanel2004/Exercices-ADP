
word = input("Word: ")

total_width = 30
word_length = len(word)
padding = (total_width - word_length) // 2

top_bottom_frame = "*" * total_width
middle_frame = "*" + " " * padding + word + " " * (total_width - padding - word_length - 2) + "*"

print(top_bottom_frame)
print(middle_frame)
print(top_bottom_frame)
