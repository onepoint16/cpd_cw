import boto3



def create_topic(name):
    """
    Creates a notification topic.

    :param name: The name of the topic to create.
    :return: The newly created topic.
    """
    sns = boto3.resource("sns")
    topic = sns.create_topic(Name=name)
    return topic
    
name = "cwSNSTopicS2003045"
create_topic(name)