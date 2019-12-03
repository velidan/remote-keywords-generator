import random
from api.services.resources.user_agents import user_agents_list

def getRandomAgent():
    max_index = len(user_agents_list) - 1
    return user_agents_list[random.randint(0, max_index)]