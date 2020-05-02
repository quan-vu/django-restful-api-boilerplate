# Restful API Boilerplate

A Boilerplate for quickstart a Restful API use Django Rest Framework.

## Features

- User Register and Login
- User Permission and Authorization
- User Profile Managemment
- Support Javascript Web Token Authentication
- Support Role Base Access Control (RBAC)
- Support Docker

## Technologies

- Python (3.6+)
- Django (3.0.5)
- Swagger UI

## API Endpoints

<table class="table table-bordered">
    <colgroup>
        <col width="40%">
        <col width="60%">
    </colgroup>
    <thead valign="bottom" class="thead-light">
        <tr>
            <th>Endpoint</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody valign="top">
        <tr>
            <td colspan=2><strong>Authentication</strong></td>
        </tr>
        <tr>
            <td>/api/auth/token</td>
            <td>Login with username, password and Generate access token</td>
        </tr>
        <tr>
            <td>/api/auth/token</td>
            <td>Refresh access token</td>
        </tr>
        <tr>
            <td colspan=2><strong>User</strong></td>
        </tr>
        <tr>
            <td>/api/users</td>
            <td>List all users</td>
        </tr>
        <tr>
            <td>/api/users/{id}</td>
            <td>Get, Update, Delete a user by id</td>
        </tr>
        <tr>
            <td>/api/users/{id}/profile</td>
            <td>Get, Update, Delete a user's profile by id</td>
        </tr>
    </tbody>
</table>

## Testing API with Swagger

![Swagger UI for interact with RESTful API](/img/swagger-ui-1.png)




