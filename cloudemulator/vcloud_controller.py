# -*- coding:utf-8 -*-

import webob
import wsgi
import time

from oslo_config import cfg
from common import log as logging
from ecloud.cloud_emulator import CloudManager, OperationName

CONF = cfg.CONF

LOG = logging.getLogger(__name__)

REST_DELAY = 0

CHECK_APP_DELAY = 1


class VcloudController(wsgi.Application):
    def __init__(self):
        super(VcloudController, self).__init__()

    def get_sessions(self, request):
        LOG.info("get vcloud session.")

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.session+xml;version=1.5'),
                       ('Set-Cookie',
                        'vcloud-token=D6R4x2b5PVTMW01b0AGJBCkT5/myTJAc6hc9zZ6LIO8=; Secure; Path=/'),
                       ('Vary', 'Accept-Encoding'), ('x-vcloud-authorization',
                                                     'D6R4x2b5PVTMW01b0AGJBCkT5/myTJAc6hc9zZ6LIO8=')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Session xmlns="http://www.vmware.com/vcloud/v1.5" user="huawei" org="emulator_org" ' \
               'type="application/vnd.vmware.vcloud.session+xml" href="http://162.3.201.10/api/session/" ' \
               'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
               'xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgList+xml" href="http://162.3.201.10/api/org/"/>' \
               '<Link rel="remove" href="http://162.3.201.10/api/session/"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.org+xml" name="emulator_org" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.query.queryList+xml" href="http://162.3.201.10/api/query"/>' \
               '<Link rel="entityResolver" type="application/vnd.vmware.vcloud.entity+xml" href="http://162.3.201.10/api/entity/"/>' \
               '</Session>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_org(self, request, org_id):
        LOG.info("get org, org_id= %s", org_id)

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.org+xml;version=1.5'),
                       ('Set-Cookie',
                        'vcloud-token=D6R4x2b5PVTMW01b0AGJBCkT5/myTJAc6hc9zZ6LIO8=; Secure; Path=/'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Org xmlns="http://www.vmware.com/vcloud/v1.5" name="emulator_org" id="urn:vcloud:org:379844e7-76e8-4966-821d-a73c083ea9db" type="application/vnd.vmware.vcloud.org+xml" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.vdc+xml" name="emulator_vdc" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.tasksList+xml" href="http://162.3.201.10/api/tasksList/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.catalog+xml" name="metadata-isos" href="http://162.3.201.10/api/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.controlAccess+xml" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2/controlAccess/"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.catalog+xml" name="template" href="http://162.3.201.10/api/catalog/2359a9f8-d95a-4616-998a-18dad3711a24"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.controlAccess+xml" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db/catalog/2359a9f8-d95a-4616-998a-18dad3711a24/controlAccess/"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="tunnelbearing-net" href="http://162.3.201.10/api/network/6d7f8b1a-f088-4baa-b5d3-889f43d9b375"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="internalbase-net" href="http://162.3.201.10/api/network/0e4e220d-4cf8-42e0-96a7-665694cc90ef"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="delete-externalapi-net" href="http://162.3.201.10/api/network/985855f5-8a11-4cef-8635-b4a79c6388c1"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="delete-internalbase-net" href="http://162.3.201.10/api/network/72ca8bfa-0bf0-4610-a341-f0196f76ebbd"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="externalapi-net" href="http://162.3.201.10/api/network/8e72984a-afa4-47f5-ac1c-dec4e9201899"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.orgNetwork+xml" name="delete-tunnelbearing-net" href="http://162.3.201.10/api/network/8205bc6e-f33e-46a0-bdc5-b4a18079adc6"/>' \
               '<Description/>' \
               '<FullName>emulator_org</FullName>' \
               '</Org>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_vdc(self, request, vdc_id):
        LOG.info("get vdc, vdc_id= %s", vdc_id)

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.vdc+xml;version=1.5'),
                       ('Vary', 'Accept-Encoding')]

        tm = CloudManager()
        vm_list = tm.query_virtual_machines()

        vm_body = ""
        for vm in vm_list:
            vm_body = vm_body + '<ResourceEntity type="application/vnd.vmware.vcloud.vApp+xml" name="%s" href="http://162.3.201.10/api/vApp/vapp-%s"/>' % (vm.name, vm.id)

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Vdc xmlns="http://www.vmware.com/vcloud/v1.5" status="1" name="emulator_vdc" id="urn:vcloud:vdc:61800c8d-89a4-4320-bbef-f57806b7064a" type="application/vnd.vmware.vcloud.vdc+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/metadata"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.uploadVAppTemplateParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/uploadVAppTemplate"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.media+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/media"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.instantiateOvfParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/instantiateOvf"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.instantiateVAppTemplateParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/instantiateVAppTemplate"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.cloneVAppParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/cloneVApp"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.cloneVAppTemplateParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/cloneVAppTemplate"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.cloneMediaParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/cloneMedia"/>' \
               '<Link rel="add" type="application/vnd.vmware.vcloud.composeVAppParams+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a/action/composeVApp"/>' \
               '<AllocationModel>AllocationPool</AllocationModel>' \
               '<StorageCapacity>' \
               '<Units>MB</Units>' \
               '<Allocated>5746379</Allocated>' \
               '<Limit>5746379</Limit>' \
               '<Used>284164</Used>' \
               '<Overhead>0</Overhead>' \
               '</StorageCapacity>' \
               '<ComputeCapacity>' \
               '<Cpu>' \
               '<Units>MHz</Units>' \
               '<Allocated>32000</Allocated>' \
               '<Limit>32000</Limit>' \
               '<Used>0</Used>' \
               '<Overhead>0</Overhead>' \
               '</Cpu>' \
               '<Memory>' \
               '<Units>MB</Units>' \
               '<Allocated>143360</Allocated>' \
               '<Limit>143360</Limit>' \
               '<Used>18944</Used>' \
               '<Overhead>199</Overhead>' \
               '</Memory>' \
               '</ComputeCapacity>' \
               '<ResourceEntities>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="a19d92d7-4ed0-4c22-aba2-b45790d94e44" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-bac0c657-e627-49df-a353-d94c85e980f6"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="vcloud_vgw" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-6e3469e9-e51f-45d2-9266-4a0068b349fd"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="c9354b0c-e940-4f4c-af85-58370947ba7c" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-37260524-953b-462b-a73f-c7e505bef43f"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="5dedff0e-a8a5-44e4-b43d-52eb48abc9ce" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-636bb448-207d-419e-997e-92b206791c0c"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="2a156653-e613-460d-b0ed-ce5a95c194a2" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-d8a637fb-47e5-4fab-9a67-7303ede5023b"/>' \
               + vm_body + \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@4dfb2c65-d88b-4f5d-be09-0e6e7b707959.iso" href="http://162.3.201.10/api/media/a7fa54df-b8d0-4770-8f72-1606c0b1b94b"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@553c49c1-7a04-40b6-bb61-dfbd854751e5.iso" href="http://162.3.201.10/api/media/77a6ba18-e0ff-450a-92bb-7359c417ff8f"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@48ddf85c-0d8d-49b9-b043-4d925c371500.iso" href="http://162.3.201.10/api/media/bf52ad5b-984b-4cd0-a894-22108969b864"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@01c1e6ec-992a-424a-8c85-16064b13fa2c.iso" href="http://162.3.201.10/api/media/5735fcbb-a137-4829-885b-3d70425469a6"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@017d489a-70fd-4a8c-9ff7-eee7fb9b0a51.iso" href="http://162.3.201.10/api/media/e5e6a248-81b9-4379-a4c5-ce72f7492fa6"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@91226ef0-613f-41df-9e10-271a26c4070a.iso" href="http://162.3.201.10/api/media/fe869670-d017-489c-b1d6-42107b65532d"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@81735cec-9713-4320-86b9-51c17e20b035.iso" href="http://162.3.201.10/api/media/f659faeb-26f1-4603-b19c-1e4272598f01"/>' \
               '<ResourceEntity type="application/vnd.vmware.vcloud.media+xml" name="diskNewName11-copy-de8281fd-9a67-4292-b8ef-f5228eb0b75d" href="http://162.3.201.10/api/media/90f58a52-bae9-40c5-9cfc-10b4f9ad1d72"/>' \
               '</ResourceEntities>' \
               '<AvailableNetworks>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="tunnelbearing-net" href="http://162.3.201.10/api/network/6d7f8b1a-f088-4baa-b5d3-889f43d9b375"/>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="internalbase-net" href="http://162.3.201.10/api/network/0e4e220d-4cf8-42e0-96a7-665694cc90ef"/>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="delete-externalapi-net" href="http://162.3.201.10/api/network/985855f5-8a11-4cef-8635-b4a79c6388c1"/>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="delete-internalbase-net" href="http://162.3.201.10/api/network/72ca8bfa-0bf0-4610-a341-f0196f76ebbd"/>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="externalapi-net" href="http://162.3.201.10/api/network/8e72984a-afa4-47f5-ac1c-dec4e9201899"/>' \
               '<Network type="application/vnd.vmware.vcloud.network+xml" name="delete-tunnelbearing-net" href="http://162.3.201.10/api/network/8205bc6e-f33e-46a0-bdc5-b4a18079adc6"/>' \
               '</AvailableNetworks>' \
               '<Capabilities>' \
               '<SupportedHardwareVersions>' \
               '<SupportedHardwareVersion>vmx-04</SupportedHardwareVersion>' \
               '<SupportedHardwareVersion>vmx-07</SupportedHardwareVersion>' \
               '<SupportedHardwareVersion>vmx-08</SupportedHardwareVersion>' \
               '<SupportedHardwareVersion>vmx-09</SupportedHardwareVersion>' \
               '<SupportedHardwareVersion>vmx-10</SupportedHardwareVersion>' \
               '</SupportedHardwareVersions>' \
               '</Capabilities>' \
               '<NicQuota>0</NicQuota>' \
               '<NetworkQuota>101</NetworkQuota>' \
               '<VmQuota>0</VmQuota>' \
               '<IsEnabled>true</IsEnabled>' \
               '</Vdc>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_catalog(self, request, catalog_id):
        LOG.info("get catalog, catalog_id = %s", catalog_id)

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.catalog+xml;version=1.5'),
                       ('Vary', 'Accept-Encoding'), ('x-vcloud-authorization',
                                                     'D6R4x2b5PVTMW01b0AGJBCkT5/myTJAc6hc9zZ6LIO8=')]

        if catalog_id == "80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2":
            body = '<?xml version="1.0" encoding="UTF-8"?>' \
                   '<Catalog xmlns="http://www.vmware.com/vcloud/v1.5" name="metadata-isos" id="urn:vcloud:catalog:80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2" type="application/vnd.vmware.vcloud.catalog+xml" href="http://162.3.201.10/api/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
                   '<Link rel="up" type="application/vnd.vmware.vcloud.org+xml" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
                   '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2/metadata"/>' \
                   '<Link rel="add" type="application/vnd.vmware.vcloud.catalogItem+xml" href="http://162.3.201.10/api/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2/catalogItems"/>' \
                   '<CatalogItems>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@4dfb2c65-d88b-4f5d-be09-0e6e7b707959.iso" id="e2eaaf37-d2b1-4f91-a5b8-53bec07ae992" href="http://162.3.201.10/api/catalogItem/e2eaaf37-d2b1-4f91-a5b8-53bec07ae992"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@553c49c1-7a04-40b6-bb61-dfbd854751e5.iso" id="d2c5545d-d18c-4167-bc9f-6989e226c263" href="http://162.3.201.10/api/catalogItem/d2c5545d-d18c-4167-bc9f-6989e226c263"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@01c1e6ec-992a-424a-8c85-16064b13fa2c.iso" id="1154b71f-41ab-4ed7-8e56-a13ed6087515" href="http://162.3.201.10/api/catalogItem/1154b71f-41ab-4ed7-8e56-a13ed6087515"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@017d489a-70fd-4a8c-9ff7-eee7fb9b0a51.iso" id="e4429ab7-935e-4928-8db2-391387b6b419" href="http://162.3.201.10/api/catalogItem/e4429ab7-935e-4928-8db2-391387b6b419"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@91226ef0-613f-41df-9e10-271a26c4070a.iso" id="b9f35492-aec5-45fd-8285-143e06dbd180" href="http://162.3.201.10/api/catalogItem/b9f35492-aec5-45fd-8285-143e06dbd180"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@81735cec-9713-4320-86b9-51c17e20b035.iso" id="31e453b3-61bb-456a-983e-113b0ebf46ff" href="http://162.3.201.10/api/catalogItem/31e453b3-61bb-456a-983e-113b0ebf46ff"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="diskNewName11" id="94768134-aca4-4cc9-9e9d-5c48aaa09e5f" href="http://162.3.201.10/api/catalogItem/94768134-aca4-4cc9-9e9d-5c48aaa09e5f"/>' \
                   '</CatalogItems>' \
                   '<IsPublished>false</IsPublished>' \
                   '</Catalog>'
        else:
            body = '<?xml version="1.0" encoding="UTF-8"?>' \
                   '<Catalog xmlns="http://www.vmware.com/vcloud/v1.5" name="template" id="urn:vcloud:catalog:2359a9f8-d95a-4616-998a-18dad3711a24" type="application/vnd.vmware.vcloud.catalog+xml" href="http://162.3.201.10/api/catalog/2359a9f8-d95a-4616-998a-18dad3711a24" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
                   '<Link rel="up" type="application/vnd.vmware.vcloud.org+xml" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
                   '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/catalog/2359a9f8-d95a-4616-998a-18dad3711a24/metadata"/>' \
                   '<Link rel="add" type="application/vnd.vmware.vcloud.catalogItem+xml" href="http://162.3.201.10/api/catalog/2359a9f8-d95a-4616-998a-18dad3711a24/catalogItems"/>' \
                   '<CatalogItems>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="metadata_server@48ddf85c-0d8d-49b9-b043-4d925c371500.iso" id="8638aadc-a375-4b43-ab46-1599780d4aed" href="http://162.3.201.10/api/catalogItem/8638aadc-a375-4b43-ab46-1599780d4aed"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="a19d92d7-4ed0-4c22-aba2-b45790d94e44" id="bfaf8cc3-3dd6-4461-aa30-807cad380cff" href="http://162.3.201.10/api/catalogItem/bfaf8cc3-3dd6-4461-aa30-807cad380cff"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="vcloud_vgw" id="5ed5800d-4a2a-42e9-91c5-77bab7dcd188" href="http://162.3.201.10/api/catalogItem/5ed5800d-4a2a-42e9-91c5-77bab7dcd188"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="c9354b0c-e940-4f4c-af85-58370947ba7c" id="d9b439ac-7b6e-4c57-8576-5af29c4235ff" href="http://162.3.201.10/api/catalogItem/d9b439ac-7b6e-4c57-8576-5af29c4235ff"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="2a156653-e613-460d-b0ed-ce5a95c194a2" id="36090b6b-48f0-46b5-997b-44ceab771d09" href="http://162.3.201.10/api/catalogItem/36090b6b-48f0-46b5-997b-44ceab771d09"/>' \
                   '<CatalogItem type="application/vnd.vmware.vcloud.catalogItem+xml" name="5dedff0e-a8a5-44e4-b43d-52eb48abc9ce" id="f92f5853-ed37-4724-88a6-bdc97b437929" href="http://162.3.201.10/api/catalogItem/f92f5853-ed37-4724-88a6-bdc97b437929"/>' \
                   '</CatalogItems>' \
                   '<IsPublished>false</IsPublished>' \
                   '</Catalog>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_catalog_item(self, request, catalogItem_id):
        LOG.info("get catalog_item, catalogItem_id = %s", catalogItem_id)

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.catalogitem+xml;version=1.5'),
                       ('Vary', 'Accept-Encoding'), ('x-vcloud-authorization',
                                                     'D6R4x2b5PVTMW01b0AGJBCkT5/myTJAc6hc9zZ6LIO8=')]

        if catalogItem_id == "36090b6b-48f0-46b5-997b-44ceab771d09":
            body = '<?xml version="1.0" encoding="UTF-8"?>' \
                   '<CatalogItem xmlns="http://www.vmware.com/vcloud/v1.5" size="0" name="2a156653-e613-460d-b0ed-ce5a95c194a2" id="urn:vcloud:catalogitem:36090b6b-48f0-46b5-997b-44ceab771d09" type="application/vnd.vmware.vcloud.catalogItem+xml" href="http://162.3.201.10/api/catalogItem/36090b6b-48f0-46b5-997b-44ceab771d09" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
                   '<Link rel="up" type="application/vnd.vmware.vcloud.catalog+xml" href="http://162.3.201.10/api/catalog/2359a9f8-d95a-4616-998a-18dad3711a24"/>' \
                   '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/catalogItem/36090b6b-48f0-46b5-997b-44ceab771d09/metadata"/>' \
                   '<Entity type="application/vnd.vmware.vcloud.vAppTemplate+xml" name="2a156653-e613-460d-b0ed-ce5a95c194a2" href="http://162.3.201.10/api/vAppTemplate/vappTemplate-d8a637fb-47e5-4fab-9a67-7303ede5023b"/>' \
                   '</CatalogItem>'
        else:
            body = '<?xml version="1.0" encoding="UTF-8"?>' \
                   '<CatalogItem xmlns="http://www.vmware.com/vcloud/v1.5" size="358400" name="metadata_server@4dfb2c65-d88b-4f5d-be09-0e6e7b707959.iso" id="urn:vcloud:catalogitem:e2eaaf37-d2b1-4f91-a5b8-53bec07ae992" type="application/vnd.vmware.vcloud.catalogItem+xml" href="http://162.3.201.10/api/catalogItem/e2eaaf37-d2b1-4f91-a5b8-53bec07ae992" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
                   '<Link rel="up" type="application/vnd.vmware.vcloud.catalog+xml" href="http://162.3.201.10/api/catalog/80e2a4ba-c835-4c0f-9a67-6c7d06eac7d2"/>' \
                   '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/catalogItem/e2eaaf37-d2b1-4f91-a5b8-53bec07ae992/metadata"/>' \
                   '<Entity type="application/vnd.vmware.vcloud.media+xml" name="metadata_server@4dfb2c65-d88b-4f5d-be09-0e6e7b707959.iso" href="http://162.3.201.10/api/media/a7fa54df-b8d0-4770-8f72-1606c0b1b94b"/>' \
                   '</CatalogItem>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_vapp(self, request, vapp_id):
        LOG.info("get vapp, vapp_id = %s", vapp_id)

        time.sleep(CHECK_APP_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.vApp+xml;version=1.5'),
                       ('Vary', 'Accept-Encoding')]

        tm = CloudManager()
        vm = tm.query_virtual_machine(vapp_id)

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<VApp xmlns="http://www.vmware.com/vcloud/v1.5" xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1" xmlns:rasd="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_ResourceAllocationSettingData" xmlns:vssd="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_VirtualSystemSettingData" xmlns:vmw="http://www.vmware.com/schema/ovf" xmlns:ovfenv="http://schemas.dmtf.org/ovf/environment/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ovfDescriptorUploaded="true" deployed="true" status="4" name="%(vm_name)s" id="urn:vcloud:vapp:%(vm_id)s" ' \
               'type="application/vnd.vmware.vcloud.vApp+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s" xsi:schemaLocation="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_VirtualSystemSettingData http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2.22.0/CIM_VirtualSystemSettingData.xsd http://www.vmware.com/schema/ovf http://www.vmware.com/schema/ovf http://schemas.dmtf.org/ovf/envelope/1 http://schemas.dmtf.org/ovf/envelope/1/dsp8023_1.1.0.xsd http://schemas.dmtf.org/ovf/environment/1 ' \
               'http://schemas.dmtf.org/ovf/envelope/1/dsp8027_1.1.0.xsd http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/CIM_ResourceAllocationSettingData http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2.22.0/CIM_ResourceAllocationSettingData.xsd">' \
               '<Link rel="power:powerOff" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/power/action/powerOff"/>' \
               '<Link rel="power:reboot" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/power/action/reboot"/>' \
               '<Link rel="power:reset" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/power/action/reset"/>' \
               '<Link rel="power:shutdown" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/power/action/shutdown"/>' \
               '<Link rel="power:suspend" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/power/action/suspend"/>' \
               '<Link rel="deploy" type="application/vnd.vmware.vcloud.deployVAppParams+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/action/deploy"/>' \
               '<Link rel="undeploy" type="application/vnd.vmware.vcloud.undeployVAppParams+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/action/undeploy"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.vAppNetwork+xml" name="internalbase-net" href="http://162.3.201.10/api/network/16e10581-c3a0-44cb-9e36-9a7432153071"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.vAppNetwork+xml" name="tunnelbearing-net" href="http://162.3.201.10/api/network/15b0d34c-7f46-42e2-9781-a9e276023447"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.controlAccess+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/controlAccess/"/>' \
               '<Link rel="controlAccess" type="application/vnd.vmware.vcloud.controlAccess+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/action/controlAccess"/>' \
               '<Link rel="up" type="application/vnd.vmware.vcloud.vdc+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.vApp+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.owner+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/owner"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/metadata"/>' \
               '<LeaseSettingsSection type="application/vnd.vmware.vcloud.leaseSettingsSection+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/leaseSettingsSection/" ovf:required="false">' \
               '<ovf:Info>Lease settings section</ovf:Info>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.leaseSettingsSection+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/leaseSettingsSection/"/>' \
               '<DeploymentLeaseInSeconds>0</DeploymentLeaseInSeconds>' \
               '<StorageLeaseInSeconds>0</StorageLeaseInSeconds>' \
               '</LeaseSettingsSection>' \
               '<ovf:StartupSection xmlns:vcloud="http://www.vmware.com/vcloud/v1.5" vcloud:href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/startupSection/" vcloud:type="application/vnd.vmware.vcloud.startupSection+xml">' \
               '<ovf:Info>VApp startup section</ovf:Info>' \
               '<ovf:Item ovf:stopDelay="0" ovf:stopAction="powerOff" ovf:startDelay="0" ovf:startAction="powerOn" ovf:order="0" ovf:id="etherpad"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.startupSection+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/startupSection/"/>' \
               '</ovf:StartupSection>' \
               '<ovf:NetworkSection xmlns:vcloud="http://www.vmware.com/vcloud/v1.5" vcloud:href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/networkSection/" vcloud:type="application/vnd.vmware.vcloud.networkSection+xml">' \
               '<ovf:Info>The list of logical networks</ovf:Info>' \
               '<ovf:Network ovf:name="internalbase-net">' \
               '<ovf:Description/>' \
               '</ovf:Network>' \
               '<ovf:Network ovf:name="tunnelbearing-net">' \
               '<ovf:Description/>' \
               '</ovf:Network>' \
               '</ovf:NetworkSection>' \
               '<NetworkConfigSection type="application/vnd.vmware.vcloud.networkConfigSection+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/networkConfigSection/" ovf:required="false">' \
               '<ovf:Info>The configuration parameters for logical networks</ovf:Info>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.networkConfigSection+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/networkConfigSection/"/>' \
               '<NetworkConfig networkName="internalbase-net">' \
               '<Link rel="repair" href="http://162.3.201.10/api/admin/network/16e10581-c3a0-44cb-9e36-9a7432153071/action/reset"/>' \
               '<Description/>' \
               '<Configuration>' \
               '<IpScope>' \
               '<IsInherited>true</IsInherited>' \
               '<Gateway>172.28.0.1</Gateway>' \
               '<Netmask>255.255.240.0</Netmask>' \
               '<IpRanges>' \
               '<IpRange>' \
               '<StartAddress>172.28.0.2</StartAddress>' \
               '<EndAddress>172.28.0.99</EndAddress>' \
               '</IpRange>' \
               '</IpRanges>' \
               '</IpScope>' \
               '<ParentNetwork name="internalbase-net" id="0e4e220d-4cf8-42e0-96a7-665694cc90ef" href="http://162.3.201.10/api/admin/network/0e4e220d-4cf8-42e0-96a7-665694cc90ef"/>' \
               '<FenceMode>bridged</FenceMode>' \
               '<RetainNetInfoAcrossDeployments>false</RetainNetInfoAcrossDeployments>' \
               '</Configuration>' \
               '<IsDeployed>true</IsDeployed>' \
               '</NetworkConfig>' \
               '<NetworkConfig networkName="tunnelbearing-net">' \
               '<Link rel="repair" href="http://162.3.201.10/api/admin/network/15b0d34c-7f46-42e2-9781-a9e276023447/action/reset"/>' \
               '<Description/>' \
               '<Configuration>' \
               '<IpScope>' \
               '<IsInherited>true</IsInherited>' \
               '<Gateway>172.30.16.1</Gateway>' \
               '<Netmask>255.255.240.0</Netmask>' \
               '<IpRanges>' \
               '<IpRange>' \
               '<StartAddress>172.30.16.2</StartAddress>' \
               '<EndAddress>172.30.16.99</EndAddress>' \
               '</IpRange>' \
               '</IpRanges>' \
               '</IpScope>' \
               '<ParentNetwork name="tunnelbearing-net" id="6d7f8b1a-f088-4baa-b5d3-889f43d9b375" href="http://162.3.201.10/api/admin/network/6d7f8b1a-f088-4baa-b5d3-889f43d9b375"/>' \
               '<FenceMode>bridged</FenceMode>' \
               '<RetainNetInfoAcrossDeployments>false</RetainNetInfoAcrossDeployments>' \
               '</Configuration>' \
               '<IsDeployed>true</IsDeployed>' \
               '</NetworkConfig>' \
               '</NetworkConfigSection>' \
               '<Owner type="application/vnd.vmware.vcloud.owner+xml">' \
               '<User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '</Owner>' \
               '<InMaintenanceMode>false</InMaintenanceMode>' \
               '<Children>' \
               '<Vm needsCustomization="false" deployed="true" status="4" name="etherpad" id="urn:vcloud:vm:424ed08c-c811-407d-943a-795e23284e5f" type="application/vnd.vmware.vcloud.vm+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f">' \
               '<Link rel="power:powerOff" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/power/action/powerOff"/>' \
               '<Link rel="power:reboot" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/power/action/reboot"/>' \
               '<Link rel="power:reset" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/power/action/reset"/>' \
               '<Link rel="power:shutdown" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/power/action/shutdown"/>' \
               '<Link rel="power:suspend" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/power/action/suspend"/>' \
               '<Link rel="undeploy" type="application/vnd.vmware.vcloud.undeployVAppParams+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/action/undeploy"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.vm+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/metadata"/>' \
               '<Link rel="screen:thumbnail" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/screen"/>' \
               '<Link rel="screen:acquireTicket" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/screen/action/acquireTicket"/>' \
               '<Link rel="media:insertMedia" type="application/vnd.vmware.vcloud.mediaInsertOrEjectParams+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/media/action/insertMedia"/>' \
               '<Link rel="media:ejectMedia" type="application/vnd.vmware.vcloud.mediaInsertOrEjectParams+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/media/action/ejectMedia"/>' \
               '<Link rel="installVmwareTools" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/action/installVMwareTools"/>' \
               '<Link rel="up" type="application/vnd.vmware.vcloud.vApp+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s"/>' \
               '<ovf:VirtualHardwareSection xmlns:vcloud="http://www.vmware.com/vcloud/v1.5" ovf:transport="" vcloud:href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/" vcloud:type="application/vnd.vmware.vcloud.virtualHardwareSection+xml">' \
               '<ovf:Info>Virtual hardware requirements</ovf:Info>' \
               '<ovf:System>' \
               '<vssd:ElementName>Virtual Hardware Family</vssd:ElementName>' \
               '<vssd:InstanceID>0</vssd:InstanceID>' \
               '<vssd:VirtualSystemIdentifier>etherpad</vssd:VirtualSystemIdentifier>' \
               '<vssd:VirtualSystemType>vmx-10</vssd:VirtualSystemType>' \
               '</ovf:System>' \
               '<ovf:Item>' \
               '<rasd:Address>00:50:56:0c:01:fe</rasd:Address>' \
               '<rasd:AddressOnParent>1</rasd:AddressOnParent>' \
               '<rasd:AutomaticAllocation>true</rasd:AutomaticAllocation>' \
               '<rasd:Connection vcloud:ipAddress="172.28.12.147" vcloud:primaryNetworkConnection="false" vcloud:ipAddressingMode="DHCP">internalbase-net</rasd:Connection>' \
               '<rasd:Description>E1000 ethernet adapter on "internalbase-net"</rasd:Description>' \
               '<rasd:ElementName>Network adapter 1</rasd:ElementName>' \
               '<rasd:InstanceID>1</rasd:InstanceID>' \
               '<rasd:ResourceSubType>E1000</rasd:ResourceSubType>' \
               '<rasd:ResourceType>10</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:Address>00:50:56:0c:01:e3</rasd:Address>' \
               '<rasd:AddressOnParent>0</rasd:AddressOnParent>' \
               '<rasd:AutomaticAllocation>true</rasd:AutomaticAllocation>' \
               '<rasd:Connection vcloud:ipAddress="172.30.16.110" vcloud:primaryNetworkConnection="true" vcloud:ipAddressingMode="DHCP">tunnelbearing-net</rasd:Connection>' \
               '<rasd:Description>E1000 ethernet adapter on "tunnelbearing-net"</rasd:Description>' \
               '<rasd:ElementName>Network adapter 0</rasd:ElementName>' \
               '<rasd:InstanceID>2</rasd:InstanceID>' \
               '<rasd:ResourceSubType>E1000</rasd:ResourceSubType>' \
               '<rasd:ResourceType>10</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:Address>0</rasd:Address>' \
               '<rasd:Description>SCSI Controller</rasd:Description>' \
               '<rasd:ElementName>SCSI Controller 0</rasd:ElementName>' \
               '<rasd:InstanceID>3</rasd:InstanceID>' \
               '<rasd:ResourceSubType>lsilogic</rasd:ResourceSubType>' \
               '<rasd:ResourceType>6</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:AddressOnParent>0</rasd:AddressOnParent>' \
               '<rasd:Description>Hard disk</rasd:Description>' \
               '<rasd:ElementName>Hard disk 1</rasd:ElementName>' \
               '<rasd:HostResource vcloud:capacity="5120" vcloud:busSubType="lsilogic" vcloud:busType="6"/>' \
               '<rasd:InstanceID>2000</rasd:InstanceID>' \
               '<rasd:Parent>3</rasd:Parent>' \
               '<rasd:ResourceType>17</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:AddressOnParent>1</rasd:AddressOnParent>' \
               '<rasd:Description>Hard disk</rasd:Description>' \
               '<rasd:ElementName>Hard disk 2</rasd:ElementName>' \
               '<rasd:HostResource vcloud:capacity="1024" vcloud:busSubType="lsilogic" vcloud:busType="6" vcloud:disk="http://162.3.201.10/api/disk/6d8bc149-0c36-47a1-bdd5-a349c5a49fa3"/>' \
               '<rasd:InstanceID>2001</rasd:InstanceID>' \
               '<rasd:Parent>3</rasd:Parent>' \
               '<rasd:ResourceType>17</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:Address>0</rasd:Address>' \
               '<rasd:Description>IDE Controller</rasd:Description>' \
               '<rasd:ElementName>IDE Controller 0</rasd:ElementName>' \
               '<rasd:InstanceID>4</rasd:InstanceID>' \
               '<rasd:ResourceType>5</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item>' \
               '<rasd:AddressOnParent>0</rasd:AddressOnParent>' \
               '<rasd:AutomaticAllocation>true</rasd:AutomaticAllocation>' \
               '<rasd:Description>CD/DVD Drive</rasd:Description>' \
               '<rasd:ElementName>CD/DVD Drive 1</rasd:ElementName>' \
               '<rasd:HostResource>metadata_%(vm_name)s.iso</rasd:HostResource>' \
               '<rasd:InstanceID>3000</rasd:InstanceID>' \
               '<rasd:Parent>4</rasd:Parent>' \
               '<rasd:ResourceSubType>vmware.cdrom.iso</rasd:ResourceSubType>' \
               '<rasd:ResourceType>15</rasd:ResourceType>' \
               '</ovf:Item>' \
               '<ovf:Item vcloud:href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/cpu" vcloud:type="application/vnd.vmware.vcloud.rasdItem+xml">' \
               '<rasd:AllocationUnits>hertz * 10^6</rasd:AllocationUnits>' \
               '<rasd:Description>Number of Virtual CPUs</rasd:Description>' \
               '<rasd:ElementName>1 virtual CPU(s)</rasd:ElementName>' \
               '<rasd:InstanceID>5</rasd:InstanceID>' \
               '<rasd:Reservation>0</rasd:Reservation>' \
               '<rasd:ResourceType>3</rasd:ResourceType>' \
               '<rasd:VirtualQuantity>1</rasd:VirtualQuantity>' \
               '<rasd:Weight>0</rasd:Weight>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/cpu"/>' \
               '</ovf:Item>' \
               '<ovf:Item vcloud:href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/memory" vcloud:type="application/vnd.vmware.vcloud.rasdItem+xml">' \
               '<rasd:AllocationUnits>byte * 2^20</rasd:AllocationUnits>' \
               '<rasd:Description>Memory Size</rasd:Description>' \
               '<rasd:ElementName>2048 MB of memory</rasd:ElementName>' \
               '<rasd:InstanceID>6</rasd:InstanceID>' \
               '<rasd:Reservation>0</rasd:Reservation>' \
               '<rasd:ResourceType>4</rasd:ResourceType>' \
               '<rasd:VirtualQuantity>2048</rasd:VirtualQuantity>' \
               '<rasd:Weight>0</rasd:Weight>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/memory"/>' \
               '</ovf:Item>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.virtualHardwareSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/cpu"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/cpu"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/memory"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItem+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/memory"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/disks"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/disks"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/media"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/networkCards"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/networkCards"/>' \
               '<Link rel="down" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/serialPorts"/>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.rasdItemsList+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/virtualHardwareSection/serialPorts"/>' \
               '</ovf:VirtualHardwareSection>' \
               '<ovf:OperatingSystemSection xmlns:vcloud="http://www.vmware.com/vcloud/v1.5" ovf:id="101" vcloud:href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/operatingSystemSection/" vcloud:type="application/vnd.vmware.vcloud.operatingSystemSection+xml" vmw:osType="otherLinux64Guest">' \
               '<ovf:Info>Specifies the operating system installed</ovf:Info>' \
               '<ovf:Description>Other Linux (64-bit)</ovf:Description>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.operatingSystemSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/operatingSystemSection/"/>' \
               '</ovf:OperatingSystemSection>' \
               '<NetworkConnectionSection type="application/vnd.vmware.vcloud.networkConnectionSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/networkConnectionSection/" ovf:required="false">' \
               '<ovf:Info>Specifies the available VM network connections</ovf:Info>' \
               '<PrimaryNetworkConnectionIndex>0</PrimaryNetworkConnectionIndex>' \
               '<NetworkConnection network="internalbase-net" needsCustomization="false">' \
               '<NetworkConnectionIndex>1</NetworkConnectionIndex>' \
               '<IpAddress>172.28.12.147</IpAddress>' \
               '<IsConnected>true</IsConnected>' \
               '<MACAddress>00:50:56:0c:01:fe</MACAddress>' \
               '<IpAddressAllocationMode>DHCP</IpAddressAllocationMode>' \
               '</NetworkConnection>' \
               '<NetworkConnection network="tunnelbearing-net" needsCustomization="false">' \
               '<NetworkConnectionIndex>0</NetworkConnectionIndex>' \
               '<IpAddress>172.30.16.110</IpAddress>' \
               '<IsConnected>true</IsConnected>' \
               '<MACAddress>00:50:56:0c:01:e3</MACAddress>' \
               '<IpAddressAllocationMode>DHCP</IpAddressAllocationMode>' \
               '</NetworkConnection>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.networkConnectionSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/networkConnectionSection/"/>' \
               '</NetworkConnectionSection>' \
               '<GuestCustomizationSection type="application/vnd.vmware.vcloud.guestCustomizationSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/guestCustomizationSection/" ovf:required="false">' \
               '<ovf:Info>Specifies Guest OS Customization Settings</ovf:Info>' \
               '<Enabled>true</Enabled>' \
               '<ChangeSid>false</ChangeSid>' \
               '<VirtualMachineId>424ed08c-c811-407d-943a-795e23284e5f</VirtualMachineId>' \
               '<JoinDomainEnabled>false</JoinDomainEnabled>' \
               '<UseOrgSettings>false</UseOrgSettings>' \
               '<AdminPasswordEnabled>true</AdminPasswordEnabled>' \
               '<AdminPasswordAuto>true</AdminPasswordAuto>' \
               '<AdminPassword>U$9eh$!F</AdminPassword>' \
               '<ResetPasswordRequired>false</ResetPasswordRequired>' \
               '<ComputerName>AVirtualMac-001</ComputerName>' \
               '<Link rel="edit" type="application/vnd.vmware.vcloud.guestCustomizationSection+xml" href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/guestCustomizationSection/"/>' \
               '</GuestCustomizationSection>' \
               '<RuntimeInfoSection xmlns:vcloud="http://www.vmware.com/vcloud/v1.5" vcloud:href="http://162.3.201.10/api/vApp/vm-424ed08c-c811-407d-943a-795e23284e5f/runtimeInfoSection" vcloud:type="application/vnd.vmware.vcloud.virtualHardwareSection+xml">' \
               '<ovf:Info>Specifies Runtime info</ovf:Info>' \
               '<VMWareTools version="2147483647"/>' \
               '</RuntimeInfoSection>' \
               '<VAppScopedLocalId>vm</VAppScopedLocalId>' \
               '<ovfenv:Environment xmlns:ns10="http://www.vmware.com/schema/ovfenv" ovfenv:id="" ns10:vCenterId="vm-12109">' \
               '<ovfenv:PlatformSection>' \
               '<ovfenv:Kind>VMware ESXi</ovfenv:Kind>' \
               '<ovfenv:Version>5.5.0</ovfenv:Version>' \
               '<ovfenv:Vendor>VMware, Inc.</ovfenv:Vendor>' \
               '<ovfenv:Locale>en</ovfenv:Locale>' \
               '</ovfenv:PlatformSection>' \
               '<ve:EthernetAdapterSection xmlns:ve="http://www.vmware.com/schema/ovfenv" xmlns="http://schemas.dmtf.org/ovf/environment/1" xmlns:oe="http://schemas.dmtf.org/ovf/environment/1">' \
               '<ve:Adapter ve:mac="00:50:56:0c:01:e3" ve:network="dvs.VCDVStunnelbearing-net-3db1c433-ea67-4a0e-a2fe-9de7f2c027b1" ve:unitNumber="7"/>' \
               '<ve:Adapter ve:mac="00:50:56:0c:01:fe" ve:network="dvs.VCDVSinternalbase-net-46e813ac-39e0-4558-9fcd-745dae894b6f" ve:unitNumber="8"/>' \
               '</ve:EthernetAdapterSection>' \
               '</ovfenv:Environment>' \
               '</Vm>' \
               '</Children>' \
               '</VApp>' % {"vm_id": vm.id, "vm_name": vm.name}

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def get_task(self, request, task_id):
        tm = CloudManager()
        task = tm.query_task(task_id)

        LOG.info("get task, task_id = %s, task_status = %s", task_id, task.status)

        time.sleep(REST_DELAY)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'), ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-04T11:23:50.617+08:00" serviceNamespace="com.vmware.vcloud" operationName="vdcInstantiateVapp" operation="Created Virtual Application server@b1059e53-1fa7-4848-95a6-f214e7df5853(8b0d1e57-29a4-469a-9ffb-b985c9735199)" expiryTime="2016-06-02T11:23:50.617+08:00" endTime="2016-03-04T11:23:54.984+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Owner type="application/vnd.vmware.vcloud.vApp+xml" name="server@b1059e53-1fa7-4848-95a6-f214e7df5853" href="http://162.3.201.10/api/vApp/vapp-8b0d1e57-29a4-469a-9ffb-b985c9735199"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Progress>100</Progress>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task.status}

        return webob.Response(status_int=200, headerlist=header_list, body=body)

    def instantiate_VApp_Template(self, request, vdc_id, vapp_name):
        LOG.info("instantiate_VApp_Template, vdc_id = %s, vapp_name = %s", vdc_id, vapp_name)

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id, vm_id = tm.create_virtual_machine(vapp_name)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.vapp+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<VApp xmlns="http://www.vmware.com/vcloud/v1.5" ovfDescriptorUploaded="true" deployed="false" status="0" name="%(vm_name)s" id="urn:vcloud:vapp:%(vm_id)s" type="application/vnd.vmware.vcloud.vApp+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="down" type="application/vnd.vmware.vcloud.vAppNetwork+xml" name="tunnelbearing-net" href="http://162.3.201.10/api/network/506102c5-ca6e-412c-9859-346dbdc2f7e8"/>' \
               '    <Link rel="down" type="application/vnd.vmware.vcloud.vAppNetwork+xml" name="internalbase-net" href="http://162.3.201.10/api/network/814cb1a9-e809-4d2c-a897-b42abae9c6fd"/>' \
               '	<Link rel="down" type="application/vnd.vmware.vcloud.controlAccess+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/controlAccess/"/>' \
               '	<Link rel="up" type="application/vnd.vmware.vcloud.vdc+xml" href="http://162.3.201.10/api/vdc/61800c8d-89a4-4320-bbef-f57806b7064a"/>' \
               '	<Link rel="down" type="application/vnd.vmware.vcloud.owner+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/owner"/>' \
               '	<Link rel="down" type="application/vnd.vmware.vcloud.metadata+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/metadata"/>' \
               '	<Link rel="ovf" type="text/xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/ovf"/>' \
               '	<Link rel="down" type="application/vnd.vmware.vcloud.productSections+xml" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s/productSections/"/>' \
               '	<Tasks>' \
               '	    <Task status="running" startTime="2016-03-04T11:23:50.617+08:00" serviceNamespace="com.vmware.vcloud" operationName="vdcInstantiateVapp" operation="Creating Virtual Application %(vm_name)s(%(vm_id)s)" expiryTime="2016-06-02T11:23:50.617+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s">' \
               '		    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '		    <Owner type="application/vnd.vmware.vcloud.vApp+xml" name="%(vm_name)s" href="http://162.3.201.10/api/vApp/vapp-%(vm_id)s"/>' \
               '		    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '		    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '		    <Progress>1</Progress>' \
               '		    <Details/>' \
               '	    </Task>' \
               '	</Tasks>' \
               '	<DateCreated>2016-03-04T11:23:48.684+08:00</DateCreated>' \
               '	<Owner type="application/vnd.vmware.vcloud.owner+xml">' \
               '	    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '	</Owner>' \
               '	<InMaintenanceMode>false</InMaintenanceMode>' \
               '</VApp>' % {"task_id": task_id, "vm_name": vapp_name, "vm_id": vm_id}

        return webob.Response(status_int=201, headerlist=header_list, body=body)

    def networkConnectionSection(self, request, vapp_id):
        LOG.info("network Connection Section, vapp_id = %s" % vapp_id)

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id, vm_id = tm.update_virtual_machine(vapp_id)
        task_status = "running"

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-06T16:33:57.959+08:00" serviceNamespace="com.vmware.vcloud" operationName="vappUpdateVm" operation="Updating Virtual Machine etherpad(d425f29a-c951-4b5e-a605-ee623bd2d33e)" expiryTime="2016-06-04T16:33:57.959+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '    <Owner type="application/vnd.vmware.vcloud.vm+xml" name="etherpad" href="http://162.3.201.10/api/vApp/vm-d425f29a-c951-4b5e-a605-ee623bd2d33e"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task_status}
        return webob.Response(status_int=202, headerlist=header_list, body=body)

    def virtualHardwareSection(self, request, vapp_id, operation):
        LOG.info("virtual Hardware Section, vapp_id = %s, operation = %s" % (vapp_id, operation))

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id, vm_id = tm.update_virtual_machine(vapp_id)
        task_status = "running"

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-06T16:33:57.959+08:00" serviceNamespace="com.vmware.vcloud" operationName="vappUpdateVm" operation="Updating Virtual Machine etherpad(d425f29a-c951-4b5e-a605-ee623bd2d33e)" expiryTime="2016-06-04T16:33:57.959+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '    <Owner type="application/vnd.vmware.vcloud.vm+xml" name="etherpad" href="http://162.3.201.10/api/vApp/vm-d425f29a-c951-4b5e-a605-ee623bd2d33e"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task_status}
        return webob.Response(status_int=202, headerlist=header_list, body=body)

    def vapp_power_action(self, request, vapp_id, operation):
        LOG.info("vapp power action, vapp_id = %s, operation = %s" % (vapp_id, operation))

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id = tm.power_on_virtual_machine(vapp_id)
        task_status = "running"

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-06T16:33:57.959+08:00" serviceNamespace="com.vmware.vcloud" operationName="vappUpdateVm" operation="Updating Virtual Machine etherpad(d425f29a-c951-4b5e-a605-ee623bd2d33e)" expiryTime="2016-06-04T16:33:57.959+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '    <Owner type="application/vnd.vmware.vcloud.vm+xml" name="etherpad" href="http://162.3.201.10/api/vApp/vm-d425f29a-c951-4b5e-a605-ee623bd2d33e"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task_status}
        return webob.Response(status_int=202, headerlist=header_list, body=body)

    def vapp_media_action(self, request, vapp_id, operation):
        LOG.info("vapp media action, vapp_id = %s, operation = %s" % (vapp_id, operation))

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id, vm_id = tm.update_virtual_machine(vapp_id)
        task_status = "running"

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-06T16:33:57.959+08:00" serviceNamespace="com.vmware.vcloud" operationName="vappUpdateVm" operation="Updating Virtual Machine etherpad(d425f29a-c951-4b5e-a605-ee623bd2d33e)" expiryTime="2016-06-04T16:33:57.959+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '    <Owner type="application/vnd.vmware.vcloud.vm+xml" name="etherpad" href="http://162.3.201.10/api/vApp/vm-d425f29a-c951-4b5e-a605-ee623bd2d33e"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task_status}
        return webob.Response(status_int=202, headerlist=header_list, body=body)

    def vapp_action(self, request, vapp_id, operation):
        LOG.info("vapp action, vapp_id = %s, operation = %s" % (vapp_id, operation))

        time.sleep(REST_DELAY)

        tm = CloudManager()
        task_id = tm.update_virtual_machine(vapp_id)
        task_status = "running"

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.task+xml;version=5.5'),
                       ('Vary', 'Accept-Encoding')]

        body = '<?xml version="1.0" encoding="UTF-8"?>' \
               '<Task xmlns="http://www.vmware.com/vcloud/v1.5" status="%(task_status)s" startTime="2016-03-06T16:33:57.959+08:00" serviceNamespace="com.vmware.vcloud" operationName="vappUpdateVm" operation="Updating Virtual Machine etherpad(d425f29a-c951-4b5e-a605-ee623bd2d33e)" expiryTime="2016-06-04T16:33:57.959+08:00" cancelRequested="false" name="task" id="urn:vcloud:task:%(task_id)s" type="application/vnd.vmware.vcloud.task+xml" href="http://162.3.201.10/api/task/%(task_id)s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.3.201.10/api/v1.5/schema/master.xsd">' \
               '    <Link rel="task:cancel" href="http://162.3.201.10/api/task/%(task_id)s/action/cancel"/>' \
               '    <Owner type="application/vnd.vmware.vcloud.vm+xml" name="etherpad" href="http://162.3.201.10/api/vApp/vm-d425f29a-c951-4b5e-a605-ee623bd2d33e"/>' \
               '    <User type="application/vnd.vmware.admin.user+xml" name="huawei" href="http://162.3.201.10/api/admin/user/9ba4f68a-aac4-4bd8-b563-91b6728e94d0"/>' \
               '    <Organization type="application/vnd.vmware.vcloud.org+xml" name="env130" href="http://162.3.201.10/api/org/379844e7-76e8-4966-821d-a73c083ea9db"/>' \
               '    <Details/>' \
               '</Task>' % {"task_id": task_id,
                            "task_status": task_status}
        return webob.Response(status_int=202, headerlist=header_list, body=body)

    def paged_query_vapp(self, request, page, pageSize):
        LOG.info("paged query vapp, page = %s, pageSize = %s" % (page, pageSize))

        time.sleep(REST_DELAY)

        tm = CloudManager()
        total, next_page, vm_list = tm.paged_query_virtual_machines(page=page, pageSize=pageSize)

        header_list = [('Content-Type',
                        'application/vnd.vmware.vcloud.query.records+xml;version=1.5'),
                       ('Vary', 'Accept-Encoding')]

        vm_page_body = ''
        if vm_list:
            for vm in vm_list:
                vm_page_body += '<VAppRecord vdcName="vdc3" vdc="https://162.4.110.131/api/vdc/3fa5cdd5-8c3f-449f-a6bf-99202a548677" status="%(vm_status)s" ' \
                                'ownerName="vdc3-user" name="%(vm_name)s" isPublic="false" isInMaintenanceMode="false" isExpired="false" isEnabled="true" ' \
                                'isDeployed="true" isBusy="false" creationDate="2016-02-18T14:32:39.048+08:00" href="https://162.4.110.131/api/vApp/vapp-%(vm_id)s" ' \
                                'cpuAllocationMhz="12" cpuAllocationInMhz="12000" ' \
                                'task="https://162.4.110.131/api/task/ca757207-1b51-43ea-882d-4862940d8180" ' \
                                'isAutoDeleteNotified="false" numberOfVMs="1" autoUndeployDate="2017-03-21T17:09:54.518+08:00" ' \
                                'isAutoUndeployNotified="false" taskStatusName="vappDeploy" isVdcEnabled="true" ' \
                                'honorBootOrder="true" pvdcHighestSupportedHardwareVersion="10" ' \
                                'lowestHardwareVersionInVApp="8" taskStatus="success" storageKB="209715200" taskDetails=" " numberOfCpus="12" memoryAllocationMB="16384"/>' \
                                % {"vm_name": vm.name, "vm_status": vm.status, "vm_id": vm.id}

        body = '<?xml version="1.0" encoding="UTF-8"?> ' \
               '<QueryResultRecords xmlns="http://www.vmware.com/vcloud/v1.5" total="%(total)s" pageSize="%(pageSize)s" page="%(page)s" ' \
               'name="vApp" type="application/vnd.vmware.vcloud.query.records+xml" ' \
               'href="https://162.4.110.131/api/query?type=vApp&amp;page=%(page)s&amp;pageSize=%(pageSize)s&amp;format=records" ' \
               'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
               'xsi:schemaLocation="http://www.vmware.com/vcloud/v1.5 http://162.4.110.131/api/v1.5/schema/master.xsd">' \
               % {"total": total, "pageSize": pageSize, "page": page}

        if next_page > 0:
            body += '<Link rel="nextPage" type="application/vnd.vmware.vcloud.query.records+xml" href="https://162.4.110.131/api/query?type=vApp&amp;page=%(next)s&amp;pageSize=%(pageSize)s&amp;format=records"/>' \
                    '<Link rel="lastPage" type="application/vnd.vmware.vcloud.query.records+xml" href="https://162.4.110.131/api/query?type=vApp&amp;page=%(total)s&amp;pageSize=%(pageSize)s&amp;format=records"/>' % {"next": next, "pageSize": pageSize}

        body += '<Link rel="alternate" type="application/vnd.vmware.vcloud.query.references+xml" href="https://162.4.110.131/api/query?type=vApp&amp;page=1&amp;pageSize=%(pageSize)s&amp;format=references"/>' \
                '<Link rel="alternate" type="application/vnd.vmware.vcloud.query.idrecords+xml" href="https://162.4.110.131/api/query?type=vApp&amp;page=1&amp;pageSize=%(pageSize)s&amp;format=idrecords"/>' % {"pageSize": pageSize}

        body += vm_page_body
        body += '</QueryResultRecords>'

        return webob.Response(status_int=200, headerlist=header_list, body=body)


