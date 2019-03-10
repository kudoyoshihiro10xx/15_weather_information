def main():
    # 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},

        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},

        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温は？

    sum = 0

    for info in weather_information:
        sum = sum + info["temperature"]

    print(sum / len(weather_information))

    # Q2. 大阪府のすべての駅名を出力してね。
    for xxx in weather_information:
        if xxx["prefecture"] == "大阪府":
            print(xxx["station"])

    # Q3. 福岡県の平均気温は？
    # zzz = 0
    # aaa = 0
    # bbb = 0
    #
    # for yyy in weather_information:
    #     if yyy["prefecture"] == "大阪府":
    #         zzz = zzz + yyy["temperature"]
    #         if yyy["prefecture"] == "大阪府":
    #             bbb = 1
    #             aaa = aaa + bbb
    # # print(aaa)
    # print(zzz / aaa)

    # 別解
    total_temp = 0
    count = 0

    for record in weather_information:
        if record["prefecture"] == "大阪府":
            total_temp = total_temp + record["temperature"]
            count += 1
    print(total_temp / count)

    # 最高気温が9.0より大きい駅名を教える

    for ccc in weather_information:
        if ccc["temperature"] > 9.0:
            print(ccc["station"])


if __name__ == "__main__":
    main()
