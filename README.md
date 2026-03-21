Project done by GAVAUD Denis and PASQUIET Valentin


### holbertonschool-hbnb
Clone the Airbnb application with peers.

## Part 1: Technical Documentation
Context and Objective

In this initial phase, you will focus on creating comprehensive technical documentation that will serve as the foundation for the development of the HBnB Evolution application. This documentation will help in understanding the overall architecture, the detailed design of the business logic, and the interactions within the system.
Problem Description

You are tasked with documenting the architecture and design of a simplified version of an AirBnB-like application, named HBnB Evolution. The application will allow users to perform the following primary operations:

    User Management: Users can register, update their profiles, and be identified as either regular users or administrators.
    Place Management: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.
    Review Management: Users can leave reviews for places they have visited, including a rating and a comment.
    Amenity Management: The application will manage amenities that can be associated with places.

Business Rules and Requirements

    User Entity

    Each user has a first name, last name, email, and password.
    Users can be identified as administrators through a boolean attribute.
    Users should be able to register, update their profile information, and be deleted.

    Place Entity

    Each place has a title, description, price, latitude, and longitude.
    Places are associated with the user who created them (owner).
    Places can have a list of amenities.
    Places can be created, updated, deleted, and listed.

    Review Entity

    Each review is associated with a specific place and user, and includes a rating and comment.
    Reviews can be created, updated, deleted, and listed by place.

    Amenity Entity

    Each amenity has a name, and description.
    Amenities can be created, updated, deleted, and listed.

        Each object should be uniquely identified by a ID.
        For audit reasons, the creation and update datetime should be registered for all entities.

Architecture and Layers

    The application follows a layered architecture divided into:
        Presentation Layer: This includes the services and API through which users interact with the system.
        Business Logic Layer: This contains the models and the core logic of the application.
        Persistence Layer: This is responsible for storing and retrieving data from the database.

Persistence

    All data will be persisted in a database, which will be specified and implemented in Part 3 of the project.

Tasks

    High-Level Package Diagram

    Create a high-level package diagram that illustrates the three-layer architecture of the application and the communication between these layers via the facade pattern.

    Detailed Class Diagram for Business Logic Layer

    Design a detailed class diagram for the Business Logic layer, focusing on the User, Place, Review, and Amenity entities, including their attributes, methods, and relationships. Ensure to include the relationships between Places and Amenities.

    Sequence Diagrams for API Calls

    Develop sequence diagrams for at least four different API calls to show the interaction between the layers and the flow of information. Suggested API calls include user registration, place creation, review submission, and fetching a list of places.

    Documentation Compilation

    Compile all diagrams and explanatory notes into a comprehensive technical document.

Conditions and Constraints

    The documentation must clearly represent the interactions and flow of data between the different layers of the application.
    Use UML notation for all diagrams to ensure consistency and clarity.
    The business rules and requirements outlined above must be reflected accurately in the diagrams.
    Ensure that the diagrams are detailed enough to guide the implementation phase in the next parts of the project.

Resources:

    UML Basics
        [Concept Page] OOP - Introduction to UML

    Package Diagrams
        UML Package Diagram Overview
        UML Package Diagrams Guide

    Class Diagrams
        UML Class Diagram Tutorial
        How to Draw UML Class Diagrams

    Sequence Diagrams
        UML Sequence Diagram Tutorial
        Understanding Sequence Diagrams

    General Diagram Tools
        Mermaid.js Documentation
        draw.io

Expected Outcome

By the end of this part, you should have a complete set of technical documentation that provides a clear and detailed blueprint for the HBnB Evolution application. This documentation will not only guide you through the implementation phases but also ensure that you have a solid understanding of the application's design and architecture.

Good luck, and remember to leverage the provided resources and your own research to overcome any challenges you encounter!




# 0. HIGH LEVEL PACKAGE DIAGRAM OBJECTIVE
Objective

Create a high-level package diagram that illustrates the three-layer architecture of the HBnB application and the communication between these layers via the facade pattern. This diagram will provide a conceptual overview of how the different components of the application are organized and how they interact with each other.
Description

In this task, you will develop a package diagram that visually represents the structure of the application, focusing on its three main layers:

    Presentation Layer (Services, API): This layer handles the interaction between the user and the application. It includes all the services and APIs that are exposed to the users.

    Business Logic Layer (Models): This layer contains the core business logic and the models that represent the entities in the system (e.g., User, Place, Review, Amenity).

    Persistence Layer: This layer is responsible for data storage and retrieval, interacting directly with the database.

Your diagram should clearly show the three layers, the components within each layer, and the communication pathways between them. The facade pattern should be represented as the interface through which the layers interact.
Steps to Complete the Task

    Understand the Layered Architecture

    Review the concept of layered architecture and how it is used to organize an application.
    Understand the responsibilities of each layer in the context of the HBnB application.

    Research the Facade Pattern

    Familiarize yourself with the facade design pattern and how it simplifies interactions between layers by providing a unified interface.

    Identify Key Components

    Identify the key components that belong to each layer:
        Presentation Layer: Services, API endpoints.
        Business Logic Layer: Core models (User, Place, Review, Amenity).
        Persistence Layer: Database access objects or repositories.

    Draft the Package Diagram

    Create a draft of your package diagram, showing the three layers and their components.
    Indicate the communication pathways between layers via the facade pattern.
    Ensure that the diagram is clear, logical, and easy to understand.

    Review and Refine

    Review your diagram to ensure that it accurately represents the application's architecture.
    Make any necessary adjustments to improve clarity and completeness.

Example of a generic package diagram using Mermaid.js:

classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
}
class BusinessLogicLayer {
    +ModelClasses
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations

Learning Resources

