DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # Con list comprehensions
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    # Con high order functions
    all_python_devs_1 = list(
        filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_2 = list(
        map(lambda worker: worker['name'], all_python_devs_1))

    all_platzi_workers_1 = list(
        filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_2 = list(
        map(lambda worker: worker['name'], all_platzi_workers_1))

    print(adults)
    print(old_people)
    print(all_python_devs_1)
    print(all_python_devs_2)
    print(all_platzi_workers_1)
    print(all_platzi_workers_2)


if __name__ == '__main__':
    run()
