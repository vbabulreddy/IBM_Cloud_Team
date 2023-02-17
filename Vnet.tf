# Vnet creation 
resource "azurerm_virtual_network" "Vnet-03" {
  name                = var.Vnet_name
  location            = var.WU-RG_location
  resource_group_name = var.WU-RG_name
  address_space       = var.vnet_range
}

resource "azurerm_subnet" "Subnet_01" {
  name                 = var.Subnet_1
  resource_group_name  = var.WU-RG_name
  virtual_network_name = var.Vnet_name
  address_prefixes     = var.Internal
}
