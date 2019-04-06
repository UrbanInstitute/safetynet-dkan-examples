#
# Safetynet_DKAN.py
# DSM 3/29/2019
#
# This will get data from the datacatalog API 
# and return a dataframe with resulting records for a statid

def get_SNA_data(statid):
    import pandas as pd
    import requests
    
    recs_sofar = 0
    
    # make initial request to the DKAN API
    # filtering for a statid
    # put resulting records in pd dataframe
    #
    # Note: we're leaving out the fields[] parameter, as the default is all fields in original order
    #       there were problems passing in specific multiple field names
    #
    myurl = 'https://datacatalog.urban.org/api/action/datastore/search.json'
    myresource_id = '6fc0556b-de8b-41b9-a535-33243f2eb490'
    myparams = {'resource_id': myresource_id,
              'sort[year]': 'asc',
              'filters[statid]': '103',
              'limit': 100,
              'offset': 0
              }
    myparams['filters[statid]'] = statid
    
    # make the initial request
    r = requests.get(url = myurl,params = myparams)
    x = r.json()
    df = pd.DataFrame(x['result']['records'])
    totalrecs = x['result']['total']
    recswegot = len(x['result']['records'])
    recs_sofar = recs_sofar + recswegot
    # end initial request
    
    # keep making requests until we get all the data for the statid
    while ( recs_sofar < totalrecs) :
        myparams['offset'] = myparams['offset'] + recswegot
        r = requests.get(url = myurl,params = myparams)
        x = r.json()
        df = df.append(x['result']['records'])
        recs_sofar = recs_sofar + len(x['result']['records'])
    #ok, done
    
    print('Total recs for statid:',totalrecs)
    print('Total retrieved      :',recs_sofar)    
    return(df)
    

    

 

