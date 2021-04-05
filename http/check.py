from requests import post, delete

# Пустой запрос


print(post('http://localhost:5000/api/jobs').json())

# Недостаток данныхх
print(post('http://localhost:5000/api/jobs',
           json={'job': 'test1'}).json())

# Рабочий запрос
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'job': 'etst4',
                 'team_leader': 4,
                 'work_size': 45,
                 'is_finished': True,
                 'collaborators': '3,1'}).json())

# Повторяющийся id
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'job': 'etst3',
                 'team_leader': 1,
                 'work_size': 15,
                 'is_finished': False,
                 'collaborators': '4,6'}).json())

print(delete('http://localhost:5000/api/jobs/1').json())