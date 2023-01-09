# pypractices

The purpose of this repo is to demonstrate several good practices for a new Python project in one place.

## SQLAlchemy

### Mapping

There are three specializations of the mapper registry to map SQLAlchemy tables: declarative base, declarative decorator, and imperative. The declarative approach can often scale better because when you describe the desired end state, SQLAlchemy takes on the responsibility of mapping objects. I don't use the decorator approach because I personally find that I almost always need to have a parent class for some shared logic anyway, thus I prefer the declarative base approach.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

### Relationships and References

Given three tables with one to many semantics in three different modules, having typings on your columns becomes more difficult. You need to prevent cyclic imports as well as let SQLAlchemy know about the tables in an order where it won't get confused by tables it doesn't know about yet.

*company.py*
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    employees = relationship()
```

*employee.py*
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

*address.py*
```python
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

## Packaging

### History

Due to backwards compatibility and a long history, Python is full of options for packaging, and this can be quite confusing. For a long time, you could run a setup.py file and it would perform various build or install actions. Potentially it might also fetch dependencies, but all of this was non-standard, and executing arbitrary code as part of a build system can be problematic. Over time, much of the logic was moved out to an INI-format file called setup.cfg, and pip became the defacto tool for fetching dependencies. It could output a requirements.txt format of dependencies or install the dependencies listed therein.

pyproject.toml allows for various build systems to evolve around its standard format, but one of the most commonly used ones is Poetry. It manages dependencies and building, as well as creating a virtual environment. Poetry is able to replace the old setup.py and 

### Hosting Your Own Index

PEP 503 and 

## Scripts

### Console Scripts

These can be run from anywhere, and their parent directory is added to the search path.

### Run Package or Module as Script

`python -m foo.bar` looks for `__main__.py` in that package and runs it. You can also run a module this way.

This works for the current directory and any directories already registered on the search path by searching `sys.path` for the named module and executing its contents as the `__main__` module after adding the current directory to the start of `sys.path`.

## Search Path

### Imports

When importing module `spam`, the interpreter searches for it in this order:

1. **built-in** modules listed in `sys.builtin_module_names`
2. files named `spam.py` in directories listed by `sys.path`, which is initialized from
   1. the **directory of the input script** (or current dir if no file specified)
   2. **PYTHONPATH**, if set. This is often used for directories of custom libraries or zipfiles of pure Python modules in source or compiled form. It uses the os.pathsep delimiter (colons on Unix and semicolons on Windows)
   3. **PYTHONHOME**, which is always added to PYTHONPATH and contains the standard library. It often looks like `/usr/local/lib/python3.10`.
3. Install-dependent locations, such as site-packages.

### PyCharm

By default, **run and test configurations** add the *content root* and *sources root* to the search path via setting the PYTHONPATH. You can change this by unchecking the last two checkboxes of a run configuration in the Environment section of the edit screen.

Special folder markings include:

- **Content root**: This is all the files making up your project as it's the top level folder. It's by default going to all be indexed and parsed unless another designation is added.
- **Source roots**: These are the source files and resources. PyCharm uses the source roots as the starting point for resolving imports. This is helpful if your source lives under an src folder.
- **Excluded roots**: Ignored folders to exclude from indexing, searching, parsing, watching, etc.
- **Test sources roots**: Code for tests.
- **Resource roots**: Places for resource files. This enables PyCharm to recognize that things like stylesheets or images can be referenced relative to this folder.
- **Template roots**: Contains template files for web projects (e.g. Jinja2 or Mako).