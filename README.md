# Api Docs


# base_Url

```
https://inrapisue.herokuapp.com/

```

# Reception Endpoints

1. Sign Up

```bash
/api/signup/reception/

```

Method : POST



  headers: { 
    'Content-Type': 'application/json'
  },

```

data
```json
{
    "email": "recp@gmail.com",
    "password": "password",
    "profile": {
        "first_name": "recp",
        "last_name": "recp",
        "phone_number": "12333",
        "age": 25,
        "gender": "F"
    }
}

```
2. Sign In

```bash
/api/signin/
```
Method : POST
```json
  headers: { 
    'Content-Type': 'application/json'
  }

  ```


data

```json

{
"email":"recp@gmail.com",
  "password":"password"
}


```

3 . Get Profile

Method : GET
```json
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYjhjN2E5MjMtYjgxMi00ZGY3LWE1NDYtNGQxM2Y3Yzk0ZDlhIiwidXNlcm5hbWUiOiJyZWNwQGdtYWlsLmNvbSIsImV4cCI6MTY1OTU2NjYyNywiZW1haWwiOiJyZWNwQGdtYWlsLmNvbSJ9.zl9mTHxRp6t9mmrSSiotA85pYsURtzLyblwAHvArEq8'
  }
```




```bash



```bash

/api/profile/

```


# Nurse Endpoints

1. Sign Up

```bash
/api/signup/nurse/

```

Method : POST



  headers: { 
    'Content-Type': 'application/json'
  },

```

data
```json

{
    "email": "nurse1@gmail.com",
    "password": "1234",
    "profile": {
        "first_name": "sue",
        "last_name": "nurse",
        "phone_number": "123454",
        "age": 20,
        "gender": "F"
    }
}

```
2. Sign In

```bash
/api/signin/
```
Method : POST
```json
  headers: { 
    'Content-Type': 'application/json'
  }

  ```


data

```json

{
"email":"nurse1@gmail.com",
  "password":"1234"
}

```

3 . Get Profile

Method : GET
```json
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYjhjN2E5MjMtYjgxMi00ZGY3LWE1NDYtNGQxM2Y3Yzk0ZDlhIiwidXNlcm5hbWUiOiJyZWNwQGdtYWlsLmNvbSIsImV4cCI6MTY1OTU2NjYyNywiZW1haWwiOiJyZWNwQGdtYWlsLmNvbSJ9.zl9mTHxRp6t9mmrSSiotA85pYsURtzLyblwAHvArEq8'
  }
```




```bash



```bash

/api/profile/

```

# Lab Tech Endpoints

1. Sign Up

```bash
/api/signup/labtech/

```

Method : POST



  headers: { 
    'Content-Type': 'application/json'
  },

```

data
```json

{
    "email": "lab@gmail.com",
    "password": "password",
    "profile": {
        "first_name": "lab",
        "last_name": "lab",
        "phone_number": "1234589",
        "age": 22,
        "gender": "F"
    }
}
```
2. Sign In

```bash
/api/signin/
```
Method : POST
```json
  headers: { 
    'Content-Type': 'application/json'
  }

  ```


data

```json

{
"email":"lab@gmail.com",
  "password":"password"
}

```

3 . Get Profile

Method : GET
```json
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYjhjN2E5MjMtYjgxMi00ZGY3LWE1NDYtNGQxM2Y3Yzk0ZDlhIiwidXNlcm5hbWUiOiJyZWNwQGdtYWlsLmNvbSIsImV4cCI6MTY1OTU2NjYyNywiZW1haWwiOiJyZWNwQGdtYWlsLmNvbSJ9.zl9mTHxRp6t9mmrSSiotA85pYsURtzLyblwAHvArEq8'
  }
```




```bash



```bash

/api/profile/

```


# Doctor Endpoints

1. Sign Up

```bash
/api/signup/doctor/

```

Method : POST



  headers: { 
    'Content-Type': 'application/json'
  },

```

data
```json

{
    "email": "doc@gmail.com",
    "password": "12345",
    "profile": {
        "first_name": "Sue",
        "last_name": "doc",
        "phone_number": "1234567",
        "age": 32,
        "gender": "M"
    }
}
```
2. Sign In

```bash
/api/signin/
```
Method : POST
```json
  headers: { 
    'Content-Type': 'application/json'
  }

  ```


data

```json

{
"email":"doc@gmail.com",
  "password":"12345"
}
```

3 . Get Profile

Method : GET
```json
  headers: { 
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYjhjN2E5MjMtYjgxMi00ZGY3LWE1NDYtNGQxM2Y3Yzk0ZDlhIiwidXNlcm5hbWUiOiJyZWNwQGdtYWlsLmNvbSIsImV4cCI6MTY1OTU2NjYyNywiZW1haWwiOiJyZWNwQGdtYWlsLmNvbSJ9.zl9mTHxRp6t9mmrSSiotA85pYsURtzLyblwAHvArEq8'
  }
```




```bash



```bash

/api/profile/

```







# Set up Url variable to your host domain 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/19768686-849ce952-e76f-4cf6-956e-a4da51dff802?action=collection%2Ffork&collection-url=entityId%3D19768686-849ce952-e76f-4cf6-956e-a4da51dff802%26entityType%3Dcollection%26workspaceId%3D3da59e20-ddaf-4c49-928a-2bfd5af8aee7)