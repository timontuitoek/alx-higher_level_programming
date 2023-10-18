<html>
<h1>Create a New User and Grant Permissions in MySQL</h1>
<h2>Creating a New User</h2>
<p>create a new user with a CREATE USER statement. These follow this general syntax:
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
</p2>
<h2>Granting a User Permissions</h2>
<p>The PRIVILEGE value in this example syntax defines what actions the user is allowed to perform on the specified database and table.
GRANT PRIVILEGE ON database.table TO 'username'@'host';
To illustrate, the following command grants a user global privileges to CREATE, ALTER, and DROP databases, tables, and users, as well as the power to INSERT, UPDATE, and DELETE data from any table on the server. 
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
</p>
</html>
