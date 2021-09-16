names = ['pony','adele','jennes']

#print(names)
#print(names[0])
#print(names[1].title())
#message = f"My name is {names[0].title()}"
#print(message)

names[2] = 'richel'
#列表末尾添加元素
names.append('lilyan')
#列表任意位置插入元素
names.insert(0,'giffph')
print(names)

#根据索引删除元素del()
#del names[4]
#弹出元素/弹出指定位置元素pop()
#names.pop()
#根据值删除元素remove()
#names.remove('adele')
#print(names)

#永久性排序
#names.sort()
#永久性逆序排序
#names.sort(reverse=True)

#临时性排序
#names.sorted()
#临时性逆序排序
#names.sorted(reverse=True)

#确定列表长度len()
print(len(names))