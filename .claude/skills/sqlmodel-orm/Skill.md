SQLModel ORM Skill

## Metadata
name: sqlmodel-orm
description: Use for database modeling, relationships, and SQLModel ORM operations

## Overview
This Skill provides specialized knowledge for working with SQLModel ORM, database modeling, and database operations. When creating database models, defining relationships, or implementing database operations, apply these guidelines to ensure proper structure, performance, and data integrity.

## SQLModel Best Practices

- Use SQLModel classes that inherit from SQLModel and Base
- Define proper table names with __tablename__
- Use appropriate field types and constraints
- Implement proper relationships between models
- Use Field() for column-specific configurations
- Define indexes for frequently queried columns

## Database Modeling

- Create normalized database schemas
- Define proper foreign key relationships
- Use appropriate data types for each field
- Implement proper constraints and validations
- Use UUID for primary keys when appropriate
- Define default values and nullable fields appropriately

## Relationship Patterns

- Use relationship() for defining relationships between models
- Implement proper back_populates for bidirectional relationships
- Use lazy loading strategies appropriately
- Define cascade options for related data operations
- Handle many-to-many relationships with association tables

## Query Optimization

- Use async session operations for database queries
- Implement proper filtering and sorting
- Use joins appropriately for related data
- Implement pagination for large datasets
- Use raw SQL queries only when ORM limitations require it
- Optimize queries with proper indexing

## Data Operations

- Implement proper CRUD operations
- Use transactions for complex operations
- Handle database exceptions appropriately
- Validate data before insertion/updating
- Implement proper data serialization/deserialization

## When to Apply

Apply these guidelines whenever implementing:
- Database model definitions
- Relationship definitions
- Database operations (CRUD)
- Query optimization
- Data validation and constraints
- Transaction management

## Code Standards

- Use async operations for all database interactions
- Implement proper error handling for database operations
- Follow SQLModel best practices for field definitions
- Use type hints for all model properties
- Write comprehensive tests for database operations