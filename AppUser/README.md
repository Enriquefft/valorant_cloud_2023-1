# App users

Rest API for managing application users

## Get all users

`GET /usuarios`

### Returns

    [
    {
        id: str,
        usuario: str,
        contrasena: str,
        correo: str,
        edad: str,
        sexo: str
    }, ...
    ]


## Create new user

`POST /usuarios`

### Arguments

    FormData object with the following fields:

    - usuario: str
    - contrasena: str
    - correo: str
    - edad: str
    - sexo: str

## Get data of a specific user

`GET /usuario/{usuario}`

### Returns

    {
        id: str,
        usuario: str,
        contrasena: str,
        correo: str,
        edad: str,
        sexo: str
    }

## Update data of a specific user

`PUT /usuario/{usuario}`

### Arguments

    FormData object with the following fields:

    - usuario: str
    - contrasena: str
    - correo: str
    - edad: str
    - sexo: str
    
## Delete a specific user

`DELETE /usuario/{usuario}`
