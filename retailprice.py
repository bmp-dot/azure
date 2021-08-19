import requests
#import urllib3

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

size = "Standard_B1ms"
region ="westus2"

#Get Prices
response = requests.get("https://prices.azure.com/api/retail/prices?$filter= armRegionName eq 'westus2' and serviceName eq 'Virtual Machines' and armSkuName eq 'Standard_B1ms'")


# Create an array to store price list
priceitems= []

#Add the retail prices returned in the API response to a list
for i in response.json()['Items']:
    priceitems.append(i) 

print(response.json()["NextPageLink"])

# Retrieve price list from all available pages until there is a 'NextPageLink' available to retrieve prices
while response.json()["NextPageLink"] != None:   
    for i in response.json()['Items']:
        priceitems.append(i) 
    response = requests.get(response.json()["NextPageLink"])
    print(response.json()["NextPageLink"])

# Retrieve price list from the last page when there is no "NextPageLink" available to retrieve prices
if response.json()["NextPageLink"] == None:
    for i in response.json()['Items']:
        priceitems.append(i) 

# Retrive price from payload filter
for armSkuName in priceitems:
    if armSkuName['productName'] == "Virtual Machines BS Series" and armSkuName['type'] == "Consumption":
        uprice = str(armSkuName['retailPrice'])

print "uprice=" + uprice
