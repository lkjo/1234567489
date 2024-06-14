#計算複利程式
#讀取xml的資料且使用
def f(money,interest,month):
    result = 0#存身上有多少錢
    for i in range(month):#跑每個月存的錢
        #i是目前跑到第幾個月
        #代表還有month-i個月要跑
        result += money*((interest+100)/100)**(month-i)
        #interest代表的是%數，所以要+100然後除以100
    return result
    #當存錢時還剩下month個月，代表要跑month個月的月息
    #每個月存money
    #月息:interest%
    #月:month
    #用for，答案要return
print(f(1000000,1.74,3))
#2. 幫我exe化
#3. 上傳至github
#4. 介紹程式
#5. 貼網址製作業