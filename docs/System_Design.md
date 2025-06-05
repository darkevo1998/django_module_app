# System Design Documentation

## Database Schema (ERD)

```mermaid
erDiagram
    User ||--o{ Group : belongs_to
    Group ||--o{ Permission : has
    Module ||--o{ Product : manages
    User ||--o{ Permission : has

    User {
        int id PK
        string username
        string password
        string email
        boolean is_active
        datetime date_joined
    }

    Group {
        int id PK
        string name
    }

    Module {
        int id PK
        string name
        text description
        string version
        boolean is_installed
        datetime created_at
        datetime updated_at
    }

    Product {
        int id PK
        string name
        string barcode
        decimal price
        int stock
        datetime created_at
        datetime updated_at
    }

    Permission {
        int id PK
        string name
        string codename
        int content_type_id
    }
```

## Module Management Flow

```mermaid
flowchart TD
    A[Start] --> B[Access /module]
    B --> C[View Module List]
    C --> D{User Action}
    D -->|Install| E[Install Module]
    D -->|Uninstall| F[Uninstall Module]
    D -->|Upgrade| G[Upgrade Module]
    E --> H[Update Status]
    F --> H
    G --> H
    H --> I[End]
```

## Product Management Flow

```mermaid
flowchart TD
    A[Start] --> B[Access /products]
    B --> C{Module Installed?}
    C -->|Yes| D[Check User Role]
    C -->|No| E[Show 404]
    D --> F{User Role}
    F -->|Manager| G[Show CRUD]
    F -->|User| H[Show CRU]
    F -->|Public| I[Show Read-only]
    G --> J{User Action}
    H --> J
    I --> J
    J -->|Create| K[Create Form]
    J -->|Update| L[Update Form]
    J -->|Delete| M[Delete Confirm]
    J -->|View| N[View Product]
    K --> O[Save]
    L --> O
    M -->|Confirm| P[Delete]
    M -->|Cancel| Q[Cancel]
    O --> R[End]
    P --> R
    Q --> R
    N --> R
```

## Authentication Flow

```mermaid
flowchart TD
    A[Start] --> B[Access Protected Page]
    B --> C{Authenticated?}
    C -->|No| D[Redirect to Login]
    C -->|Yes| E[Check Permissions]
    D --> F[Show Login Form]
    F --> G{Valid Credentials?}
    G -->|Yes| H[Set Session]
    G -->|No| I[Show Error]
    H --> J[Redirect to Page]
    E --> K{Has Permission?}
    K -->|Yes| L[Allow Access]
    K -->|No| M[Show Access Denied]
    J --> N[End]
    L --> N
    M --> N
    I --> N
```

## UI Design

### Module List Page
```
+----------------------------------+
|  Modular Django        [Login]   |
+----------------------------------+
| Modules | Products              |
+----------------------------------+
| Available Modules                |
+----------------------------------+
| Name    | Desc  | Ver  | Status |
|---------|-------|------|--------|
| Product | CRUD  | 1.0  | [Inst] |
| Module  |       |      |        |
+----------------------------------+
```

### Product List Page
```
+----------------------------------+
|  Modular Django        [Logout]  |
+----------------------------------+
| Modules | Products              |
+----------------------------------+
| Products                [Add]    |
+----------------------------------+
| Name  | Barcode | Price | Stock |
|-------|---------|-------|-------|
| Item1 | 123456  | $10   | 100   |
| Item2 | 789012  | $20   | 50    |
+----------------------------------+
```

### Product Form
```
+----------------------------------+
|  Create/Update Product           |
+----------------------------------+
| Name:     [                  ]   |
| Barcode:  [                  ]   |
| Price:    [                  ]   |
| Stock:    [                  ]   |
|                                  |
| [Save] [Cancel]                  |
+----------------------------------+
```

### Delete Confirmation
```
+----------------------------------+
|  Delete Product                  |
+----------------------------------+
| Are you sure to delete this      |
| data?                            |
|                                  |
| [Yes, Delete] [Cancel]           |
+----------------------------------+
```

## Color Scheme
- Primary: #007bff (Bootstrap Blue)
- Secondary: #6c757d (Bootstrap Gray)
- Success: #28a745 (Bootstrap Green)
- Danger: #dc3545 (Bootstrap Red)
- Warning: #ffc107 (Bootstrap Yellow)
- Background: #ffffff (White)
- Text: #212529 (Bootstrap Dark)

## Typography
- Headings: Roboto
- Body: Open Sans
- Monospace: Source Code Pro

## Responsive Design
- Mobile First Approach
- Breakpoints:
  - xs: < 576px
  - sm: ≥ 576px
  - md: ≥ 768px
  - lg: ≥ 992px
  - xl: ≥ 1200px 