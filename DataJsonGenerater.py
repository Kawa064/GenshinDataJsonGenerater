import json
#必要なファイルのロード
#言語データ
with open("lang.json", "r", encoding="utf-8") as f1:
    lang_data = json.load(f1)
#キャラクターの情報
with open("charactors.json", "r", encoding="utf-8") as f2:
    char_data = json.load(f2)
#自分のデータ
with open("mydata.json", "r", encoding="utf-8") as f3:
    my_data = json.load(f3)
TEST_ID = 3

#data.json用元素変換辞書
genso = {
    "Ice":"氷",
    "Fire":"炎",
    "Wind":"風",
    "Rock":"岩",
    "Electric":"雷",
    "Grass":"草",
    "Water":"水"
    }
#data.json用元素バフ変換辞書
genso_buff_id = {
    "40":"炎元素ダメージ",
    "41":"雷元素ダメージ",
    "42":"水元素ダメージ",
    "43":"草元素ダメージ",
    "44":"風元素ダメージ",
    "45":"岩元素ダメージ",
    "46":"氷元素ダメージ",
}
#data.json用ゲーム内変数とジェネレータ用変換
equip_dict = {
    "EQUIP_BRACER" : "flower",
    "EQUIP_NECKLACE" : "wing",
    "EQUIP_SHOES" : "clock",
    "EQUIP_RING" : "cup",
    "EQUIP_DRESS": "crown"
}

#skill_lvの作成
skill_lv_list=[]
for i in my_data["avatarInfoList"][TEST_ID]["skillLevelMap"].values():
    skill_lv_list.append(i)

serch_max_elem ={}
for j in genso_buff_id.keys():
    serch_max_elem.setdefault(j,my_data["avatarInfoList"][TEST_ID]["fightPropMap"][j])
max_elem=max(serch_max_elem.items(), key = lambda x:x[1])

#星座(凸)が進んでいるかチェック
def check_const():
    #talentIdList(星座)が存在する場合はその合計数を返す
    if "talentIdList" in my_data["avatarInfoList"][TEST_ID]:
        return len(my_data["avatarInfoList"][TEST_ID]["talentIdList"])
    #talentIdListが存在しない場合は0を返す
    else:
        return 0
    
#data.jsonのuid情報
Uid : str= my_data["uid"]
#data.jsonのキャラ関連情報
CharaName : str = lang_data["ja"][str(char_data[str(my_data["avatarInfoList"][TEST_ID]["avatarId"])]["NameTextMapHash"])]
CharaConst : int = check_const()
CharaLv : int = my_data["avatarInfoList"][TEST_ID]["propMap"]["4001"]["val"]
CharaLove : int = my_data["avatarInfoList"][TEST_ID]["fetterInfo"]["expLevel"]
CharaMaxHP : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["2000"]
CharaMaxAtk : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["2001"]
CharaMaxDef : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["2002"]
CharaElemMast : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["28"]
CharaCritRate : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["20"]
CharaCritDmg : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["22"]
CharaElemRate : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["23"]
CharaElemBuff : str = genso_buff_id[max_elem[0]]
CharaBuffRate : int = max_elem[1]

CharaNormalLv : int = skill_lv_list[0]
CharaSkillLv : int = skill_lv_list[1]
CharaUltLv : int = skill_lv_list[2]

CharaBaseHP : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["1"]
CharaBaseATK : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["4"]
CharaBaseDef : int = my_data["avatarInfoList"][TEST_ID]["fightPropMap"]["7"]

#data.jsonの武器関連情報
WeaponName : str = lang_data["ja"][my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["flat"]["nameTextMapHash"]]
WeaponLv : int = my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["weapon"]["level"]
WeaponTotu : int = max(my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["weapon"]["affixMap"].values()) + 1
WeaponRare : int = my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["flat"]["rankLevel"]
WeaponBaseATK : int = my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["flat"]["weaponStats"][0]["statValue"]
WeaponSubName : str = lang_data["ja"][my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["flat"]["weaponStats"][1]["appendPropId"]]
WeaponSubValue : int = my_data["avatarInfoList"][TEST_ID]["equipList"][-1]["flat"]["weaponStats"][1]["statValue"]
#data.jsonの聖遺物情報
equip_list = ("EQUIP_BRACER","EQUIP_NECKLACE","EQUIP_SHOES","EQUIP_RING","EQUIP_DRESS")
equip_sublist ={}
subop_value_list = []

