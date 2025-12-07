# Database Schema (MongoDB)

## User
- _id
- name
- email
- password
- role (user/admin)
- createdAt
- updatedAt

## Item (Example)
- _id
- userId (ref: User)
- title
- description
- status
- createdAt
- updatedAt
