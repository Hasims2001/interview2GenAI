employees = [
{"name": "John", "skills": ["Python", "Database"], "current_project": None},
{"name": "Emma", "skills": ["Java", "Testing"], "current_project": None},
{"name": "Kelly", "skills": ["Python", "Java"], "current_project": None},
]

projects = [ {"name": "Project A", "required_skills": ["Python", "Database"]},
{"name": "Project B", "required_skills": ["Java", "Testing"]},
{"name": "Project C", "required_skills": ["Python", "Java"]},
]

def allocate_projects(emp, project):
    allocated = []
    for item in project:
        req = item['required_skills']
        temp = {}
        for single in emp:
            skill = single['skills']
            if(single['current_project'] == None and req == skill):
                temp.update({'employee': single['name'], 'project': item['name']})
                single['current_project'] = item['name']
                break
        allocated.append(temp)
    return allocated


print(allocate_projects(employees, projects))