def setup(app):
    app.connect('autodoc-process-docstring', update_docstring)

def update_docstring(app, what, name, obj, options, lines):
    if what == 'class':
        idx = 1
    else:
        idx = 2

    path = name.split(".")

    module_paths = path[:-idx]
    module_path = ".".join(module_paths)

    class_name = path[-idx]
    for i, line in enumerate(lines):
        lines[i] = line\
                    .replace("{class_name}", class_name)\
                    .replace("{module_path}", module_path)

        for idx, p in enumerate(module_paths):
            mp = ".".join(module_paths[:-idx])
            lines[i] = lines[i].replace("{module_path[-%d]}" % idx, mp)