# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetSharedImageVersionResult:
    """
    A collection of values returned by getSharedImageVersion.
    """
    def __init__(__self__, exclude_from_latest=None, gallery_name=None, id=None, image_name=None, location=None, managed_image_id=None, name=None, resource_group_name=None, tags=None, target_regions=None):
        if exclude_from_latest and not isinstance(exclude_from_latest, bool):
            raise TypeError("Expected argument 'exclude_from_latest' to be a bool")
        __self__.exclude_from_latest = exclude_from_latest
        """
        Is this Image Version excluded from the `latest` filter?
        """
        if gallery_name and not isinstance(gallery_name, str):
            raise TypeError("Expected argument 'gallery_name' to be a str")
        __self__.gallery_name = gallery_name
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if image_name and not isinstance(image_name, str):
            raise TypeError("Expected argument 'image_name' to be a str")
        __self__.image_name = image_name
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        __self__.location = location
        """
        The supported Azure location where the Shared Image Gallery exists.
        """
        if managed_image_id and not isinstance(managed_image_id, str):
            raise TypeError("Expected argument 'managed_image_id' to be a str")
        __self__.managed_image_id = managed_image_id
        """
        The ID of the Managed Image which was the source of this Shared Image Version.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The Azure Region in which this Image Version exists.
        """
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        __self__.resource_group_name = resource_group_name
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the Shared Image.
        """
        if target_regions and not isinstance(target_regions, list):
            raise TypeError("Expected argument 'target_regions' to be a list")
        __self__.target_regions = target_regions
        """
        One or more `target_region` blocks as documented below.
        """
class AwaitableGetSharedImageVersionResult(GetSharedImageVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSharedImageVersionResult(
            exclude_from_latest=self.exclude_from_latest,
            gallery_name=self.gallery_name,
            id=self.id,
            image_name=self.image_name,
            location=self.location,
            managed_image_id=self.managed_image_id,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags,
            target_regions=self.target_regions)

def get_shared_image_version(gallery_name=None,image_name=None,name=None,resource_group_name=None,opts=None):
    """
    Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.




    :param str gallery_name: The name of the Shared Image in which the Shared Image exists.
    :param str image_name: The name of the Shared Image in which this Version exists.
    :param str name: The name of the Image Version.
    :param str resource_group_name: The name of the Resource Group in which the Shared Image Gallery exists.
    """
    __args__ = dict()


    __args__['galleryName'] = gallery_name
    __args__['imageName'] = image_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:compute/getSharedImageVersion:getSharedImageVersion', __args__, opts=opts).value

    return AwaitableGetSharedImageVersionResult(
        exclude_from_latest=__ret__.get('excludeFromLatest'),
        gallery_name=__ret__.get('galleryName'),
        id=__ret__.get('id'),
        image_name=__ret__.get('imageName'),
        location=__ret__.get('location'),
        managed_image_id=__ret__.get('managedImageId'),
        name=__ret__.get('name'),
        resource_group_name=__ret__.get('resourceGroupName'),
        tags=__ret__.get('tags'),
        target_regions=__ret__.get('targetRegions'))
