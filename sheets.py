import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
data = sheet.get_all_records()
names = sheet.col_values(3)
rooms = sheet.col_values(9)

room_num = input("Room number: ")
while room_num.lower() != "stop":
    r_ind = []
    for i in range(len(rooms)):
        room_name = "Soto " + room_num
        if room_name in rooms[i]:
            r_ind.append(i)
    if len(r_ind) == 1:
        sheet.update_cell(r_ind[0] + 1, 14, "TRUE")
    elif len(r_ind) == 2:
        for ind in r_ind:
            res_num = rooms[ind][-1]
            res_name = names[ind]
            print(f"Resident {res_num}: {res_name}")
        r_num = input("Resident number? Enter 0 if checking both: ")
        if r_num == "0":
            sheet.update_cell(r_ind[0] + 1, 14, "TRUE")
            sheet.update_cell(r_ind[1] + 1, 14, "TRUE")
        elif r_num == "1" or r_num == "2":
            num = int(r_num) - 1
            sheet.update_cell(r_ind[num] + 1, 14, "TRUE")
        else:
            print("Something went wrong. Try this one manually.")
    else:
        print("Something went wrong. Try this one manually.")
    room_num = input("Room number: ")