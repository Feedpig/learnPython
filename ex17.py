from sys import argv
from os.path import exists

script, from_file, to_file  = argv

print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
# in_file = open(from_file,'r')
# indata = in_file.read()
indata = open(from_file).read()  # 将上面2行变成一行 ，并且最后不需要close（）
print(f"The input file is {len(indata)} bytes long")

print(f"Dose the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input('?')
#下面这行代码也是将 2行代码缩成一行 最后也不需要 close
#out_file = open(to_file,'w').write(indata)
out_file = open(to_file,'w')
out_file.write(indata)
print("Alright,all done.")

out_file.close()
#in_file.close()




# script, from_file, to_file   = argv
# print(f"Copying from {from_file} to {to_file}")
# with open(from_file,'r') as Txt:
#     Indata = Txt.read()
# print(f"Does the file exist? {to_file}")

# input("Are you sure to start?")

# with open(to_file,'w') as Txt_in:
#     Txt_in.write(Indata)

# print("Okey! finished.")