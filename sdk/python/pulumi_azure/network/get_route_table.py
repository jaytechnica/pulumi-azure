# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetRouteTableResult(object):
    """
    A collection of values returned by getRouteTable.
    """
    def __init__(__self__, location=None, routes=None, subnets=None, tags=None):
        if not location:
            raise TypeError('Missing required argument location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected argument location to be a basestring')
        __self__.location = location
        """
        The Azure Region in which the Route Table exists.
        """
        if not routes:
            raise TypeError('Missing required argument routes')
        elif not isinstance(routes, list):
            raise TypeError('Expected argument routes to be a list')
        __self__.routes = routes
        """
        One or more `route` blocks as documented below.
        """
        if not subnets:
            raise TypeError('Missing required argument subnets')
        elif not isinstance(subnets, list):
            raise TypeError('Expected argument subnets to be a list')
        __self__.subnets = subnets
        """
        The collection of Subnets associated with this route table.
        """
        if not tags:
            raise TypeError('Missing required argument tags')
        elif not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags assigned to the Route Table.
        """

def get_route_table(name=None, resource_group_name=None):
    """
    Gets information about a Route Table
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = pulumi.runtime.invoke('azure:network/getRouteTable:getRouteTable', __args__)

    return GetRouteTableResult(
        location=__ret__['location'],
        routes=__ret__['routes'],
        subnets=__ret__['subnets'],
        tags=__ret__['tags'])