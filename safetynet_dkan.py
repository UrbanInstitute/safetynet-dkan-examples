#
# Safetynet_DKAN.py
# DSM 3/29/2019
#
# This will get data from the datacatalog API 
# and return a dataframe with resulting records for a statid
#
# get_SNA_data(statid)
# get_SNA_meta(statid)
#

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
       
    myprogram_name = validate_statid(statid)
    
    # define a dictionary of program resourceids by programs
    myprogram_resources = {'SNAP'       :'6fc0556b-de8b-41b9-a535-33243f2eb490', 
                           'TANF'       :'a77378a2-f26b-4802-be45-d558ea47b65b',
                           'EITC'       :'8ecae928-c689-48cc-8953-6d4e0afc31bd',
                           'ECON'       :'f4041439-66ea-49cf-9b41-685c6036ed93',
                           'SSI'        :'47df5bf5-0305-4df1-98dd-a2320941ecd3',
                           'CCDF'       :'441d6b32-d52f-4cbf-acf7-bff14fd06bc1',
                           'HUD'        :'06eac4b8-dbcd-41bf-81ce-1b15c771d048',
                           'UI'         :'951d6ace-51d1-4956-beaa-df5db9f1e9ae',
                           'MEDICAID'   :'6ae37f37-bbe5-4961-a092-abe8742742e8'
                           } 
    

    print ('Program name is: ',myprogram_name)
    if ( myprogram_name == "ERROR"):
        print("Error, invalid statid:", statid)
        return()
    
    myurl = 'https://datacatalog.urban.org/api/action/datastore/search.json'
    
    myresource_id = myprogram_resources[myprogram_name]
    myparams = {'resource_id': myresource_id,
              'sort[year]': 'asc',
              'filters[statid]': '103',
              'limit': 100,
              'offset': 0
              }
    myparams['filters[statid]'] = statid
    myparams['filters[statecode]'] = 99
    
    # make the initial request
    r = requests.get(url = myurl,params = myparams)
    x = r.json()
    #print ( r.url )
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
#    
# get_SNA_meta(statid)
# This will just get the metadata for a statid
#    
    
def get_SNA_meta(statid):
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
    # leave this if/elif/then structure in here for validation
    #
    
    myprogram_name = validate_statid(statid)
    
    if ( myprogram_name == "ERROR"):
        print("Error, invalid statid:", statid)
        return()
    

    print ('Program name is: ',myprogram_name)
    myurl = 'https://datacatalog.urban.org/api/action/datastore/search.json'
    
    myresource_id = '4ea56583-1376-4a4e-93d3-757b736ea964'
    myparams = {'resource_id': myresource_id,
              'limit': 100,
              'offset': 0
              }
    myparams['filters[statid]'] = statid
    
    # make the initial request
    r = requests.get(url = myurl,params = myparams)
    x = r.json()
    #print ( r.url )
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
    
    print('Total meta recs for statid:',totalrecs)
    print('Total meta retrieved      :',recs_sofar)    
    return(df)   

#    
# get_SNA_graphic(statid)
# This will just get the metadata for a statid
#    
    
def get_SNA_graphic(graphicid):
    import pandas as pd
    import requests
    
    recs_sofar = 0
    

    


    myurl = 'https://datacatalog.urban.org/api/action/datastore/search.json'
    
    myresource_id = 'aa7c5ea3-ff23-494d-8bbf-a7496a0541bc'
    myparams = {'resource_id': myresource_id,
              'limit': 100,
              'offset': 0
              }
    myparams['filters[graphicid]'] = graphicid    
    
    # make the initial request
    r = requests.get(url = myurl,params = myparams)
    x = r.json()
#    print ( r.url )
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
    
    print('Total recs for graphicid  :',totalrecs)
    print('Total recs retrieved      :',recs_sofar)    
    return(df)   


#    
# validate_statid(statid)
# This will return the program name for a valid statid
#        
    
def validate_statid(statid):
    
    if   ( statid  >= 1 and statid <= 43 ):
        myprogram_name = 'TANF'    
    elif (  statid  >= 101 and statid <= 193):
        myprogram_name = 'SNAP'
    elif (  statid  >= 301 and statid <= 373):
        myprogram_name = 'EITC'
    elif (  statid  >= 901 and statid <= 903):
        myprogram_name = 'ECON'
    elif (  statid  >= 401 and statid <= 416):
        myprogram_name = 'SSI'  
    elif (  statid  >= 501 and statid <= 528):
        myprogram_name = 'CCDF' 
    elif (  statid  >= 601 and statid <= 612):
        myprogram_name = 'HUD'      
    elif (  statid  >= 701 and statid <= 731):
        myprogram_name = 'UI'    
    elif (  statid  >= 801 and statid <= 802):
        myprogram_name = 'MEDICAID'           
    else:
        print('No Coke, Pepsi?')
        return("ERROR")
        
    return(myprogram_name)        
    

    

 

