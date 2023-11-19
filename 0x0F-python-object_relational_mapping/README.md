<html>
<head>
</head>
<h1>Object-relational Mappers (ORMs)</h1>
<br>
<p>An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.</p>

<h3>Why are ORMs useful?</h3>
<br>
<p>ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.</p>
<br>
<p>For example, without an ORM a developer would write the following SQL statement to retrieve every row in the USERS table where the zip_code column is 94107:

SELECT * FROM USERS WHERE zip_code=94107;
iThe equivalent Django ORM query would instead look like the following Python code:

users = Users.objects.filter(zip_code=94107)
</p>
<h4> Object Relational Tutorial </h4>
<p>The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows, called a unit of work, as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.</p>
<br>
<h5>Version Check</h5>
<p>A quick check to verify that we are on at least version 1.3 of SQLAlchemy</p>
<br>
<p>import sqlalchemy
sqlalchemy.__version__ </p>
<br>
<h5>Connecting</h5>
<p>For this tutorial we will use an in-memory-only SQLite database. To connect we use create_engine():</p>
<br>
<p>from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)</p>

</html>
