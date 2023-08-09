# 列表（list）：[]    列表的元素是可以重复的
# list[起始索引,结束索引]切片时包含起始索引位置的元素，但不包含结束索引位置的元素
list1 = [20, 3.14, True, "七木", "荷花鱼", [1, 2, 3, 4]]
print(list1[2:4])  # [true,'七木']
print(list1[5][1])  # 2
list1.append("焕蓝")	#默认追加元素到列表的末尾	-P1
list1.insert(5, "kingo")	#指定位置迸行元素插入	--P2
list1.extend(["十又", "kingo", "陌上寸草", "大丑"])  #两个列表合并--P3
print(list1)

#删除
list1.pop(0)	#默认鹏除最后一个元素，也可以拊定位置（索引）进行鹏除
list1.remove(3.14)		#指定元素本身进行驱除
#list1.clear()	#清除所有元素
print(list1)

# 列表的元素是可以重复的   --统计个数count()
list1.append("方方士")
print(list1)
print(list1.count("方方士"))



# 元组  tuple()
# 元组的元素是不可以被改变的
tuple1 = ('方方士', '七木', '荷花值', 'kingo', 'Amice', '焕蓝', '十又', 'bingo', '陌上寸草', '大丑')
# 元组的元素是可以重复的

# list和tuple的互相转换
list1 = list(tuple1)  #把元组转化为列表
list1[-1] = "小丑"
print(list1)
tuple2 = tuple(list1)
print(tuple2)


# 字典：dict{}
# 3.1、元素: key: value(键值对）
# 场景:存储数据属性:人--名字 身高 体重
# key: 1）不能是可以改变的数据类型（list，dict) ---字符串;
# 2）不能重复的，唯一的
# value:可以是任意数据类型	--可以被改变	==增删改

# 字典是没有顺序的!!--不能用索引取值- 取值:通过key取value
dict1 = {"name": "tan", "height": "173", "weight": "160"}  #空字典
print(dict1["height"])	#key--value 1
print(dict1.get("weight"))	#key-- value2
dict1["weight"] = "150"		#key存在，修改对应key 的value
print(dict1)
# 添加
dict1["age"] =18   	#key不存在，新增加键值对
print(dict1)
dict1.update({"city": "北京", "hobby": "学习python", "gender": "male"})  #字典的合并
# 删除
dict1.pop("weight")	#指定key删除对应的键值对
print(dict1)
#del dict1		#变最存储	删除--对象不存在了
# print (dict1)


# 集合: set{}   ，元素单个   --了解
# 4.1、无序
# 4.2、元素不可以重复—使用场景:去重
list2 = [11, 22, 11, 33, 11, 11]  #去重
set1 = set(list2)		#set() --list2转化为集合
print(set1)
list3 = list(set1)		#list() --set1转化为列表
print(list3)
