# Modifying Global Scope

enemies = 1

"""
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside funciton: {enemies}") 

instead use the below function
"""
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside funciton: {enemies}")    
