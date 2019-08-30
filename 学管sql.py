import pymysql
def pymysql_hui():
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
    cursor = connect.cursor()
    cursor.execute("create table students(id varchar(10) unique ,name varchar(10),sex varchar(5),age varchar(10),phone varchar(20))")
    connect.commit()
    cursor.close()
    connect.close()
def show_students():        # 查询
    print('ID','\t' '  ','姓名',' ','性别','  ' ,'年龄','  ','电话')
    print('*'*50)
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
    cursor = connect.cursor()
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    for i in row:
        print(i)
    connect.commit()
    cursor.close()
    connect.close()
def add_students():      # 添加
    id = input('新学生学号:')
    name = input('新学生姓名:')
    sex = input('新学生性别：')
    age = input('新学生年龄：')
    phone = input('新学生电话:')
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
    cursor = connect.cursor()
    try:
    # eow = "INSERT INTO students VALUES ("+id+',"'+name+'","'+sex+'",'+age+','+phone+");"
        eow = "INSERT INTO students VALUES ('%s','%s','%s','%s','%s')"%(id,name,sex,age,phone);
        print(eow)
        cursor.execute(eow)
        connect.commit()
        cursor.close()
        connect.close()
    except:
        print('      该ID已存在')
def update_students():      # 改
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
    cursor = connect.cursor()
    new_xh = input('请输入要修改的学生ID：')
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    try:
        for a in row:
            if new_xh == a[0]:
                new_id = input('新学生学号:')
                new_ne = input('新学生姓名:')
                new_sex = input('新学生性别：')
                new_age = input('新学生年龄：')
                new_phone = input('新学生电话:')
                cursor.execute("""update students set id=%s,name=%s,sex=%s,age=%s,phone=%s where id =%s""",(new_id,new_ne, new_sex, new_age, new_phone,new_xh,))
                connect.commit()
                cursor.close()
                connect.close()
    except:
        print('该ID已存在')
    else:
        print('      该学生不存在')
def delete_students():
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
    cursor = connect.cursor()
    new_xh = input('请输入要删除的学生ID：')
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    try:
        for a in row:
            if new_xh == a[0]:
                cursor.execute("""delete from students where id=%s""",(new_xh))
                connect.commit()
                cursor.close()
                connect.close()
    except:
        print('操作异常，请从新操作')
    else:
        print('      该学生不存在')
def main():     # 主函数，程序入口
    while True:
        print("""
            欢迎使用学生管理系统
            1-查看学员信息
            2-添加学员信息
            3-修改学员信息
            4-删除学员信息
            0-退出程序
            """)
        num = int(input('请输入操作编号：'))
        if num == 1:
            show_students()
        elif num == 2:
            add_students()
        elif num == 3:
            update_students()
        elif num == 4:
            delete_students()
        elif num == 0:
            break
if __name__ == '__main__':
    main()

