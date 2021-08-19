#Python script to deallocate VM in Azure

AZ_SUBSCRIPTION_ID = 
AZ_CLIENT_ID = 
AZ_TENANT_ID = 
AZ_SECRET = 
AZ_RESOURCE_GROUP_NAME = 
VM_NAME = 
#AZ_LOCATION = 


# ------------------------------------ #

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient


def get_credentials():
    subscription_id = AZ_SUBSCRIPTION_ID
    credentials = ServicePrincipalCredentials(
        client_id=AZ_CLIENT_ID,
        secret=AZ_SECRET,
        tenant=AZ_TENANT_ID
    )
    return credentials, subscription_id

credentials, subscription_id = get_credentials()


compute_client = ComputeManagementClient(credentials, subscription_id)
resource_group_name = AZ_RESOURCE_GROUP_NAME
vm_name = VM_NAME
result = compute_client.virtual_machines.deallocate(resource_group_name, vm_name)

print("deallocate done")
