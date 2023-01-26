# About the repository

This repository contains words, phrases, and grammar structures found by me in
various technical documentation that can be used and reused.

The main purpose is to make technical English better.

Currently, this repository contains the database of words and Python scripts for adding these words into the database. 

Database access:

sqlite3 words.db - open the database
.tables - retrieve the table name
select * from WORDS; - select all entries from the WORDS table
.schema - retrieve the names of the columns in the WORDS table
select * from WORDS where LANGUAGE IS 'German'; - retrieve all German words



