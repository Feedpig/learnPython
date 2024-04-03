import sys
script , encoding ,  error =  sys.argv

def main(language_file, encoding, errors):
    for i, line in enumerate(language_file):
        print_line(line, encoding, errors)

    # line = language_file.readline()

    # if line:
    #     print_line(line, encoding,error)
    #     return main (language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

language = open("ex23.txt",encoding = "utf-8")

main(language, encoding , error)


# def main(file , encoding, errors):
#     for i, line in enumerate(file):

 
#         print_line()
        
# def print_line(line, encoding, errors):
#     line_read =  line.strip()
#     raw_bytes = line_read.encode()
#     raw_string = raw_bytes.decode()
#     print(raw_bytes,raw_string)

        