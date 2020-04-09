def conference_picker(cities_visited, cities_offered):
    for conference in cities_offered:
        if conference not in cities_visited:
            return conference
            
    return 'No worthwhile conferences this year!'        
    


# def conference_picker(visited, offered):
#     visited = set(visited)
#     return next((city for city in offered if city not in visited),
#                 'No worthwhile conferences this year!')