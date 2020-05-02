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

<table border="1" class="docutils" id="id13">
    <colgroup>
        <col width="50%">
        <col width="50%">
    </colgroup>
    <thead valign="bottom">
        <tr class="row-odd">
            <th class="head">Endpoint</th>
            <th class="head">Description</th>
        </tr>
    </thead>
    <tbody valign="top">
        <tr class="row-even">
            <td colspan=2><strong>Authentication</strong></td>
        </tr>
        <tr class="row-odd">
            <td>/api/auth/token</td>
            <td>Login with username, password and Generate access token</td>
        </tr>
        <tr class="row-odd">
            <td>/api/auth/token</td>
            <td>Refresh access token</td>
        </tr>
        <tr class="row-even">
            <td colspan=2><strong>User</strong></td>
        </tr>
        <tr class="row-even">
            <td>/api/users</td>
            <td>List all users</td>
        </tr>
        <tr class="row-even">
            <td>/api/users/{id}</td>
            <td>Get, Update, Delete a user by id</td>
        </tr>
        <tr class="row-even">
            <td>/api/users/{id}/profile</td>
            <td>Get, Update, Delete a user's profile by id</td>
        </tr>
    </tbody>
</table>

## Testing API with Swagger

![Swagger UI for interact with RESTful API](/img/swagger-ui-1.png)




