#全程手摳,無使用Chat GPT
#全程手摳,無使用Chat GPT
#全程手摳,無使用Chat GPT
def input_f():
    for i in range(len(Q)):
        while True:
            
            score = input(Q[i])
            if(i==0 or i==1):
                df[Q[i]] = score
                break
            try:
                score = float(score)
                if 0 <= score <= 100:
                    df[Q[i]] = score
                    break
                else:
                    print("輸入大於100或小於0!請重新輸入")
            except ValueError:
                print("請輸入有效的成績（0-100之間）！")

def preprocess():
    for x in range(2, len(Q)):
        df[Q[x]] = float(df[Q[x]])

def desh():
    for i in range(50):
        print("-", end="")
    print(" ")
if __name__ == '__main__':
    Q = ['請輸入您的學號：', '請輸入您的姓名：', '請輸入您的國文成績：', '請輸入您的數學成績：', '請輸入您的電腦成績：']
    df = {}
    total = round(df[Q[2]] + df[Q[3]] + df[Q[4]], 2)
    mid = round(total / (len(Q) - 2), 2)

    input_f()
    preprocess()
    desh()#分隔
    print(f"{df[Q[1]]}({df[Q[0]]})同學您好:")
    print("以下是您的各科成績與分數評定\n")
    print(f"國文 : {df[Q[2]]} / 數學 : {df[Q[3]]} / 電腦 : {df[Q[4]]}")
    print(f"總分 : {total:.2f} / 平均 : {mid:.2f}")
    desh()#分隔

    if mid >= 60:
        print(f'成績判定 : 合格')
    else:
        print("成績判定 : 不合格")

    print()
