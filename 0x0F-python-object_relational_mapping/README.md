<html>
<head>
<title>Object-relational Mappers (ORMs)</title>
</head>
<h1>Object-relational Mappers</h1>
<br>
<p>An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.</p>

<h3>Why are ORMs useful?</h3>
<br>
<p>ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.</p>
<br>
<p>For example, without an ORM a developer would write the following SQL statement to retrieve every row in the USERS table where the zip_code column is 94107:

SELECT * FROM USERS WHERE zip_code=94107;
The equivalent Django ORM query would instead look like the following Python code:

# obtain everyone in the 94107 zip code and assign to users variable
users = Users.objects.filter(zip_code=94107)
</p>

</html>
