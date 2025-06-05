# System Flowchart

## Module Management Flow

```plantuml
@startuml Module Management

start
:User accesses /module;
:View module list;

if (User clicks Install?) then (yes)
  :Install module;
  :Update module status;
  :Enable module features;
else (no)
  if (User clicks Uninstall?) then (yes)
    :Uninstall module;
    :Update module status;
    :Disable module features;
  else (no)
    if (User clicks Upgrade?) then (yes)
      :Check for updates;
      :Run migrations;
      :Update module version;
    endif
  endif
endif

stop

@enduml
```

## Product Management Flow

```plantuml
@startuml Product Management

start
:User accesses /products;

if (Module installed?) then (yes)
  :Check user role;
  
  if (User is Manager?) then (yes)
    :Show CRUD options;
  else (no)
    if (User is Regular User?) then (yes)
      :Show CRU options;
    else (no)
      :Show Read-only options;
    endif
  endif
  
  if (User performs action?) then (yes)
    if (Action is Create?) then (yes)
      :Show create form;
      :Validate input;
      :Save product;
    else (no)
      if (Action is Update?) then (yes)
        :Show update form;
        :Validate input;
        :Update product;
      else (no)
        if (Action is Delete?) then (yes)
          :Show confirmation;
          if (User confirms?) then (yes)
            :Delete product;
          else (no)
            :Cancel delete;
          endif
        else (no)
          :View product;
        endif
      endif
    endif
  endif
else (no)
  :Show 404 error;
endif

stop

@enduml
```

## Authentication Flow

```plantuml
@startuml Authentication

start
:User accesses protected page;

if (User authenticated?) then (no)
  :Redirect to login;
  :Show login form;
  
  if (Valid credentials?) then (yes)
    :Authenticate user;
    :Set session;
    :Redirect to requested page;
  else (no)
    :Show error message;
  endif
else (yes)
  :Check permissions;
  
  if (Has required permission?) then (yes)
    :Allow access;
  else (no)
    :Show access denied;
  endif
endif

stop

@enduml
```

## Process Descriptions

### Module Management
1. User accesses module management page
2. Views list of available modules
3. Can perform actions:
   - Install: Enables module features
   - Uninstall: Disables module features
   - Upgrade: Updates module and runs migrations

### Product Management
1. User accesses product management page
2. System checks:
   - Module installation status
   - User role and permissions
3. Based on role:
   - Manager: Full CRUD access
   - Regular User: Create, Read, Update access
   - Public: Read-only access
4. Actions require confirmation for delete operations

### Authentication
1. User attempts to access protected page
2. System checks authentication status
3. If not authenticated:
   - Redirects to login
   - Validates credentials
   - Sets session on success
4. If authenticated:
   - Checks required permissions
   - Allows or denies access accordingly 