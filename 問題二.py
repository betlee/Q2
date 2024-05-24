number = int(input(""))##輸入組數
res = 0##歸零組數

for i in range(number):##有幾組就執行幾次
    member = int(input(""))##輸入每組數量
    if member % 3 == 0 and member > 0:##如果是合法行為
        res = res + 1##合法組數+1
print(res)##輸出合法的組數量