    [Concept Page] Software Architecture Patterns - Layered Architecture in Python
    Facade Pattern Overview
    UML Package Diagram Guide
    UML Package Diagram Overview

Deliverables

    High-Level Package Diagram:

    A clear, well-organized package diagram showing the three layers (Presentation, Business Logic, Persistence).

    Communication pathways between layers via the facade pattern.

    Explanatory Notes:

    A brief description of each layer and its responsibilities.

    Explanation of how the facade pattern facilitates communication between the layers.

Recommendations

    Start Simple: Begin with a basic structure, then refine it as you understand the relationships and components better.
    Use Mermaid.js: If you are comfortable with coding, Mermaid.js is a great option for creating diagrams as part of your project documentation. It’s especially useful for version control and iterative development.
    Seek Feedback: Once your diagram is drafted, get feedback from peers or tutors to ensure clarity and accuracy.
    Document As You Go: Keep notes on your design decisions, as these will be useful when you compile your final documentation.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part1



# 1. DETAILED CLASS DIAGRAM FOR BUSINESS LOGIC LAYER
Objective

Design a detailed class diagram for the Business Logic layer of the HBnB application. This diagram will depict the entities within this layer, their attributes, methods, and the relationships between them. The primary goal is to provide a clear and detailed visual representation of the core business logic, focusing on the key entities: User, Place, Review, and Amenity.
Description

In this task, you will create a class diagram that represents the internal structure of the Business Logic layer. This diagram will include entities, their attributes, methods, and relationships such as associations, inheritance, and dependencies.
Steps to Complete the Task

    Review the Business Logic Requirements

    Understand the business rules and requirements for each entity in the Business Logic layer.
    Review how these entities interact with each other and the significance of their relationships.

    Identify Key Attributes and Methods

    For each entity, identify the key attributes and methods that define its behavior and state.
    Ensure that each entity includes a unique identifier (UUID4) and attributes for creation and update dates.

    Design the Class Diagram

    Begin by outlining the entities as classes, specifying their attributes and methods.
    Represent relationships between entities using appropriate UML notation (e.g., associations, generalizations, compositions).
    Include multiplicity where relevant.

    Refine and Review

    Review the diagram to ensure that it accurately represents the business logic and adheres to the project’s requirements.
    Refine the diagram as needed to improve clarity and completeness.

Example of a generic class diagram using Mermaid.js:

classDiagram
class ClassName {
    +AttributeType attributeName
    +MethodType methodName()
}
ClassName1 --|> ClassName2 : Inheritance
ClassName3 *-- ClassName : Composition
ClassName4 --> ClassName : Association

Learning Resources

    UML Class Diagram Tutorial
    How to Draw UML Class Diagrams
    [Concept Page] OOP - SOLID Pronciples
    SOLID Principles of Object-Oriented Design

Deliverables

    Detailed Class Diagram:

    A comprehensive class diagram showing the key entities, including their attributes, methods, and relationships.

    Proper use of UML notation to depict associations, generalizations, and compositions.

    Explanatory Notes:

    A brief description of each entity, including its role in the system and key attributes and methods.

    Explanation of relationships between entities and how they contribute to the overall business logic.

Recommendations

    Start with a Basic Outline: Begin by defining the classes and their basic attributes. Once you have the core structure, add methods and refine the relationships between entities.
    Leverage Mermaid.js: If you are comfortable with coding, consider using Mermaid.js for creating and maintaining your class diagram as part of your project documentation.
    Consider Relationships Carefully: Pay close attention to how entities are related, especially when defining associations and compositions. Ensure that these relationships are accurately represented in your diagram.
    Iterate and Improve: Don’t hesitate to revise your diagram as you refine your understanding of the system. Continuous improvement will lead to a more accurate and comprehensive representation.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part1



# 2. SEQUENCE DIAGRAMS FOR API CALLS
Objective

Develop sequence diagrams for at least four different API calls to illustrate the interaction between the layers (Presentation, Business Logic, Persistence) and the flow of information within the HBnB application. The sequence diagrams will help visualize how different components of the system interact to fulfill specific use cases, showing the step-by-step process of handling API requests.
Description

In this task, you will create sequence diagrams that represent the flow of interactions across the different layers of the application for specific API calls. These diagrams will show how the Presentation Layer (Services, API), Business Logic Layer (Models), and Persistence Layer (Database) communicate with each other to handle user requests.

You will create sequence diagrams for the following API calls:

    User Registration: A user signs up for a new account.
    Place Creation: A user creates a new place listing.
    Review Submission: A user submits a review for a place.
    Fetching a List of Places: A user requests a list of places based on certain criteria.

Steps to Complete the Task

    Understand the Use Cases

    Review the requirements and business logic for each of the selected API calls.
    Understand the sequence of operations needed to fulfill each API call, from the moment a request is received by the API to the point where a response is returned to the client.

    Identify Key Components Involved

    Determine which components of the system (within each layer) are involved in handling each API call.
    Identify the order of operations, including method calls and data exchanges between components.

    Design the Sequence Diagrams

    Begin by drafting the sequence of interactions for each API call.
    For each diagram, start with the API call from the Presentation Layer, followed by interactions with the Business Logic Layer, and ending with operations in the Persistence Layer.
    Clearly show the flow of messages, including method invocations, data retrieval, and processing steps.

    Refine and Review

    Review your diagrams to ensure they accurately reflect the flow of information and operations required to fulfill each API call.
    Refine the diagrams for clarity and completeness, ensuring all relevant interactions are captured.

Example of a generic sequence diagram using Mermaid.js:

sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: API Call (e.g., Register User)
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Response
API-->>User: Return Success/Failure

Learning Resources

    UML Sequence Diagram Tutorial
    Understanding Sequence Diagrams
    RESTful API Design Guide

Deliverables

    Sequence Diagrams:

