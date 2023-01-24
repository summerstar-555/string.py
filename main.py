#字符串有三种定义方式
'''
1.单引号
2.双引号
3.三引号（如果不用变量去接受就是注释的一种方式，反之则是一种字符串定义方式）
'''

#三引号应用
'''a = \'''
\t悯农
\t李绅
锄禾日当午，汗滴禾下土。
谁知盘中餐，粒粒皆辛苦。\'''
print(a);'''

#在双引号内包含双引号
'''
a = "\"这是一句话。\""
print(a);
'''

#字符串拼接
'''
a = "你";
b = "干";
c = "嘛";
print(a+b+c);'''

'''
address = "移动营业厅";
tel = "1008611"; #拼接只能用于字符串类型，所以这里加上双引号
print(address + tel);
'''

#字符串格式化(差不多也是拼接)
'''
num = 1;
num1 = 18;
#如果是连接多个变量需要加上“括号”
a = "我中专毕业已经整整%s年了，今天距离开学也只剩%d天了" % (num,num1); #这里可以用%s也可以用%d
print(a);
'''

#字符串格式化精度控制
#重点：如果一个数字只有两位，宽度限制设置为1，那么就不生效
#例如：a = 10;print("数字限制为1，不生效。结果为：%1d" % a)
#保留小数点.n还会对数据做一个四舍五入的操作
'''
a = 10.235;
b = "%6.2f这个数字的宽度为6,并且取小数点后两位\n" % a;
c = "%.3f这个数字不限制宽度，取小数点后三位" % a;
print(b);
#上面那句代码也可以这么写
print("%6.2f这个数字的宽度为6,并且取小数点后两位\n" % a);
print(c);
'''

#字符串格式化-快速写法
'''
name = "坤坤";
music = "鸡你太美";
year = "2018";
print(f"她的名字是：{name}\n成名曲:{music}\n年份为：{year}");
#可在花括号中放表达式
print(f"5*5的结果为{5*5}");
'''

#综合练习
'''
name = "坤坤";
price = 19.99;
code = 123456;
price_daily = 1.2;
days = 7;
res = price_daily ** days * price;
print(f"公司：{name},代码：{code}，价格:{price}");
print("每日增长价格%.1f,经过%d天的增长，股价达到了:%.2f" % (price_daily,days,res));
'''


# 对字符串进行是否为数字的判断
'''
def is_num(string: str)-> bool:
    """
    :param string: 
    :return: bool
    对字符串进行判断，如果字符串内的所有字符皆为数字，则返回True，否则返回False
    """
    for char in a:      # 对字符串内的每个字符进行检查
        asc_val = ord(char)
        if 48 <= asc_val <= 57:
            continue
        else:
            return False
    return True


while 1:
    a = input('>>>')
    if is_num(a):
        # print('这是数字')
        a = int(a)
        try:
            assert a > 0
        except AssertionError:
            print('请输入大于0的数字')
    else:
        print('非数字,请输入数字')
'''