def create_router(mapper):
    controller = VcloudController()
    mapper.connect('/api/sessions',
                   controller=controller,
                   action='get_sessions',
                   conditions=dict(method=['POST']))
    mapper.connect('/api/org/{org_id}',
                   controller=controller,
                   action='get_org',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/vdc/{vdc_id}',
                   controller=controller,
                   action='get_vdc',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/catalog/{catalog_id}',
                   controller=controller,
                   action='get_catalog',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/catalogItem/{catalogItem_id}',
                   controller=controller,
                   action='get_catalog_item',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/vdc/{vdc_id}/action/instantiateVAppTemplate/{vapp_name}',
                   controller=controller,
                   action='instantiate_VApp_Template',
                   conditions=dict(method=['POST']))
    mapper.connect('/api/task/{task_id}',
                   controller=controller,
                   action='get_task',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/vApp/{vapp_id}',
                   controller=controller,
                   action='get_vapp',
                   conditions=dict(method=['GET']))
    mapper.connect('/api/vApp/{vapp_id}/networkConnectionSection/',
                   controller=controller,
                   action='networkConnectionSection',
                   conditions=dict(method=['PUT']))
    mapper.connect('/api/vApp/{vapp_id}/virtualHardwareSection/{operation}',
                   controller=controller,
                   action='virtualHardwareSection',
                   conditions=dict(method=['PUT']))
    mapper.connect('/api/vApp/{vapp_id}/power/action/{operation}',
                   controller=controller,
                   action='vapp_power_action',
                   conditions=dict(method=['PUT']))
    mapper.connect('/api/vApp/{vapp_id}/media/action/{operation}',
                   controller=controller,
                   action='vapp_media_action',
                   conditions=dict(method=['PUT']))
    mapper.connect('/api/vApp/{vapp_id}/action/{operation}',
                   controller=controller,
                   action='vapp_action',
                   conditions=dict(method=['POST']))
    mapper.connect('/api/query?type=vApp&page={page}&pageSize={pageSize}&format=records',
                   controller=controller,
                   action='paged_query_vapp',
                   conditions=dict(method=['POST']))