    Four sequence diagrams, each depicting the interaction flow for a specific API call (User Registration, Place Creation, Review Submission, Fetching a List of Places).

    Diagrams should clearly illustrate the communication between layers and the sequence of operations required to process each request.

    Explanatory Notes:

    A brief description of each API call, outlining the key steps involved and the purpose of the sequence diagram.

    Explanation of the flow of interactions, highlighting how each layer contributes to fulfilling the API request.

Recommendations

    Focus on Clarity: Ensure that your diagrams are easy to read and understand. Use consistent naming conventions for components and clearly indicate the flow of messages.
    Use Mermaid.js for Code-Based Diagrams: If you prefer working with code, Mermaid.js offers a straightforward way to create and maintain sequence diagrams as part of your documentation.
    Double-Check the Flow: Make sure the sequence of operations in your diagrams accurately reflects the intended behavior of the system. Each step should logically follow the previous one.
    Iterate as Needed: Don't hesitate to revise your diagrams as you refine your understanding of the system's interactions. The goal is to create accurate and informative representations of the API calls.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part1



# 3. DOCUMENTATION COMPILATION
Objective

Compile all the diagrams and explanatory notes created in the previous tasks into a comprehensive technical document. This document will serve as a detailed blueprint for the HBnB project, guiding the implementation phases and providing a clear reference for the system’s architecture and design.
Description

In this task, you will bring together the high-level package diagram, detailed class diagram for the Business Logic layer, and sequence diagrams for API calls into a single, well-organized document. The goal is to create a cohesive and comprehensive technical document that not only includes the diagrams but also provides explanatory notes that clarify design decisions, describe interactions, and outline the overall architecture of the application.

The final document should be clear, professional, and structured in a way that makes it easy to follow and understand. It will be used as a reference throughout the project, so accuracy and completeness are critical.
Steps to Complete the Task

    Organize Your Work

    Gather all diagrams created in the previous tasks:
        High-Level Package Diagram (Task 1)
        Detailed Class Diagram for the Business Logic Layer (Task 2)
        Sequence Diagrams for API Calls (Task 3)
    Ensure that each diagram is finalized and reviewed for accuracy and clarity.

    Create an Introduction

    Write a brief introduction for the document that explains its purpose and scope.
    Provide an overview of the HBnB project and the role of this technical document in guiding the implementation process.

    Structure the Document

    Introduction: Briefly describe the project, the purpose of the document, and what it contains.
    High-Level Architecture: Include the high-level package diagram and explain the layered architecture and facade pattern used.
    Business Logic Layer: Present the detailed class diagram, explaining the entities, their relationships, and how they fit into the business logic of the application.
    API Interaction Flow: Include the sequence diagrams for the selected API calls, providing explanations of the interactions and data flow between components.

    Add Explanatory Notes

    For each diagram, include explanatory notes that describe:
        The purpose of the diagram.
        Key components or classes involved.
        Design decisions and their rationale.
        How the diagram fits into the overall architecture and design of the application.

    Review and Edit

    Review the entire document to ensure it is clear, logical, and free of errors.
    Edit the document for clarity, conciseness, and professionalism. Ensure consistent formatting and style throughout.
    Make sure that all diagrams are accurately represented and that their accompanying explanations are clear and informative.

    Finalize the Document

    Save the document in a standard format (e.g., PDF or Word document) for easy sharing and reference.
    Double-check that all components of the technical documentation are included and correctly formatted.

Learning Resources

    Microsoft Writing Style Guide
    Google Developer Documentation Style Guide
    Formatting Documents

Deliverables

Comprehensive Technical Document:

    A well-organized document that includes:
    Introduction: Overview of the project and the purpose of the document.
    High-Level Architecture: High-Level Package Diagram with explanations.
    Business Logic Layer: Detailed Class Diagram with explanations.
    API Interaction Flow: Sequence Diagrams for API calls with explanations.
    The document should be clear, professional, and easy to follow, serving as a reference for the implementation phases.

Recommendations

    Focus on Clarity: Ensure that both the diagrams and the accompanying text are easy to understand. Avoid overly technical jargon unless necessary, and explain all key terms and concepts.
    Consistency is Key: Maintain consistent formatting, terminology, and style throughout the document. This includes consistent naming conventions for classes, methods, and components.
    Seek Feedback: If possible, have peers or tutors review your document before finalizing it. Fresh eyes can help catch any errors or unclear sections you might have missed.
    Proofread Carefully: Errors in a technical document can lead to misunderstandings during implementation, so take the time to thoroughly proofread your work.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part1


## Part 2: Implementation of Business Logic and API Endpoints

In this part of the HBnB Project, you will begin the implementation phase of the application based on the design developed in the previous part. The focus of this phase is to build the Presentation and Business Logic layers of the application using Python and Flask. You will implement the core functionality by defining the necessary classes, methods, and endpoints that will serve as the foundation for the application’s operation.

In this part, you will create the structure of the project, develop the classes that define the business logic, and implement the API endpoints. The goal is to bring the documented architecture to life by setting up the key functionalities, such as creating and managing users, places, reviews, and amenities, while adhering to best practices in API design.

It’s important to note that, at this stage, you will focus only on implementing the core functionality of the API. JWT authentication and role-based access control will be addressed in the next part. The services layer will be built using Flask and the flask-restx extension to create RESTful APIs.
Objectives

By the end of this project, you should be able to:

    Set Up the Project Structure:

    Organize the project into a modular architecture, following best practices for Python and Flask applications.
    Create the necessary packages for the Presentation and Business Logic layers.

    Implement the Business Logic Layer:

    Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
    Implement relationships between entities and define how they interact within the application.
    Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.

    Build RESTful API Endpoints:

    Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
    Use flask-restx to define and document the API, ensuring a clear and consistent structure.
    Implement data serialization to return extended attributes for related objects. For example, when retrieving a Place, the API should include details such as the owner’s first_name, last_name, and relevant amenities.

