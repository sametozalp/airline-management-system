# Airline Management System API

This project created with Django (DRF). It enables the management of aircraft, flights, and reservations.

## Project Structure

```
airline-management-system/
 > airplanes/
   > airplane_views/
   > serializers/
 > flights/
   > flight_views/
   > serializers/
 > reservations/
   > reservation_views/
   > serializers/
   > mail_service.py # E-mail service (DEPRECATED)
 > core/
 > utils/
 > config/ # Gmail API credentials (DEPRECATED)
```

## Models

### Airplane
- `id`: int
- `tail_number`: str
- `model`: str
- `capacity`: int
- `production_year`: int
- `status`: boolean

### Flight
- `id`: int
- `flight_number`: str
- `departure`: str
- `destination`: str
- `departure_time`: datetime
- `arrival_time`: datetime
- `airplane`: int (fk)

### Reservation
- `id`: int
- `passenger_name`: str
- `passenger_email`: str
- `flight`: int (fk)
- `status`: boolean
- `reservation_code`: str
- `created_at`: datetime

## Setup

- Getting started, you need to configure the email functionality.

Please create file by named '.env' and define it:

```bash
EMAIL_HOST_USER = 'YOUR_EMAIL'
DEFAULT_FROM_EMAIL = 'YOUR_NAME <YOUR_EMAIL>'
EMAIL_HOST_PASSWORD = 'YOUR_PASSWORD'
```

You can use the infos for testing:
```bash
EMAIL_HOST_USER = 'tecnhartstest@gmail.com'
DEFAULT_FROM_EMAIL = 'Technarts Airlines <tecnhartstest@gmail.com>'
EMAIL_HOST_PASSWORD = 'rcvzssqriwuhpmqd'
```

1. **Setup Python:**
   - Python -> 3.11

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Active virtual environment:**
```bash
source .venv/bin/activate
```

4. **Download requirements:**
```bash
pip install -r requirements.txt
```

5. **Run migrations:**
```bash
pythın manage.py makemigrations
python manage.py migrate
```

6. **Run server:**
```bash
python manage.py runserver
```

7. **It's working: http://localhost:8000/

## API Docs

### Swagger UI

The swagger is in below url:
```
http://localhost:8000/swagger/
```

## API Endpoints

### Base URL
```
http://localhost:8000
```

### Airplane API

- Get all airplanes

  **Request:**

  ```bash
  GET http://localhost:8000/airplanes/
  ```

  **Response:**

  ```bash
  [
    {
        "id": 18,
        "tail_number": "TC-NRT",
        "model": "Airbus A320",
        "capacity": 200
    }
  ]
  ```

- Create new airplane

  **Request:**

  ```bash
  POST http://localhost:8000/airplanes/
  Content-Type: application/json
  
  {
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 200,
    "production_year": 2006
  }
  ```

  **Response:**

  ```bash
  POST http://localhost:8000/airplanes/
  Content-Type: application/json
  
  {
    "id": 17,
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 200,
    "production_year": 2006
  }
  ```

- Get details of spesific airplane

  **Request:**

  ```bash
  GET http://localhost:8000/airplanes/{id}
  ```

  **Response:**

  ```bash
  {
    "id": 17,
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 200,
    "production_year": 2006,
    "status": true
  }
  ```

- Update the airplane info

  **Request:**

  ```bash
  PATCH http://localhost:8000/airplanes/{id}
  Content-Type: application/json
  
  {
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 200,
    "production_year": 2006,
    "status": true
  }
  ```

  **Response:**

  ```bash
  {
    "tail_number": "TC-NRT",
    "model": "Airbus A320",
    "capacity": 200,
    "production_year": 2006,
    "status": true
  }
  ```

- Delete airplane

  **Request:**

  ```bash
  DELETE http://localhost:8000/airplanes/{id}
  ```


- Get reservations of spesific airplane

  **Request:**

  ```bash
  GET http://localhost:8000/airplanes/{id}/flights
  ```

  **Response:**

  ```bash
  [
    {
      "id": 18,
      "flight_number": "789654",
      "departure": "Ankara",
      "destination": "Berlin",
      "airplane": {
          "id": 17,
          "tail_number": "TC-NRT",
          "model": "Airbus A320",
          "capacity": 200
      }
    }
  ] 
  ```


### Flight API

- Get all flights

  **Request:**

  ```bash
  GET http://localhost:8000/flights/
  
  # Filtering
  GET http://localhost:8000/flights/?departure=Istanbul
  GET http://localhost:8000/flights/?destination=Ankara
  GET http://localhost:8000/flights/?airplane=1
  GET http://localhost:8000/flights/?departure_time=2026-01-17T10:00:00Z
  GET http://localhost:8000/flights/?arrival_time=2026-01-17T10:00:00Z
  ```

  **Response:**

  ```bash
  [
    {
      "id": 18,
      "flight_number": "789654",
      "departure": "Ankara",
      "destination": "Berlin",
      "airplane": {
          "id": 17,
          "tail_number": "TC-NRT",
          "model": "Airbus A320",
          "capacity": 200
      }
    }
  ]
  ```

