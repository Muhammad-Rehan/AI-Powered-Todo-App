Next.js App Router Skill

## Metadata
name: nextjs-app-router
description: Use for implementing Next.js applications with the App Router architecture

## Overview
This Skill provides specialized knowledge for implementing Next.js applications with the App Router architecture. When creating Next.js applications using the app directory, implementing server components, or working with the modern Next.js architecture, apply these guidelines to ensure proper structure and performance.

## App Directory Structure

- Organize files using the app directory convention
- Create route segments with folders
- Implement layout and template components appropriately
- Use the correct file naming conventions (page.js, layout.js, etc.)
- Structure nested routes correctly
- Implement parallel and intercepted routes when needed

## Server and Client Components

- Use Server Components by default for data fetching
- Use Client Components only when interactivity is required
- Implement proper "use client" directives
- Pass data from server to client components appropriately
- Handle component boundaries effectively
- Optimize component types for performance

## Data Fetching Patterns

- Use async/await in Server Components for data fetching
- Implement server-side rendering with proper caching
- Use Suspense for loading states
- Implement proper error handling for data fetching
- Use React Query or similar for client-side caching if needed
- Follow Next.js data fetching best practices

## Routing and Navigation

- Implement dynamic routes with bracket notation [slug]
- Use Next.js navigation APIs (router, Link)
- Handle route parameters and search parameters
- Implement proper URL structure and SEO
- Use intercepting routes when needed
- Handle route transitions and loading states

## Forms and Actions

- Implement server actions for form submissions
- Handle form state and validation appropriately
- Use React Hook Form or similar for complex forms
- Implement proper error handling for form submissions
- Handle file uploads if needed
- Manage optimistic updates where appropriate

## Styling and Assets

- Use Tailwind CSS for styling
- Implement proper CSS module patterns if needed
- Handle asset optimization (images, fonts, etc.)
- Implement responsive design patterns
- Use Next.js Image component for optimization
- Manage global and component-specific styles

## API Routes

- Create API routes in the app/api directory
- Implement proper request/response handling
- Use Next.js API route features
- Handle authentication in API routes
- Implement proper error responses
- Follow RESTful API patterns

## Performance Optimization

- Implement code splitting effectively
- Use dynamic imports when appropriate
- Optimize component rendering
- Implement proper caching strategies
- Use Next.js image and font optimization
- Minimize bundle sizes

## Security Implementation

- Validate and sanitize user inputs
- Implement proper authentication flows
- Secure API routes appropriately
- Handle JWT tokens securely
- Implement proper CORS policies
- Follow Next.js security best practices

## Error Handling

- Implement global error boundaries
- Handle loading and error states with Suspense
- Create custom error pages
- Implement proper error logging
- Handle client and server errors appropriately
- Provide user-friendly error messages

## Testing

- Write tests for components and pages
- Implement integration tests for critical flows
- Use Next.js testing utilities
- Test server and client components appropriately
- Implement end-to-end testing
- Follow testing best practices

## When to Apply

Apply these guidelines whenever implementing:
- Next.js applications with App Router
- Server and Client component architecture
- Data fetching and rendering patterns
- Routing and navigation systems
- Form handling and API routes
- Performance optimization strategies

## Code Standards

- Follow Next.js App Router conventions
- Use Server Components by default
- Implement proper error handling and loading states
- Follow React and Next.js best practices
- Write comprehensive tests for critical functionality