    Test and Validate the API:

    Ensure that each endpoint works correctly and handles edge cases appropriately.
    Use tools like Postman or cURL to test your API endpoints.

Project Vision and Scope

The implementation in this part is focused on creating a functional and scalable foundation for the application. You will be working on:

    Presentation Layer: Defining the services and API endpoints using Flask and flask-restx. You’ll structure the endpoints logically, ensuring clear paths and parameters for each operation.

    Business Logic Layer: Building the core models and logic that drive the application’s functionality. This includes defining relationships, handling data validation, and managing interactions between different components.

At this stage, you won’t need to worry about user authentication or access control. However, you should ensure that the code is modular and organized, making it easy to integrate these features in Part 3.
Learning Objectives

This part of the project is designed to help you achieve the following learning outcomes:

    Modular Design and Architecture: Learn how to structure a Python application using best practices for modularity and separation of concerns.
    API Development with Flask and flask-restx: Gain hands-on experience in building RESTful APIs using Flask, focusing on creating well-documented and scalable endpoints.
    Business Logic Implementation: Understand how to translate documented designs into working code, implementing core business logic in a structured and maintainable manner.
    Data Serialization and Composition Handling: Practice returning extended attributes in API responses, handling nested and related data in a clear and efficient way.
    Testing and Debugging: Develop skills in testing and validating APIs, ensuring that your endpoints handle requests correctly and return appropriate responses.

Recommended Resources

    Flask and flask-restx Documentation:

    Flask Official Documentation
    flask-restx Documentation

    RESTful API Design Best Practices:

    Best Practices for Designing a Pragmatic RESTful API
    REST API Tutorial

    Python Project Structure and Modular Design:

    Structuring Your Python Project
    Modular Programming with Python

    Facade Design Pattern:

    Facade Pattern in Python

This introduction sets the stage for the implementation phase of the project, where you will focus on bringing the documented design to life through well-structured code. The tasks ahead will challenge you to apply object-oriented principles, build scalable APIs, and think critically about how different components of the application interact.

Tasks

# 0. Project Setup and Package Initialization
Objective

Set up the initial project structure for the HBnB application, ensuring the codebase is organized according to best practices for a modular Python application. The focus is on creating the necessary folders, packages, and files for the Presentation, Business Logic, and Persistence layers while preparing the code to integrate the Facade pattern. Although the Persistence layer will be fully implemented in Part 3 using SQL Alchemy, this task includes setting up the structure and providing the complete implementation of an in-memory repository to handle object storage and validation.
Context

Before diving into the implementation of the business logic and API endpoints, it’s essential to have a well-organized project structure. A clear and modular organization will help maintain the codebase, make it easier to integrate new features, and ensure that your application is scalable. Additionally, to simplify the implementation, you are provided with the complete in-memory repository code. This repository will later be replaced by a database-backed solution in Part 3.

In this task, you will:

    Set up the structure for the Presentation, Business Logic, and Persistence layers.
    Prepare the project to use the Facade pattern for communication between layers.
    Implement the in-memory repository to handle object storage and validation.
    Plan for future integration of the Persistence layer, even though it won’t be fully implemented in this part.

Instructions

-> Find the detailed instructions for this task here <-
Expected Outcome

By the end of this task, you should have a well-organized project structure that accommodates the Presentation, Business Logic, and Persistence layers. The codebase should be modular and easy to maintain, with a clear separation of concerns. You’ll also have a functional Flask application that is ready to integrate API endpoints, business logic, and persistence in the upcoming tasks.

The in-memory repository and Facade pattern are now set up to streamline communication between layers. While the persistence layer is only using in-memory storage at this stage, it is designed to be easily replaced with a database-backed solution in Part 3.
Resources

    Flask Documentation: https://flask.palletsprojects.com/en/stable/
    Flask-RESTx Documentation: https://flask-restx.readthedocs.io/en/latest/
    Python Project Structure Best Practices: https://docs.python-guide.org/writing/structure/
    Facade Design Pattern in Python: https://refactoring.guru/design-patterns/facade/python/example

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 1. Core Business Logic Classes
Objective

Implement the core business logic classes that define the entities of the HBnB application, including the necessary attributes, methods, and relationships. This task focuses on creating the fundamental models (User, Place, Review, and Amenity) while considering the design choices made by students in Part 1.
Context

In Part 1, students designed the Business Logic layer, including defining entities and relationships. This task requires you to implement those designs while adhering to best practices for modular, maintainable code. You may have already created base classes with common attributes (e.g., id, created_at, and updated_at) to be inherited by concrete classes such as User, Place, Review, and Amenity.

In this task, you will:

    Implement the classes based on your Part 1 design.
    Ensure relationships between entities are correctly implemented.
    Handle attribute validation and updates according to the requirements.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Python OOP Basics: https://realpython.com/python3-object-oriented-programming/
    Designing Classes and Relationships: https://docs.python.org/3/tutorial/classes.html
    Why You Should Use UUIDs: https://datatracker.ietf.org/doc/html/rfc4122

Expected Outcome

By the end of this task, you should have fully implemented core business logic classes (User, Place, Review, Amenity) with the appropriate attributes, methods, and relationships. With these components in place, you will be ready to proceed to implementing the API endpoints in the next task. The implemented classes should support the necessary validation, relationships, and data integrity checks required for the application’s core functionality. Additionally, the relationships between entities should be fully operational, allowing seamless interactions like linking reviews to places or associating amenities with places.

With this solid foundation in place, the business logic will be prepared for further integration with the Presentation and Persistence layers in subsequent tasks.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 2. User Endpoints
Objective

Implement the API endpoints needed for managing users in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update) for users, ensuring that these endpoints are integrated with the Business Logic layer. The DELETE operation will not be implemented for users in this part of the project. Additionally, when retrieving user data, the password should not be included in the response. The API interface, return format, and status codes must be clearly defined since black-box testing will be performed later.