- Create new flight

  **Request:**

  ```bash
  POST http://localhost:8000/flights/
  Content-Type: application/json
  
  {
    "flight_number": "987654",
    "departure": "Ankara",
    "destination": "İstanbul",
    "arrival_time": "2026-01-17T19:47:03.143Z",
    "departure_time": "2026-01-17T19:17:03.143Z",
    "airplane": 1
  }
  ```

  **Response:**

  ```bash
  {
    "id": 19,
    "flight_number": "987654",
    "departure": "Ankara",
    "destination": "İstanbul",
    "arrival_time": "2026-01-20T19:47:03.143000Z",
    "departure_time": "2026-01-20T19:17:03.143000Z",
    "airplane": 17
  }
  ```

- Get details of spesific flight

  **Request:**

  ```bash
  GET http://localhost:8000/flights/{id}
  ```

  **Response:**

  ```bash
  {
    "id": 19,
    "airplane": {
        "id": 17,
        "tail_number": "TC-NRT",
        "model": "Airbus A320",
        "capacity": 200,
        "production_year": 2005,
        "status": true
    },
    "flight_number": "987654",
    "departure": "Ankara",
    "destination": "İstanbul",
    "departure_time": "2026-01-20T19:17:03.143000Z",
    "arrival_time": "2026-01-20T19:47:03.143000Z"
  }
  ```

- Update the flight info

  **Request:**

  ```bash
  PATCH http://localhost:8000/flights/{id}
  Content-Type: application/json
  
  {
    "flight_number": "456123",
    "departure": "Ankara",
    "destination": "İzmir",
    "arrival_time": "2026-01-17T19:47:17.599Z",
    "departure_time": "2026-01-17T19:17:17.599Z",
    "airplane": 2
  }
  ```

  **Response**

  ```bash
  {
    "id": 19,
    "flight_number": "456123",
    "departure": "Ankara",
    "destination": "İzmir",
    "arrival_time": "2026-01-21T19:47:17.599000Z",
    "departure_time": "2026-01-21T19:17:17.599000Z",
    "airplane": 17
  }
  ```

- Delete flight

  **Request:**

  ```bash
  DELETE http://localhost:8000/flights/{id}
  ```

- Get reservations of spesific flight

  **Request:**

  ```bash
  GET http://localhost:8000/flights/{id}/reservations
  ```

  **Response:**

  ```bash
  [
    {
        "id": 44,
        "passenger_name": "Samet Özalp",
        "reservation_code": "2BC3E8D6",
        "flight": {
            "id": 19,
            "flight_number": "456123",
            "departure": "Ankara",
            "destination": "İzmir",
            "airplane": {
                "id": 17,
                "tail_number": "TC-NRT",
                "model": "Airbus A320",
                "capacity": 200
            }
        }
    }
  ]
  ```

### Reservation API

- Get all reservations

  **Request:**

  ```bash
  GET http://localhost:8000/reservations/
  ```

  **Response:**

  ```bash
  [
    {
        "id": 44,
        "passenger_name": "Samet Özalp",
        "reservation_code": "2BC3E8D6",
        "flight": {
            "id": 19,
            "flight_number": "456123",
            "departure": "Ankara",
            "destination": "İzmir",
            "airplane": {
                "id": 17,
                "tail_number": "TC-NRT",
                "model": "Airbus A320",
                "capacity": 200
            }
        }
    }
  ]
  ```

- Create new reservation

  **Request:**

  ```bash
  POST http://localhost:8000/reservations/
  Content-Type: application/json
  
  {
    "passenger_name": "Samet Özalp",
    "passenger_email": "sametozalp0056@gmail.com",
    "flight": 1
  }
  ```

  **Response**

  ```bash
  {
    "id": 44,
    "passenger_name": "Samet Özalp",
    "passenger_email": "sametozalp0056@gmail.com",
    "flight": 19
  }
  ```

- Get details of spesific reservaition

  **Request:**

  ```bash
  GET http://localhost:8000/reservations/{id}
  ```

  **Response**

  ```bash
  {
    "id": 44,
    "flight": {
        "id": 19,
        "flight_number": "456123",
        "departure": "Ankara",
        "destination": "İzmir",
        "airplane": {
            "id": 17,
            "tail_number": "TC-NRT",
            "model": "Airbus A320",
            "capacity": 200
        }
    },
    "passenger_name": "Samet Özalp",
    "passenger_email": "sametozalp0056@gmail.com",
    "status": true,
    "created_at": "2026-01-18T20:24:43.269628Z",
    "reservation_code": "2BC3E8D6"
  }
  ```

- Update the resrvation info

  **Request:**

  ```bash
  PATCH http://localhost:8000/reservations/{id}
  Content-Type: application/json
  
  {
    "passenger_name": "string",
    "passenger_email": "user@example.com",
    "flight": 0,
    "status": true
  }
  ```

  **Response**

  ```bash
  {
    "passenger_name": "string",
    "passenger_email": "user@example.com",
    "flight": 19,
    "status": false
  }
  ```

### Extra

- **Admin Panel**: `http://localhost:8000/admin/`
- **Swagger UI**: `http://localhost:8000/swagger/`
- **Api Json**: `http://localhost:8000/swagger.json`
