from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class AzureSearchPublicNetworkAccessDisabled(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that Azure Cognitive Search disables public network access"
        id = "CKV_AZURE_124"
        supported_resources = ['azurerm_search_service']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'public_network_access_enabled'

    def get_expected_value(self):
        return False


check = AzureSearchPublicNetworkAccessDisabled()
