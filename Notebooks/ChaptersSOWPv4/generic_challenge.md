### Coding Challenge: Generic Library Management System

#### Scenario
You are tasked with creating a generic library management system for a public library.
The system should be able to handle different types of media, such as books, magazines, and DVDs.
Each media type will have its own specific attributes, but the system should be able to manage them in a generic way.

#### Requirements
1. **Generic Repository**: Create a generic repository class that can store and manage media items of any type.
    - The repository should have methods to add items, retrieve all items, and find items based on a condition.
    - Use Python's `typing` module to define a generic repository class.
    - The repository should store media items in a list.
    - The `find` method should accept a lambda function as a condition to filter media items.
    - The repository should be able to store media items of different types (e.g., books, magazines, DVDs).
2. **Generic Service**: Create a generic service class that uses the repository to perform operations on the media items.
    - The service class should have methods to add items, retrieve all items, and find items based on a condition.
    - Use Python's `typing` module to define a generic service class.
    - The service class should use the generic repository to store and manage media items.
3. **Media Classes**: Define specific media classes for books, magazines, and DVDs, each with their own attributes.
    - Each media class should have at least three attributes.
    - The media classes should be used to create instances of media items.
4. **Type Safety**: Use Python's `typing` module to ensure type safety throughout the system.
    - Use `TypeVar` and `Generic` to define generic classes.
    - Use type hints for method arguments and return types.
5. **Class Diagram**: Using mermaid create a class diagram showing the relationships between the repository, service,
and media classes.
    - Use UML notation to represent the classes and their relationships.
    - Include attributes and methods in the class diagram.
    - Indicate the generic nature of the repository and service classes.

#### Constraints
1. **TypeVar and Generic**: Use `TypeVar` and `Generic` from the `typing` module to create the generic repository and service classes.
2. **Attributes**: Each media class must have at least three attributes.
3. **Condition Function**: The `find` method should accept a lambda function as a condition to filter media items.
4. **No External Libraries**: Do not use any external libraries other than Python's standard library.

#### Example Media Classes
- **Book**: Attributes - `title` type string, `author` type string, `isbn` type int (as a placeholder)
  - Example: "1984" by George Orwell (ISBN: 1234567890)
  - Example: "The Great Gatsby" by F. Scott Fitzgerald (ISBN: 9876543210)
- **Magazine**: Attributes - `title` type string, `issue` type date (formatted as yyyy-mm-dd), `publisher` type string 
  - Example: "Tech Today" (Issue: "2023-09-01") by Tech Publishers
  - Example: "Fashion Weekly" (Issue: "2023-08-02") by Style Inc.
- **DVD**: Attributes - `title` type string, `director` type string, `duration` type integer (in minutes)
  - Example: "Inception" by Christopher Nolan (Duration: 148 minutes)
  - Example: "The Matrix" by The Wachowskis (Duration: 136 minutes)

### Implementation

#### Step 1: Define the Generic Repository Class
#### Step 2: Define the Generic Service Class
#### Step 3: Define the Media Classes
#### Step 4: Example Usage

#### Example Usage
1. Create instances of the media classes.
2. Add media items to the repository using the service.
3. Retrieve and print all media items.
4. Find and print media items based on specific conditions (e.g., title contains a certain keyword).

```python
# The following code demonstrates the usage of the generic library management system.
# It creates instances of media items, adds them to the repository using the service,
# and retrieves and prints the media items. It also demonstrates finding media items 
# based on specific conditions. This code should be run after implementing the generic 
# repository, service, and media classes.

# Create repositories
book_repo = Repository[Book]()
magazine_repo = Repository[Magazine]()
dvd_repo = Repository[DVD]()

# Create services
book_service = Service(book_repo)
magazine_service = Service(magazine_repo)
dvd_service = Service(dvd_repo)

# Add media items
book_service.add_item(Book("1984", "George Orwell", 1234567890))
magazine_service.add_item(Magazine("Tech Today", "2023-09-01", "Tech Publishers"))
dvd_service.add_item(DVD("Inception", "Christopher Nolan", 148))

# Retrieve and print all media items
print("All Books:")
for item in book_service.repository.get_all():
    print(item)

print("\nAll Magazines:")
for item in magazine_service.repository.get_all():
    print(item)

print("\nAll DVDs:")
for item in dvd_service.repository.get_all():
    print(item)

# Find and print media items based on conditions
print("\nBooks by George Orwell:")
for item in book_service.find_items(lambda b: b.author == "George Orwell"):
    print(item)
```
