# lib/db/schema.sql

This SQL file defines the database schema for the application.

### Tables Defined:
- `authors`: Represents authors with id and name.
- `magazines`: Represents magazines with id, name, and category.
- `articles`: Represents articles linking authors and magazines.

### Relationships:
- One-to-many: Author → Articles
- One-to-many: Magazine → Articles
