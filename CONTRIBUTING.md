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
- Tables **must** include UUIDs. The UUIDs **must** be named `<table_name>_uuid`.
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