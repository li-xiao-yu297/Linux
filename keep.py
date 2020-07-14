Name = input('姓名:')
Age = input('年龄:')
Sex = input('性别:')
Xl = input('学历')
Newslist = [Name,Age,Sex,Xl]
N = open('./News','w')
N.write(str(Newslist))
N.close()

