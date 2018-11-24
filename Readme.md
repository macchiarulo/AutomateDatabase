Step 1) Download XAMPP, run Apache and MySQL to access php local host path, usually on most computers_
google search "localhost/php" after running Apache and MySQL. Make sure all files are saved in that directory.
Step 2) Save blank text file to php local host path.
Step 3) Save the s3.php and index.php to local host path.
Step 4) Make sure to have a MySQL database running for the python code to query from.
Step 5) Run python code. I reccomend running the python code every five minutes so text file is always refreshed with new data.

Summary:
The python code is appending the text file with the MySQL database data and then is automatically uploading it to S3 bucket with php.
The end result is a text file hosted on S3 with the MySQL queried data.
Benefits: No liability of hosting a MySQL database directly on a webpage_
rather you are uploading a simple text file.
