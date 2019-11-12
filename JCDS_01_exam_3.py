import json
def cekAwalan(string):
    
    if string[0] == '4' or string[0] == '5' or string[0] == '6':
        # print("masih valid")
        valid = True
    else: valid = False
    return valid

def cekDigitCCAngka(string):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    valid = False
    cekdigit = string.replace('.', '')
    cekdigit = cekdigit.replace('-','')
    cekdigit = cekdigit.replace(' ','')
    if len(cekdigit) == 16:
        valid = True
        for letter in string:
            if letter not in num:
                valid = False
                break
    else:
        valid = False
    
    return valid

def cekDigitHubung(string):
    hubung = False
    valid = False
    for letter in string:
        if letter == '-':
            hubung = True
            break
        else:
            hubung = False
    if hubung :
        listString = string.split('-')
        # print(listString)
        for elemen in listString:
            if len(elemen)==4:
                valid = True
            else: 
                # print("y",len(elemen))
                valid = False
                break
            
    # print(hubung, valid)
    return hubung, valid
def cekPerulangan(string):
    string=string.replace('-','')
    string=string.replace('.','')
    # print("ini", string)
    valid = True
    twin = 0
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            twin +=1
            if twin>=3:
                valid = False
                # print("3xxxxxxxxxxxx!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
        else:
            twin = 0
    # print(valid)
    return valid

def cekCC(string):
    validFULL = False
    #rule1 - awalan 4 5 6
    awalanValid = cekAwalan(string)
    #rule2 digit 16 dan terdiri dari angka 0-9
    digitValid = cekDigitCCAngka(string)
    #jika ada hubung (true), cek hubungvalid . Jika true artinya valid
    hubung, hubungvalid = cekDigitHubung(string)
    #valid-> cekPerulanganCC ==true
    cekPerulanganCC = cekPerulangan(string)
    
    if awalanValid and digitValid and cekPerulanganCC:
        #jika ada penghubung harus cek digit 4nya
        if hubung:
            if hubungvalid:
                validFULL = True
            else: validFULL = False
        else:
            validFULL = True

    return validFULL
    
def main():
    listValid = []
    listInValid = []
    with open('ccNasabah.json') as json_file:
        data = json.load(json_file)
        for p in data:
            valid = False
            noCR = p['noCreditCard']
            # print(noCR)
            # print(cekCC(noCR))
            statusValid = cekCC(noCR)
            if statusValid:
                print(p['nama'])
                print(p['noCreditCard'])
                listValid.append(p)
            else:
                listInValid.append(p)

    with open('ccValid.json', 'w') as outfile:
        json.dump(listValid, outfile)
    with open('ccInvalid.json', 'w') as outfile2:
        json.dump(listInValid, outfile2)

if __name__ == '__main__':
    main()
    