In this task, the full implementation for user creation (POST) and retrieval (GET) by ID is provided as a guide. You will be responsible for implementing the retrieval of the list of users (GET /api/v1/users/) and updating user information (PUT /api/v1/users/). The approach for the remaining endpoints follows similar principles and should be implemented analogously. The same applies to the other entities (e.g., Place, Review, Amenity).

In this task, you will:

    Set up the POST, GET, and PUT endpoints for managing users.
    Implement the logic for handling user-related operations in the Business Logic layer.
    Integrate the Presentation layer (API) and Business Logic layer, utilizing the repository pattern.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-RESTx Documentation: https://flask-restx.readthedocs.io/en/latest/
    Testing REST APIs with cURL: https://everything.curl.dev/
    Designing RESTful APIs: https://restfulapi.net/

Expected Outcome

By the end of this task, you should have fully implemented the core user management endpoints, including the ability to create, read, and update users. The DELETE operation will not be implemented for users in this part. The provided implementation guide for the user registration endpoint should serve as a model for implementing the remaining user endpoints as well as endpoints for other entities (e.g., Place, Review, Amenity). The functionality should be documented and tested, ensuring that all user-related operations are handled smoothly within the HBnB application.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 3. Amenity Endpoints
Objective

Implement the API endpoints required for managing amenities in the HBnB application. This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for amenities, while ensuring integration with the Business Logic layer via the Facade pattern. The DELETE operation will not be implemented for amenities in this part of the project.

In this task, you will:

    Set up the POST, GET, and PUT endpoints for managing amenities.
    Implement the necessary logic for handling amenity-related operations in the Business Logic layer.
    Integrate the Presentation layer (API) and Business Logic layer through the Facade.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-RESTx Documentation: https://flask-restx.readthedocs.io/en/latest/
    Testing REST APIs with cURL: https://everything.curl.dev/
    Designing RESTful APIs: https://restfulapi.net/

Expected Outcome

By the end of this task, you should have fully implemented the core amenity management endpoints, including the ability to create, read, and update amenities. The DELETE operation will not be implemented for amenities in this part. The provided placeholders should guide you in implementing the logic based on the example provided for user registration. The functionality should be documented and tested, ensuring that all amenity-related operations are handled smoothly within the HBnB application.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 4. Place Endpoints
Objective

Implement the API endpoints needed for managing places in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update) for places, ensuring that these endpoints are integrated with the Business Logic layer through the Facade pattern. The DELETE operation will not be implemented for places in this part of the project.

Given that the Place entity has relationships with other entities, such as User (owner) and Amenity, you’ll need to handle these relationships carefully while maintaining the integrity of the application logic. The Review entity will be implemented in the next task, so it should not be included in this task.

In this task, you will:

    Set up the POST, GET, and PUT endpoints for managing places.
    Implement the logic for handling place-related operations in the Business Logic layer.
    Integrate the Presentation layer (API) and Business Logic layer through the Facade.
    Implement validation for specific attributes like price, latitude, and longitude.
    Ensure that related data such as owner details and amenities are properly handled and returned with the Place data.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-RESTx Documentation: https://flask-restx.readthedocs.io/en/latest/
    Testing REST APIs with cURL: https://everything.curl.dev/
    Designing RESTful APIs: https://restfulapi.net/

Expected Outcome

By the end of this task, you should have implemented the core place management endpoints, including the ability to create, read, and update places. The DELETE operation will not be implemented for places in this part. You will have handled the relationships between places, owners, and amenities, including validating specific attributes like price, latitude, and longitude. The functionality should be documented and tested, ensuring smooth operation within the HBnB application.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 5. Review Endpoints
Objective

Implement the API endpoints needed for managing reviews in the HBnB application. This task involves setting up CRUD operations (Create, Read, Update, Delete) for reviews, ensuring that these endpoints are integrated with the Business Logic layer through the Facade pattern. The DELETE operation will be implemented for reviews, making it the only entity for which deletion is supported in this part of the project.

In this task, you will:

    Set up the POST, GET, PUT, and DELETE endpoints for managing reviews.
    Implement the logic for handling review-related operations in the Business Logic layer.
    Integrate the Presentation layer (API) and Business Logic layer through the Facade.
    Implement validation for specific attributes like the text of the review and ensure that the review is associated with both a user and a place.
    Update the Place model in api/v1/places.py to include the collection of reviews for a place.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-RESTx Documentation: https://flask-restx.readthedocs.io/en/latest/
    Testing REST APIs with cURL: https://everything.curl.dev/
    Designing RESTful APIs: https://restfulapi.net/

Expected Outcome

By the end of this task, you should have implemented the core review management endpoints, including the ability to create, read, update, and delete reviews. Additionally, you will have implemented the ability to retrieve all reviews associated with a specific place. The DELETE operation is introduced here to allow students to practice implementing this functionality for the first time. The functionality should be documented and tested, ensuring that all review-related operations are handled smoothly within the HBnB application.

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2


# 6. Testing and Validation
Objective

This task involves creating and running tests for the endpoints you have developed so far. You will implement validation logic, perform thorough testing using cURL, and document the results of those tests. The focus is on ensuring that each endpoint works as expected and adheres to the input/output formats, status codes, and validation rules you have defined in previous tasks.

In this task, you will:

    Implement basic validation checks for each of the attributes in your endpoints.
    Perform black-box testing using cURL and the Swagger documentation generated by Flask-RESTx.
    Create a detailed testing report, highlighting both successful and failed cases.

Instructions

