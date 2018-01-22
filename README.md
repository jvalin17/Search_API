## Search_API 

#### Element Search API 

#### Requirements: 
Language & Tools - Python 2.7, Javascript, HTML, SQLite3  
Framework - Flask  


#### SQL Schema 

CREATE TABLE `Chem_data` ( 
	`Chemical_formula` TEXT NOT NULL, 
	`Band_gap` real NOT NULL, 
	`Color` TEXT NOT NULL, 
	PRIMARY KEY (`Chemical_formula`) 
);



#### How to Run: 

1. Make sure the data set (data.csv), templates and all python code is in same folder (Search_API).  
2. Go to the folder ‘ Search_API ‘ from terminal/command line. 
3. Next, run code ‘route.py’ using command — “python route.py”. 
4. Go to “http://127.0.0.1:5002/” in browser. 


#### How to use Web API  

You can search elements in 2 ways: 
1. Using element Formula 
2. Using property characteristics —  
     a) Band Gap - give start range and end range number as input. 
     b) Color - Select from drop down/Enter text.  


#### Output/Result 
The elements with its properties will be displayed in output table. 

#### Exceptions: 
1. If you don’t give any input, it won’t process query. 
2. If you want to search element of specific range, please give specific number in both start and end range text boxes. 

#### Assumptions: 

1. There are just 2 properties for each element. 
2. The given data is going to remain same for any element search that is all rows are unique elements. 
3. You can search by element name or properties at a time and not by both. 
4. Search by element formula, the formula is case sensitive and should be exactly how formula is. 
5. Band Gap is always float/number. 

#### How it works: 

1. It will create a file ‘chem_data.csv’ if it doesn’t exist in same folder which is cleaned data.  
2. Then it will create a table in sqlite3 and insert data from chem_data.csv if it doesn’t exist based on schema. 
3. It will start web service on local host where you can enter/choose your requirements. 
4. It will take the requirements, query from sqlite3 and display results. 

