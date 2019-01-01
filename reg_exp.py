import re

input_file = "text_re.txt"
output_file = "result.txt"

email_file = open(input_file, mode="r", encoding="utf-8")
result_file = open(output_file, mode="w", encoding="utf-8")

email_file_data = email_file.read()

searching_pattern = r"[A-Za-z-.]+@(?![A-Za-z.]+\.com)[A-Za-z-.]+\.[A-Za-z]+"

result_searching_pattern = re.findall(searching_pattern, email_file_data)

for num, result_data in enumerate(result_searching_pattern, 1):
    result_file.write(str(num) + ". " + result_data + "\n")