-> Find the detailed instructions for this task here <-
Expected Outcome

By the end of this task, you should have:

    Implemented basic validation for all entity models.
    Performed thorough testing using cURL and other tools.
    Generated Swagger documentation to confirm that your API is correctly described.
    Created and executed unit tests using unittest or pytest.
    Documented the testing process, highlighting both successful cases and edge cases that were handled correctly.

This task combines both manual and automated testing while guiding students to validate and thoroughly test their implementation. Let me know if any additional information is needed!

Repo:

    GitHub repository: holbertonschool-hbnb
    Directory: part2

## Part 3: Enhanced Backend with Authentication and Database Integration

Welcome to Part 3 of the HBnB Project, where you will extend the backend of the application by introducing user authentication, authorization, and database integration using SQLAlchemy and SQLite for development. Later, you'll configure MySQL for production environments. In this part, you will secure the backend, introduce persistent storage, and prepare the application for a scalable, real-world deployment.
Objectives of the Project

    Authentication and Authorization: Implement JWT-based user authentication using Flask-JWT-Extended and role-based access control with the is_admin attribute for specific endpoints.
    Database Integration: Replace in-memory storage with SQLite for development using SQLAlchemy as the ORM and prepare for MySQL or other production grade RDBMS.
    CRUD Operations with Database Persistence: Refactor all CRUD operations to interact with a persistent database.
    Database Design and Visualization: Design the database schema using mermaid.js and ensure all relationships between entities are correctly mapped.
    Data Consistency and Validation: Ensure that data validation and constraints are properly enforced in the models.

Learning Objectives

By the end of this part, you will:

    Implement JWT authentication to secure your API and manage user sessions.
    Enforce role-based access control to restrict access based on user roles (regular users vs. administrators).
    Replace in-memory repositories with a SQLite-based persistence layer using SQLAlchemy for development and configure MySQL for production.
    Design and visualize a relational database schema using mermaid.js to handle relationships between users, places, reviews, and amenities.
    Ensure the backend is secure, scalable, and provides reliable data storage for production environments.

Project Context

In the previous parts of the project, you worked with in-memory storage, which is ideal for prototyping but insufficient for production environments. In Part 3, you'll transition to SQLite, a lightweight relational database, for development, while preparing the system for MySQL in production. This will give you hands-on experience with real-world database systems, allowing your application to scale effectively.

Additionally, you'll introduce JWT-based authentication to secure the API, ensuring that only authenticated users can interact with certain endpoints. You will also implement role-based access control to enforce restrictions based on the user's privileges (regular users vs. administrators).
Project Resources

Here are some resources that will guide you through this part of the project:

    JWT Authentication: Flask-JWT-Extended Documentation
    SQLAlchemy ORM: SQLAlchemy Documentation
    SQLite: SQLite Documentation
    Flask Documentation: Flask Official Documentation
    Mermaid.js for ER Diagrams: Mermaid.js Documentation

Structure of the Project

In this part of the project, the tasks are organized in a way that builds progressively towards a complete, secure, and database-backed backend system:

    Modify the User Model to Include Password: You will start by modifying the User model to store passwords securely using bcrypt2 and update the user registration logic.
    Implement JWT Authentication: Secure the API using JWT tokens, ensuring only authenticated users can access protected endpoints.
    Implement Authorization for Specific Endpoints: You will implement role-based access control to restrict certain actions (e.g., admin-only actions).
    SQLite Database Integration: Transition from in-memory data storage to SQLite as the persistent database during development.
    Map Entities Using SQLAlchemy: Map existing entities (User, Place, Review, Amenity) to the database using SQLAlchemy and ensure relationships are well-defined.
    Prepare for MySQL in Production: Towards the end of this phase, you’ll configure the application to use MySQL in production and SQLite for development.
    Database Design and Visualization: Use mermaid.js to create entity-relationship diagrams for your database schema.

Each task is carefully designed to build on previous work and ensure the system transitions smoothly from development to production readiness.

By the end of Part 3, you will have a backend that not only stores data in a persistent and secure database but also ensures that only authorized users can access and modify specific data. You will have implemented industry-standard authentication and database management practices that are crucial for real-world web applications.

# 0. Modify the Application Factory to Include the Configuration
Objective

Update the Flask Application Factory to include the configuration object.
Context

In the previous part of the project, we created a Config class to handle different configurations in the application, but we weren't using it yet. In this task, you will update the create_app() method (following the Application Factory pattern) in the app/__init__.py file to receive a configuration, which will be used to instantiate the application.

IMPORTANT: Before starting the task, be sure to read and understand the resources provided below.
Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask Documentation: Application Factories
    Flask Documentation: Configuration Handling

Expected Outcome

By the end of this task, you should have a fully functional Application Factory that can handle different configurations.


# 1. Modify the User Model to Include Password Hashing
Objective

Update the User model to securely store a hashed password using bcrypt. Modify the user registration endpoint to accept the password field and ensure that it is hashed before storing it. The password should not be returned in any GET requests.
Context

In previous tasks, the User model was created, but it did not handle passwords. In this task, you will enhance the User model to support password hashing using bcrypt, ensuring passwords are securely stored. Additionally, you will update the user registration endpoint to accept and hash passwords before storing them. Passwords will not be returned in any GET requests.
Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-Bcrypt Documentation: Flask-Bcrypt
    Password Hashing Best Practices: OWASP Password Storage Cheat Sheet

Expected Outcome

By the end of this task, the User model will securely hash and store passwords using bcrypt. The POST /api/v1/users/ endpoint will accept passwords and securely hash them before storing. Passwords will not be returned in any GET requests.


# 2. Implement JWT Authentication with `flask-jwt-extended`
Objective

