import pyodbc

server = 'secretsasquatchsociety.database.windows.net'
database = 'sasquatch'
username = 'Sasquatch'
password = 'Whadyatalkinabeet1'
driver = '{ODBC Driver 17 for SQL Server}'

reg = {
    'fname': 'Test',
    'lname': 'Tester',
    'email': 'test@test.com',
    'pass': 'test',
    'deptcode': '1234567'
}

log = {
    'email': 'test@test.com',
    'pass': 'pass'
}

cnxn = pyodbc.connect(
    'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
    )
cursor = cnxn.cursor()

def register(cursor, args):
    sql = 'EXEC [usr].[getUserByEmail] @Email=?'
    cursor.execute(sql, args['email'])
    rc = cursor.fetchall()
    if not rc:
        sql = 'EXEC [usr].[registerUser] @FirstName=?, @LastName=?, @Email=?, @Pass=?, @DepartmentCode=?'
        values = (args['fname'], args['lname'], args['email'], args['pass'], args['deptcode'])
        cursor.execute(sql, values)
        cursor.commit()
        return {
            'HttpResponse': 200,
            'Info': 'User account created'
        }
    return {
        'HttpResponse': 400,
        'Info': 'Email registered with an existing account'
    }

def login(cursor, args):
    sql = """\
        DECLARE @RC int
        EXEC @RC = [usr].[loginUser] @Email=?, @Pass=?
        SELECT @RC as rc
        """
    values = (args['email'], args['pass'])
    rc = cursor.execute(sql, values).fetchval()
    if rc == 200:
        return {
            'HttpResponse': 200,
            'Info': 'Login Successful'
        }
    elif rc == 400:
        return {
            'HttpResponse': 200,
            'Info': 'Login Successful'
        }

print(register(cursor, reg))
print(login(cursor, log))
