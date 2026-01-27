person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


skills_set = set(person.get('skills', []))

if skills_set == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set) and 'React' not in skills_set:
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print('He is a fullstack developer')
else:
    print('unknown title')