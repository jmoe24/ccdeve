# The first step to start using a Terraform provider like the ACI Terraform provider is to define 
# a provider in your Terraform Plan. A Terraform Plan is the configuration file that describes 
# the providers, resources, and data sources that represent your infrastructure using the HashiCorp 
# Configuration Language (HCL). The default Terraform Plan file is named main.tf.

# You can see that the first part of the main.tf file points to the source of the provider.
# The next part contains the definition of the ACI provider and the necessary parameters 
# needed to instantiate it.
# In this example of the ACI provider configuration, the username, password, and URL used to 
# establish a connection the APIC API.

# The ACI provider uses those parameters to instantiate each resource or to retrieve information 
# for each data source. You can define multiple providers in your main.tf to be able to interact
#  with multiple third-party systems in the same plan.

terraform {
  required_providers {
    aci = {
      source = "ciscodevnet/aci"
    }
  }
}

# Note that var.user.username, var.user.password, and var.user.url denotes variables defined
#  in the variable.tf file:

provider "aci" {
  # cisco-aci user name
  username = var.user.username
  # cisco-aci password
  password = var.user.password
  # cisco-aci url
  url      = var.user.url
  insecure = true
}

# Define an ACI Tenant Resource
resource "aci_tenant" "terraform_tenant" {
    name        = "terraform_tenant"
    description = "This tenant is created by terraform"
}

# Define an ACI Tenant VRF Resource
resource "aci_vrf" "terraform_vrf" {
    tenant_dn   = aci_tenant.terraform_tenant.id
    description = "VRF Created Using Terraform"
    name        = var.vrf
}

# Define an ACI Tenant BD Resource
resource "aci_bridge_domain" "terraform_bd" {
    tenant_dn          = aci_tenant.terraform_tenant.id
    relation_fv_rs_ctx = aci_vrf.terraform_vrf.id
    description        = "BD Created Using Terraform"
    name               = var.bd
}

# Define an ACI Tenant BD Subnet Resource
resource "aci_subnet" "terraform_bd_subnet" {
    parent_dn   = aci_bridge_domain.terraform_bd.id
    description = "Subnet Created Using Terraform"
    ip          = var.subnet
}