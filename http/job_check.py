from requests import post, delete, put, get

print(get('http://localhost:5000/api/v2/jobs').json())

print(get('http://localhost:5000/api/v2/jobs/1').json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'id': 3,
                 'team_leader': 2,
                 'job': 'test',
                 'work_size': 14,
                 'collaborators': '3',
                 'is_finished': False
                 }).json())

print(post('http://localhost:5000/api/v2/jobs',
           json={'id': 3}).json())

print(post('http://localhost:5000/api/v2/jobs').json())

print(get('http://localhost:5000/api/v2/jobs/3').json())

print(put('http://localhost:5000/api/v2/jobs/3', json={'team_leader': 2,
                                                       'job': 'test1',
                                                       'work_size': 15,
                                                       'collaborators': '3',
                                                       'is_finished': True
                                                       }).json())

print(put('http://localhost:5000/api/v2/jobs/3', json={'team_leader': 2,
                                                       'job': 'test1',
                                                       'collaborators': '3',
                                                       'is_finished': True
                                                       }).json())

print(get('http://localhost:5000/api/jobs/3').json())

print(delete('http://localhost:5000/api/jobs/3').json())

print(delete('http://localhost:5000/api/jobs/5').json())

print(get('http://localhost:5000/api/jobs/4').json())
