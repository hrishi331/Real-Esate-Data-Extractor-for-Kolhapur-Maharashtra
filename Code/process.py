import pickle 
import numpy as np
import pandas as pd

tab = {'price' : [],
       'min_price' : [],
       'max_price' : [],
       'owner_name' : [],
       'ownership_type' : [],
       'locality' : [],
       'sqftprice' : [],
       'prop_type' : [],
       'city' : [],
       'carpet_area' : [],
       'carpet_area_unit' : [],
       'covered_area' : [],
       'covered_area_unit' : []
       }


with open ("Database/prop_list.pkl","rb") as file:
    f = pickle.load(file)



for i in f:
    tab['price'].append(i.get('price',np.nan))
    tab['min_price'].append(i.get('minPrice',np.nan))
    tab['max_price'].append(i.get('maxPrice',np.nan))
    tab['owner_name'].append(i.get('oname',np.nan))
    tab['ownership_type'].append(i.get('OwnershipTypeD',np.nan))
    tab['locality'].append(i.get('lmtDName',np.nan))
    tab['sqftprice'].append(i.get('sqFtPrice',np.nan))
    tab['prop_type'].append(i.get('propTypeD',np.nan))
    tab['city'].append(i.get("defaultAdddressGoogle",np.nan))
    tab['carpet_area'].append(i.get('carpetArea',np.nan))
    tab['carpet_area_unit'].append(i.get('carpAreaUnit',np.nan))
    tab['covered_area'].append(i.get('coveredArea',np.nan))
    tab['covered_area_unit'].append(i.get('coverAreaUnitD',np.nan))


table = pd.DataFrame(tab)
with open ("Database/res_prop.pkl","wb") as file:
    pickle.dump(table,file=file)

table.to_csv("Database/res_prop.csv",index=False)

print(table)

