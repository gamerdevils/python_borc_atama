from datetime import date
def repeat_string(a_string, target_length):
    number_of_repeats = target_length // len(a_string) + 1
    a_string_repeated = a_string * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:target_length]
    return a_string_repeated_to_target

#f = open("c:/users/hakanbilgin/desktop/0815ATS-" + date.today().strftime("%d%m%Y-%H%M%S")+".txt","w")
f = open("c:/users/hakanbilgin/desktop/0815ATS-11+"+".txt","w")
f.truncate()
f.write("0815D")
f.write("00030000")
f.write("                 ")
f.write("DORMYURTUC-")
f.write(str(date.today().strftime("%d%m")))
f.write(str(date.today().strftime("%d.%m.%Y")))
f.write("00000000005100000")
f.write("  ")
name = "çağrı".upper().replace('Ç','C').replace('Ö','O').replace('Ğ','G').replace('Ü','U').replace('İ','I').replace('Ş','S')
f.write(name)
f.write(repeat_string(" ",15- len(name)))
surname = "sarıoğlük".upper().replace('Ç','C').replace('Ö','O').replace('Ğ','G').replace('Ü','U').replace('İ','I').replace('Ş','S')
f.write(surname)
f.write(repeat_string(" ",25- len(surname)))
f.write("A\n")

#son satır
f.write("0815F")
f.write(repeat_string(" ",26))
satirsayi = 2445
f.write(repeat_string("0",15- len(str(satirsayi))))
f.write(str(satirsayi))
toplamtutar = 2200500000
f.write(repeat_string("0",17- len(str(toplamtutar))))
f.write(str(toplamtutar))

f.close()

#open and read the file after the appending:
f = open("c:/users/hakanbilgin/desktop/0815ATS-11+"+".txt", "r")
print(f.read())
