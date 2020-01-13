import pyodbc

class Database:

    def __init__(self, driver, endpoint, db, username, passw):
        self.driver = ('DRIVER='+ driver +
            ';SERVER='+endpoint+';PORT=1433;DATABASE=' +
            db+';UID='+username+';PWD='+ passw)
        self.cnxn   = pyodbc.connect(self.driver)

    def register_user(self, args):
        cursor = self.cnxn.cursor()
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
    
    def login_user(self, args):
        cursor = self.cnxn.cursor()
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
