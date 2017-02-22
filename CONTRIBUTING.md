Introduction
------------
This document adheres to the specifications outlined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

Source Control
--------------
### Commit Messages
- Issue IDs **should** be included.
```
# YES
git commit --message "PROJECT-1: foo"

# No
git commit --message "foo"
```

Database
--------
- The timezone **must** be "UTC".
- In general, lowercase_delimited_by_underscores **should** be used.
- Tables **must** be named with the plural form of their entity.
- Tables describing one-to-many relationships **should** be named `<parent_table>_<child_table>`.
- Tables **must** have primary keys.
- Primary and foreign keys **must** be named `<table_name>_id`.
```
-- YES
CREATE TABLE parents (
    parents_id  serial              PRIMARY KEY,
    children_id int     NOT NULL    REFERENCES children (children_id)
);
```
- Primary keys **should** be surrogate keys.
```
-- YES
CREATE TABLE users (
    users_id        serial                  PRIMARY KEY,
    email_address   varchar(64) NOT NULL    UNIQUE
);

-- No
CREATE TABLE users (
    email_address   varchar(64)             PRIMARY KEY
);
```
- Tables **must** include UUIDs.
- The UUIDs **must** be named `<table_name>_uuid`.
```
-- YES
CREATE TABLE users (
    users_id        serial              PRIMARY KEY,
    users_uuid      uuid    NOT NULL    DEFAULT uuid_generate_v1mc()    UNIQUE,
);
```
- Tables **must** include metadata fields.
```
-- YES
CREATE TABLE users (
    users_id        serial                                  PRIMARY KEY,
    email_address   varchar(64)                 NOT NULL    UNIQUE
    created_at      timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    created_by      int                         NOT NULL,
    updated_at      timestamp with time zone,
    updated_by      int
);
```
- Hungarian notation **must not** be used.
```
-- YES
CREATE TABLE foo (
    created_at      timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP
);

-- No
CREATE TABLE foo (
    created_date    timestamp with time zone    NOT NULL    DEFAULT CURRENT_TIMESTAMP
);
```
- Column constraints **should** trend towards being more restrictive.
- Data type constraints **should** trend towards being more relaxed.
- Datetime (data types that store both date and time) columns **must** include the time zone.
- Database schema changes **should** be propagated to the corresponding application views.

Python
------
### Architecture
This service implements a five-tier architecture.
- At the API tier, *Resources* provide an interface for inbound client requests. Resources are purely for orchestrating work between the underlying Services, Repositories, Models, and Views. In this sense, they are comparable to Controllers in the classical MVC definition.
- At the services tier, *Services* house the primary business logic functions.
- At the data tier, *Repositories* enable Services to perform primitive CRUD operations. A Service may bind to 0 or more Repositories.
- At the domain tier, *Models* are how Repositories represent database entities and are the system's fundamental objects.
- At the presentation tier, *Views* "marshall" or serialize Models so Resources can respond to clients.

### General
- Documentation **must** adhere to the [NumPy / SciPy specifications](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).
- Packages **should** have `__all__` indices in their `__init__.py`.
- `__all__` indices **should** be sorted alphabetically.
- Modules **should not** have `__all__` indices.
- Modules **must** be named with an object type suffix. An exception is with Models. Model modules **must not** be named with an object type suffix.
```
# YES
/foos
    - eggs_foo.py
    - ham_foo.py

/models
    - eggs.py
    - ham.py

# No
/foos
    - eggs.py
    - ham.py

/models
    - eggs_model.py
    - ham_model.py
```
- Package base classes **must** be named with a "Base" prefix.
```
# YES
class BaseFoo:
    pass

# No
class Foo:
    pass
```
- Classes **must** follow the same naming conventions as modules.
- Classes **should** implement `__repr__()` methods.
- Methods intended for subclassing (i.e. stub methods) **could** be named `do_<method_name>()`.
- Functions or methods intended for facilitating testing **could** be named `help_<function_or_method_name>()`.
- Logging **should** be done in the Controllers.

### Models
- Models **should not** have docstrings.
- Models describing one-to-many relationships **should not** be named `<Parent><Child>`.
```
# YES
class Child:
    pass

# No
class ParentChild:
    pass
```