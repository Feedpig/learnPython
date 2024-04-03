from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(f"the {line_count} line : {f.readline()}",end = ' ')

def print_a_line_1(line_count, line_content):
    # 检查行内容是否不仅仅是换行符
    if line_content.strip() != '':
        print(line_count, line_content, end='')


# 使用 UTF-16LE 编码打开文件
promt = '*****'
line_count = 0
#因为打开阅读模式，系统是按行进行迭代的
with open(input_file, 'r', encoding='utf-16le') as file:
     for line in file:
        if line.strip():  # 使用 strip() 方法移除行首尾的空白字符，检查行是否非空
            line_count += 1

print(f"The file has {line_count} lines.")

print(promt)
current_file = open(input_file, encoding='utf-16le')

# 确保文件指针回到文件开头
rewind(current_file)
# 使用 enumerate 遍历文件的每一行
for i, line in enumerate(current_file, start=1):  # start=1 使行号从1开始
    print_a_line_1(i, line)


# 使用 range 遍历文件的每一行
print(promt)
rewind(current_file)
for a in range(line_count):
    print_a_line(a,current_file)


print(promt)    
print("First let's print the whole file:\n")

rewind(current_file)
print_all(current_file)

# print("Now let's rewind, kind of like a tape.")
# rewind(current_file)

# print("Let's print three lines:")
# current_line = 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

current_file.close()

