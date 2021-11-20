""" #承接 is index len remove pop sort
append(b)
extend
a.index(1)=>无 ValueError 值报错
del 非函数，函数加（） del是命令 eg：del ls【3】
remove: Ls.remove(7) 仅删首个7=>无 值报错
pop： a=ls.pop() 只能删最后的
sort a.sort()升序 a.sort(reverse=true) 降序 """

#2.3列表设计
#max，min,sum

#2.4列表统计
#sc.count(90) 出现的次数

#2.4.5列表切片
#ls[2:6:1] 1:步长2+1=3 被选中 6是假尾巴

#2.5 三大结构
""" 顺序结构 分支结构 循环结构
分支结构：双分支 if
        多分支 级联：if-elife-else
print（''%（）） %前十是格式控制 %后是输出项列表
1.单分支
3.双分支 if-else
4.多分支 if-elif-els """
#=> 输入一个数判断是不是水仙花数 eg：153
""" sc=eval(input('输入一个三位数:'))
# 将字符串str当作有效的表达式来求值并返回计算结果
gw=sc%10
sw=sc%100//10
bw=sc//100
if pow(gw,3)+pow(sw,3)+pow(bw,3)==sc:
    print('%d这个数是一个水仙花数' % sc)
else: #没else会执行两个printprint
    print('%d这个数不是一个水仙花数' % sc)
tip:1.else可不包含 
2.
if sc<60:
    elif sc>=60 and sc<85 #要避免重复包含 """
    
#3.2循环

#3.2.1 while 循环
""" 
三要素：1.控制表达式 2.控制变量 3.控制变量的增量
n=100 2
while n>=2: 1
    n-=2 3
 """

练：求1~100的数的和
数学思维： ((a1+an)n)/2
计算机思维：
