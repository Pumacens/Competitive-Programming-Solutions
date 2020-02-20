def zombie_shootout(zombies, distance, ammo):
    killed_zombies = 0
    
    while True:
        killed_zombies += 1
        ammo -= 1
        distance -= 0.5
        
        if killed_zombies == zombies:
            return f'You shot all {killed_zombies} zombies.'
            
        if distance == 0:
            return f"You shot {killed_zombies} zombies before being eaten: overwhelmed."
        
        if ammo == 0:
            return f"You shot {killed_zombies} zombies before being eaten: ran out of ammo."
            

# def zombie_shootout(zombies, distance, ammo, shot=0):
    
#     if not zombies:
#         return f'You shot all {shot} zombies.'
    
#     if distance <= 0:
#         return f'You shot {shot} zombies before being eaten: overwhelmed.'
    
#     if not ammo:
#         return f'You shot {shot} zombies before being eaten: ran out of ammo.'
    
#     return zombie_shootout(zombies - 1, distance - 0.5, ammo - 1, shot + 1)


# def zombie_shootout(z, r, a):
#     s = min(r*2, a)
#     return f"You shot all {z} zombies." if s>=z else f"You shot {s} zombies before being eaten: { 'overwhelmed' if s==2*r else 'ran out of ammo' }."