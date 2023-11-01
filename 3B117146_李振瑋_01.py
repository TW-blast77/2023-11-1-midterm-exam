#全程手摳,無使用Chat GPT
#全程手摳,無使用Chat GPT
#全程手摳,無使用Chat GPT
def preprocess(number):
    b = 0
    for i in range (number):
        if i % 2 == 1:
           b+=1
    return b

number = input("請輸入星星數量 : ")
number = int(number)
odd_number = preprocess(number)
text = "*"
f = "*"
if __name__ == '__main__':
    for i in range (odd_number+1):#上半部
        for i in range (odd_number-i):#打印空白
              print(" ",sep="",end="")
        print(text)#打印星星
        text =  text + "**"
    for i in range (odd_number):#下半部
        for x in range (((odd_number-odd_number)+1)+i):
            print(" ",sep="",end="")#打印空白
        for i in range((odd_number-1)-i):
            f = f + "**"
        print(f)#打印星星
        f = "*"#重製星星數
   
       