Set up JWT-based authentication for the HBnB application, enabling secure login functionality. This task involves configuring the API to generate and verify JWT tokens using the flask-jwt-extended extension. Tokens will be issued upon successful login and required for accessing protected endpoints.
Context

JWT (JSON Web Token) allows secure authentication by providing a token that clients can use to access protected resources without having to re-authenticate on every request. JWT is stateless, meaning the server doesn’t need to store user sessions, making it ideal for scalable applications. JWT tokens also allow embedding additional claims (such as user roles), which is useful for authorization.

In this task, we will set up user login, issue JWT tokens, and use these tokens to protect specific API endpoints.
Instructions

-> Find the detailed instructions for this task here <-
Resources

    JWT Authentication: JWT.io
    Flask-JWT-Extended Documentation: Flask-JWT-Extended
    JWT Best Practices: OWASP JWT Security

Expected Outcome

By the end of this task, students will have implemented user login functionality using JWT. They will be able to generate and verify JWT tokens, protect specific API endpoints, and embed claims (like is_admin) within the token for future authorization checks.


# 3. Implement Authenticated User Access Endpoints
Objective

Secure various API endpoints to allow only authenticated users to perform specific actions, including creating and modifying places and reviews, as well as updating their own user details. Access will be controlled via JWT authentication, with additional validation to ensure users can only modify data that belongs to them (e.g., places they own, reviews they created).
Context

Authenticated user access is a critical part of securing an API. By ensuring that only authorized users can perform specific actions, the integrity of the data is protected. This task focuses on securing endpoints related to creating and modifying places and reviews, while also allowing users to modify their own data.

In this task, you will:

    Secure endpoints to ensure only authenticated users can create, update, and delete resources.
    Add logic to validate ownership of places and reviews.
    Implement logic to prevent users from reviewing places they own or reviewing a place multiple times.
    Verify that public users can access the PUBLIC endpoints without a JWT token.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-JWT-Extended Documentation: Flask-JWT-Extended
    Testing REST APIs with cURL: Everything cURL

Expected Outcome

By the end of this task, the following endpoints will be secured, allowing only authenticated users to perform actions based on their ownership of places and reviews:

    Create, update, and delete places (with ownership checks).
    Create and update reviews (with restrictions on reviewing owned places and duplicate reviews).
    Modify user details (excluding email and password).


# 4. Implement Administrator Access Endpoints
Objective

Restrict access to specific API endpoints so that only users with administrative privileges can perform certain actions. These actions include creating new users, modifying any user's details (including email and password), and adding or modifying amenities. Additionally, administrators can perform the same tasks as authenticated users without being restricted by ownership of places and reviews.
Context

Role-based access control (RBAC) is crucial in API security. Administrators have the highest level of privileges, and this task will allow them to bypass restrictions that regular users face. This includes the ability to manage any user or resource in the system.

In this task, you will:

    Implement logic for restricting access to specific endpoints based on the user's role (is_admin).
    Ensure that administrators can manage user accounts, including creating and modifying user details.
    Allow administrators to bypass ownership restrictions for places and reviews.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Flask-JWT-Extended Documentation: Flask-JWT-Extended
    Bcrypt Documentation: Flask-Bcrypt

Expected Outcome

By the end of this task, admins will be able to:

    Create new users.
    Modify any user’s data, including email and password (with validation for unique emails).
    Add and modify amenities.
    Bypass ownership restrictions on places and reviews.


# 5. Implement SQLAlchemy Repository
Objective

Replace the in-memory repository with a SQLAlchemy-based repository for persistence. In this task, you will create the SQLAlchemyRepository and integrate it into the project for managing database interactions. This task will lay the foundation for further model mapping and database setup in subsequent tasks.
Context

In the previous parts of the project, the persistence layer was managed using an in-memory repository. This task introduces SQLAlchemy to persist data in an SQLite database during development, preparing the application for a production-ready relational database. The repository pattern remains the same, but the implementation will now interact with SQLAlchemy for all CRUD operations. Due to the fact that the database has not yet been initialized, this task focuses only on creating the repository. Model mapping and database initialization will follow in the next task.

You will:

    Create the SQLAlchemy repository that implements the existing repository interface.
    Refactor the existing Facade to utilize the SQLAlchemy-based repository for user operations.
    Provide code and detailed instructions for integration, but no database initialization will be performed yet.

Read this guide before start: Transitioning from In-Memory to Database Persistence: A Step-by-Step Guide
Instructions

-> Find the detailed instructions for this task here <-
Resources

    SQLAlchemy Documentation: SQLAlchemy
    Flask-SQLAlchemy Documentation: Flask-SQLAlchemy

Expected Outcome

By the end of this task, you will have implemented the SQLAlchemyRepository and refactored the Facade to use this new repository for data persistence. However, since the model mapping and database initialization will be performed in the next task, the actual integration testing will be delayed until the next step.


# 6. Map the User Entity to SQLAlchemy Model
Objective

Map the User entity to a SQLAlchemy model, ensuring the correct database relationships, attribute definitions, and CRUD operations are implemented. You will incorporate the ORM functionality within the repository layer, service layer (Facade), and API layer for full integration. The password hashing mechanism from the previous task should remain functional.
Context

In the previous task, the repository was updated to use SQLAlchemy for database persistence, replacing the in-memory repository. This task extends that functionality by mapping the User entity to the database using SQLAlchemy. The new UserRepository will be responsible for handling user-specific queries, enhancing the flexibility and maintainability of the application. As we're also using a BaseClass to handle the common attributes for all the Business Logic classes, we'll update this class first to manage the mapping.

