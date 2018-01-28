def calc_checkdigit(num):
  _s = 0
  if (len(str(num))) != 10:
    print("10桁の数字が必要")
  else:
    for n, p in enumerate(num,start=1):
      if (n <= 4):
        _s += (5-n) * int(p)
      elif (n >= 5):
        _s += (7-n) * int(p)

  _mod = _s % 11
  if (_mod <= 1):
    return 0
  else:
    return 11 - _mod

def verify_stnumber(num):
  if(len(num)) != 11:
    print("11桁の数字が必要です")
  else:
    checkdigit = str(calc_checkdigit(num[:10]))
    if (num[10] == checkdigit):
      print("正しいナンバーです")
    else:
      print("計算上のチェックデジットは{0} 入力された末尾は{1}です".format(checkdigit, num[10]))

def check_person_info(num):
  if (len(str(num))) <= 10:
    print("10桁の数字が必要")
  else:
    _college = int(num[0:2])
    _major_field = str(num[2:4])
    _entering_year = str(num[4:6])
    _personal_number = str(num[6:10])

    _colleges_list = {11:"法学部",
                    12:"経済学部",
                    13:"経営学部",
                    14:"産業社会学部",
                    15:"国際関係学部",
                    17:"文学部",
                    18:"政策科学部",
                    19:"映像学部",
                    20:"総合心理学部",
                    21:"理工学部",
                    22:"理工学部",
                    25:"食マネジメント学部",
                    26:"情報理工学部",
                    27:"生命科学部",
                    28:"薬学部",
                    29:"スポーツ健康科学部"
                    }
    _major_fields_list = {}

    # 学部
    _college = _colleges_list.get(_college, 'None')
    # 課程・専攻など
    _major_field = _major_fields_list.get(_major_field, 'None')

    print("学部・研究科: {0}".format(_college))
    print("課程・専攻など: {0}".format(_major_field))
    print("入学年度: 20{0}".format(_entering_year))
    print("個人番号: {0}".format(_personal_number))

if __name__ == '__main__':
  stnumber = str(input("学生証番号を入力してください(ハイフンなし): "))
  if ((len(stnumber)) == 11) and (stnumber.isdigit()):
    verify_stnumber(stnumber)
    check_person_info(stnumber)
  else:
    print("正しい学生証番号を入力してください")
