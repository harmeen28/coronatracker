import re
from datetime import datetime, timezone

Class Date_Convertor: #AGGREGATE ROOT
 def _init_(self,str,reg_all,DT_Obj):
     self.string = str
     self.regAll = reg_all
     self.DT_Obj = DT_Obj
    
#str = "Sat, 25 Jan 2020 01:52:22 +2000"
#all = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4} \b(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9] [\+]{1}[0-9]{4}\b", str)

Convert_Date = Date_Convertor("Sat, 25 Jan 2020 01:52:22 +2000",
                     re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4} \b(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9] [\+]{1}[0-9]{4}\b", str),
                     datetime.strptime(datetime_str, '%d %b %Y %H:%M:%S %z'))


#datetime_str = all[0] # '09/19/18 13:55:26'

#datetime_object = datetime.strptime(datetime_str, '%d %b %Y %H:%M:%S %z')

print(type(datetime_object))
print(datetime_object)  # printed in default format
print(datetime_object.astimezone(timezone.utc))