In this task, you will:

    Map the BaseModel class to a SQLAlchemy model, including the id, created_at and updated_at attributes.
    Map the User entity to a SQLAlchemy model, including attributes like first_name, last_name, email, password, and is_admin.
    Implement the UserRepository class to interact with the database using SQLAlchemy.
    Refactor the Facade to use the UserRepository for user-related operations.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    SQLAlchemy Documentation: SQLAlchemy
    Flask-SQLAlchemy Documentation: Flask-SQLAlchemy
    Flask-Bcrypt Documentation: Flask-Bcrypt
    Testing REST APIs with cURL: Everything cURL

Expected Outcome

By the end of this task, the User entity will be fully mapped to a SQLAlchemy model, and the repository pattern will be updated to interact with the database using SQLAlchemy. You will have refactored the Facade to use the new UserRepository, and the application will now store user data in the database persistently.


# 7. Map the Place, Review, and Amenity Entities
Objective

Map the Place, Review, and Amenity entities to SQLAlchemy models. This task requires you to apply the knowledge gained from mapping the User entity in the previous task to these new entities. You will implement the core database attributes for each entity, and in subsequent tasks, relationships between entities will be defined. No relationships between these entities should be added at this point.
Context

In the previous tasks, you mapped the User entity and implemented the UserRepository to interact with the database through SQLAlchemy. Now, you will extend this mapping to the Place, Review, and Amenity entities. These mappings will prepare the foundation for the relationships that will be added later between places, reviews, amenities, and users.

In this task, you will:

    Map the core attributes for Place, Review, and Amenity entities.
    Ensure that each entity has basic CRUD functionality through the repository pattern.
    Follow the same process you used to map the User entity in the previous tasks.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    SQLAlchemy Documentation: SQLAlchemy
    Flask-SQLAlchemy Documentation: Flask-SQLAlchemy
    SQLAlchemy Relationship Patterns: SQLAlchemy ORM Relationships

Expected Outcome

By the end of this task, you should have mapped the Place, Review, and Amenity entities to SQLAlchemy models, ensuring that their basic attributes are stored in the database. The repositories and facade methods should be updated to handle CRUD operations for each entity. No relationships between entities should be implemented yet; this will be done in a later task.


# 8. Map Relationships Between Entities Using SQLAlchemy
Objective

Map the relationships between the entities using SQLAlchemy. You will define both one-to-many and many-to-many relationships and apply the appropriate constraints and foreign keys in the models. This task will serve as a foundation for linking related data in your application.
Context

Now that you have defined the core entities like User, Place, Review, and Amenity, it's time to establish relationships between these entities. These relationships reflect the connections between the real-world concepts represented by the entities (e.g., a User can own many Places, a Place can have many Reviews). Defining relationships in the database ensures that related data can be easily queried and manipulated in a structured way.

In this task, you will define relationships between the entities, using SQLAlchemy’s ORM capabilities. Relationships like "one-to-many" and "many-to-many" allow for a clear and efficient organization of data, enforcing the logical structure of the database.
Instructions

-> Find the detailed instructions for this task here <-
Resources

    SQLAlchemy Documentation: SQLAlchemy
    Flask-SQLAlchemy Documentation: Flask-SQLAlchemy
    SQLAlchemy Relationship Patterns: SQLAlchemy ORM Relationships

Expected Outcome

By the end of this task, you will have successfully mapped the relationships between entities using SQLAlchemy. These relationships will ensure data integrity and allow efficient querying of related data, enabling complex operations such as retrieving all reviews for a place or all places owned by a user. The correct use of relationship(), backref, and foreign keys will establish clear, bidirectional links between your entities.


# 9. SQL Scripts for Table Generation and Initial Data
Objective

Create SQL scripts to generate the entire database schema for the HBnB project and populate it with initial data. The scripts should include all tables and relationships necessary to reflect the project’s model and insert the required initial data.
Context

In this task, you will focus on designing the database schema using raw SQL to generate tables and insert initial data. This includes creating tables for User, Place, Review, Amenity, and their relationships. The purpose of this task is to practice defining databases independently of any ORM, ensuring you understand how to design tables and relationships at the SQL level.
Instructions

-> Find the detailed instructions for this task here <-
Resources

    SQL Tutorial for Beginners: W3Schools SQL Tutorial

Expected Outcome

By the end of this task, you should have:

    SQL scripts that generate the full database schema.
    Inserted an administrator user and amenities into the database.
    Tested CRUD operations to verify correct functionality of the schema and data.


# 10. Generate Database Diagrams
Objective

Create Entity-Relationship (ER) diagrams to visually represent the structure of the database schema for the HBnB project using Mermaid.js. This task will help ensure that the database schema is accurately reflected and consistent with previous parts of the project. Students will use Mermaid.js to visualize tables and their relationships in a readable format.
Context

Visualizing database relationships is crucial for understanding the connections between entities. ER diagrams provide a high-level overview of the database's structure and serve as an essential reference for further development or debugging. Mermaid.js is a tool that allows you to create these diagrams in markdown-like syntax, making it easy to integrate them into documentation and collaboration platforms like GitHub or GitLab.

In this task, you will:

    Learn to use Mermaid.js to create ER diagrams.
    Generate diagrams that represent the User, Place, Review, Amenity, and Place_Amenity tables, along with their relationships.
    Ensure consistency in the schema visualization, using Mermaid.js as the primary tool for diagram generation.

Instructions

-> Find the detailed instructions for this task here <-
Resources

    Mermaid.js Documentation: Mermaid.js Official Docs
    Live Mermaid.js Editor: Mermaid Live Editor
    SQLAlchemy Relationship Documentation: SQLAlchemy ORM Relationships

Expected Outcome

By the end of this task, you should have:

    Created an ER diagram in Mermaid.js that accurately represents the database schema for HBnB.
    Understood the various types of relationships (one-to-many, many-to-many) and how they are represented visually.
    Exported the diagram to be included in your project documentation.


### ER diagram representing the core entities of the HBnB project

![Mermaid](Mermaid.png)
