# ParseJson
Python module to Parse nested json file

Input: Nested json file content (in dict or list format)
Ouput: Returns a dict of all json fields and their data types. If the json format is consistent multiple dicts will be returned for each format.

## Steps
1. Download the **nestedparse.py** file and place it inside the Lib/site_packages folder
2. Load the json data as usual using <br/> 
**with open("ictnl-2019-09.json") as datafile:    
   &nbsp; data = json.load(datafile)**
2. To call the parser use **nestedparse.parse(data)**. Make sure the original data is in either dict or list format.


