from requests import post

print(post('http://localhost:5000/api/jobs').json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'test1'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'job': 'etst3',
                 'team_leader': 1,
                 'work_size': 15,
                 'is_finished': False,
                 'collaborators': '4,6'}).json())
