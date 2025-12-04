#national code validator V2
#coded by javadnistesh
print("""
  ___                 _               _   _       _   _                   _    ____          _        _____           _ 
 |_ _|_ __ __ _ _ __ (_) __ _ _ __   | \ | | __ _| |_(_) ___  _ __   __ _| |  / ___|___   __| | ___  |_   _|__   ___ | |
  | || '__/ _` | '_ \| |/ _` | '_ \  |  \| |/ _` | __| |/ _ \| '_ \ / _` | | | |   / _ \ / _` |/ _ \   | |/ _ \ / _ \| |
  | || | | (_| | | | | | (_| | | | | | |\  | (_| | |_| | (_) | | | | (_| | | | |__| (_) | (_| |  __/   | | (_) | (_) | |
 |___|_|  \__,_|_| |_|_|\__,_|_| |_| |_| \_|\__,_|\__|_|\___/|_| |_|\__,_|_|  \____\___/ \__,_|\___|   |_|\___/ \___/|_|
                                                                                                                          
""")

National_Code = input("ENTER YOUR NATIONAL CODE : ")

if len(National_Code) != 10:
    print("Not Valid , The National Code SHOULD BE 10 Number")
else:
    kol = int(National_Code[0])*10 + int(National_Code[1])*9 + int(National_Code[2])*8 + int(National_Code[3])*7 + int(National_Code[4])*6 + int(National_Code[5])*5 + int(National_Code[6])*4 + int(National_Code[7])*3 + int(National_Code[8])*2
    total = kol % 11
    
    
    
    if (total < 2 and int(National_Code[9]) == total) or (total >= 2 and int(National_Code[9]) == (11 - total)):
        print("The National Code Is VALID")
        
        three = National_Code[0:3]
        
        match three:
            case "261":
                print("Astara")
            case "273":
                print("Astaneh-Ashrafie")
            case "630":
                print("Amlash")
            case "264":
                print("Bandar-Anzali")
            case "518":
                print("Khomam")
            case "631":
                print("Rahim-Abad")
            case "259" | "258":
                print("Rasht")
            case "516":
                print("Masal")
            case "570":
                print("Rezvan-Shahr")
            case "265":
                print("Rodbar")
            case "269" | "268":
                print("Rodsar")
            case "653":
                print("Sangar")
            case "517":
                print("Siahkal")
            case "569":
                print("Shaft")
            case "267":
                print("Someh-Sara")
            case "263" | "262":
                print("Talesh")
            case "266":
                print("Foman")
            case "693":
                print("Koch-Esfahan")
            case "272" | "271":
                print("Lahijan")
            case "694":
                print("Lasht-Nesha")
            case "270":
                print("Langarod")
            case _:
                print("City Not Found")
                
    else:
        print("National Code Is NOT VALID !")