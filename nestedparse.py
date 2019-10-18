# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:18:32 2019

@author: jaya.kumar

Script to parse nested json files and extract all fields and their types
"""

 

  
def parse(data):     
    field_value_list = [] 
    res_list = []
    
    
    if type(data) == list:
        for row in data:
            field_value_list.append(parsejson(row, JsonFields = {}))     
              
        if(len(field_value_list)) > 1:
            #Uneven json structure
            for i in range(len(field_value_list)):
                if field_value_list[i] not in field_value_list[i + 1:]: 
                    res_list.append(field_value_list[i])                     
#            field_value_list = list({frozenset(item.items()) : item for item in field_value_list}.values())

               
    elif type(data) == dict:
        res_list.append(parsejson(data, JsonFields = {}))      
        
    return res_list
        

def parsejson(data, JsonFields, category=None):    
    for key, value in data.items():
        if isinstance(value,dict):
            parsejson(value, JsonFields, key)
        else:
            JsonFields.update({(key  if category == None else category+'.'+key):type(value).__name__})    
    return JsonFields
    