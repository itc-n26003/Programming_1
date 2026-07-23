# 表のデータ生成
data = [
        ['01' , '0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo'],
        ['01' , '0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa'],
        ['01' , '0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama'],
        ['02' , '0001' , 'Male' , 'Smith' , 'Mike' , 22 , 'NewJersey'],
        ['02' , '0002' , 'Male' , 'Turner' , 'Tom' , 27 , 'Kansas'],
        ['02' , '0003' , 'Male' , 'Jackson' , 'David' , 22 , 'Florida']
        ]
#print(data)

# 辞書変数生成
member_information = {}

# 表データをレコード毎に格納する
for record in data:
    key = (record[0],record[1])
    info = record[2:]
    member_information[key] = info

# 結果を表示する
print('number', 'information', sep='\t')
for key, info in member_information.items():
    print(key, info)
