def get_vpc_id_by_node_obj(aws_obj, instances):
    """
    This function getting vpc id by randomly selecting instances out of user aws deployment

    Args:
        aws_obj (obj): AWS() object
        instances (dict): cluster ec2 instances objects

    Returns:
        str: vpc_id: The vpc id

    """

    instance_id = random.choice(list(instances.keys()))
    vpc_id = aws_obj.get_vpc_id_by_instance_id(instance_id)

    return vpc_id 


""" for more information: https://www.programcreek.com/python/?CodeExample=get+vpc+id """