import os

structure = {
    'mood-analyzer': [
        'app.py',
        'config.py',
        'requirements.txt',
        '.env',
        ('templates', ['index.html']),
        ('static', ['style.css', 'script.js'])
    ]
}

def create_project(base, structure):
    for item in structure:
        if isinstance(item, tuple):
            dir_name, files = item
            path = os.path.join(base, dir_name)
            os.makedirs(path, exist_ok=True)
            for file in files:
                open(os.path.join(path, file), 'w').close()
        else:
            open(os.path.join(base, item), 'w').close()

create_project('.', structure['mood-analyzer'])
print("Project structure created successfully!")