last_equip = {}
for equip_item in my_data["avatarInfoList"][TEST_ID]["equipList"]:
    if "equipType" in equip_item["flat"] and equip_item["flat"]["equipType"] in equip_list:
        subop_value_list = []
        for subop in equip_item["flat"]["reliquarySubstats"]:
            subf = lang_data["ja"][subop["appendPropId"]]
            subfv = subop["statValue"]
            subop_value_list.append({"option": subf, "value": subfv})
        equip_sublist[equip_item["flat"]["equipType"]] = subop_value_list

for equip_item in my_data["avatarInfoList"][TEST_ID]["equipList"]:
    if "equipType" in equip_item["flat"] and equip_item["flat"]["equipType"] in equip_list:
        equipType = equip_dict[equip_item["flat"]["equipType"]]
        equipName = lang_data["ja"][equip_item["flat"]["setNameTextMapHash"]]  
        equipLv = equip_item["reliquary"]["level"]
        equipRank = equip_item["flat"]["rankLevel"]
        equipMainOpt = lang_data["ja"][equip_item["flat"]["reliquaryMainstat"]["mainPropId"]]
        equipMainVal = equip_item["flat"]["reliquaryMainstat"]["statValue"]
        last_equip.setdefault(equipType)
        last_equip[equipType] = {
            "type": equipName,
            "Level": equipLv,
            "rarelity":equipRank,
            "main":{
                "option":equipMainOpt,
                "value":equipMainVal
            },
            "sub":equip_sublist[equip_item["flat"]["equipType"]]
        }

#data.jsonのスコア用データ
set_state = "atk"
def get_score(type,state = set_state):
    score = 0
    if type in last_equip:
        for subop in last_equip[type]["sub"]:
            if subop["option"] == "会心率":
                score = score + subop["value"] * 2
            elif subop["option"] == "会心ダメージ":
                score = score + subop["value"]
            
            if state == "atk":
                if subop["option"] == "攻撃パーセンテージ":
                    score = score + subop["value"]
            elif state == "def":
                if subop["option"] == "防御パーセンテージ":
                    score = score + subop["value"]
            elif state == "hp":
                if subop["option"] == "HPパーセンテージ":
                    score = score + subop["value"]
            elif state == "recharge":
                if subop["option"] == "元素チャージ効率":
                    score = score + subop["value"]
            elif state == "jukuchi":
                if subop["option"] == "元素熟知":
                    score = score + subop["value"] * 0.25
        return score
    else:
        return 0
        
ScoreFlower : int = get_score("flower",set_state)
ScoreWing : int = get_score("wing",set_state)
ScoreClock : int = get_score("clock",set_state)
ScoreCup : int = get_score("cup",set_state)
ScoreCrown : int = get_score("crown",set_state)
TotalEquipScore : int = ScoreFlower + ScoreWing + ScoreClock + ScoreCup + ScoreCrown

#data.jsonの元素データ
Element : str = genso[char_data[str(my_data["avatarInfoList"][TEST_ID]["avatarId"])]["Element"]]

#data.jsonの作成
datajson = {}
datajson["uid"] = Uid
datajson["Character"] = {
    "Name":CharaName,
    "Const":CharaConst,
    "Level":int(CharaLv),
    "Love":CharaLove,
    "Status":{
        "HP":round(CharaMaxHP),
        "攻撃力":round(CharaMaxAtk),
        "防御力":round(CharaMaxDef),
        "元素熟知":round(CharaElemMast),
        "会心率": round(CharaCritRate*100,1),
        "会心ダメージ":round(CharaCritDmg*100,1),
        "元素チャージ効率":round(CharaElemRate*100,1),
        CharaElemBuff:round(CharaBuffRate*100,1)
    },
    "Talent":{
        "通常":CharaNormalLv,
        "スキル":CharaSkillLv,
        "爆発":CharaUltLv
    },
    "Base":{
        "HP":round(CharaBaseHP),
        "攻撃力":round(CharaBaseATK),
        "防御力":round(CharaBaseDef)
    }
}
datajson["Weapon"] = {
    "name": WeaponName,
    "Level": WeaponLv,
    "totu": WeaponTotu,
    "rarelity": WeaponRare,
    "BaseATK": WeaponBaseATK,
    "Sub": {
        "name": WeaponSubName,
        "value": WeaponSubValue
    }

}
datajson["Score"] = {
    "State": "攻撃",
    "total": TotalEquipScore,
    "flower": ScoreFlower,
    "wing": ScoreWing,
    "clock": ScoreClock,
    "cup": ScoreCup,
    "crown": ScoreCrown
}
datajson["Artifacts"] = last_equip
datajson["元素"] = Element

with open('data.json','w', encoding= "utf-8") as f:
    json.dump(datajson, f, indent=4 ,ensure_ascii=False)

