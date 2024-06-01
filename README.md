# Faker-data
This project is a simple API that has different endpoints that allow us to consume random data such as temperatures,
network connections, etc.

## Get Started

### 1. Source Code

    pip install -r requirements
    cd api & flask run -p 8080

### 2. Docker Image

    docker pull rghcr.io/elskater98/fake-data
    docker run -it --rm -p 8080:8080 rghcr.io/elskater98/fake-data

## Endpoints

### [GET] generate/time-series/temperature

**RESPONSE**

    { 
        "collect_dt": "2024-06-01 21:09:55",
        "value": 13.958027224129026
    },
    {
        "collect_dt": "2024-06-01 21:10:00",
        "value": 16.07785986202289
    },
    {
        "collect_dt": "2024-06-01 21:10:05",
        "value": 24.735720654579758
    },
    {
        "collect_dt": "2024-06-01 21:10:10",
        "value": 6.517568254544638
    },
    {
        "collect_dt": "2024-06-01 21:10:15",
        "value": 28.623424149058135
    }

### [GET] generate/time-series/network-traffic

**RESPONSE**

    {
        "collect_dt": "2024-04-05 06:29:30",
        "ip_address": "79.118.165.163",
        "lat": "-59.807033",
        "long": "116.667229"
    },
    {
        "collect_dt": "2024-05-14 06:24:23",
        "ip_address": "155.221.242.216",
        "lat": "-28.212631",
        "long": "-109.271807"
    },
    {
        "collect_dt": "2024-03-12 10:41:20",
        "ip_address": "56.24.43.96",
        "lat": "87.517305",
        "long": "-120.644543"
    },
    {
        "collect_dt": "2024-04-08 12:10:31",
        "ip_address": "67.31.230.135",
        "lat": "67.4960095",
        "long": "-36.332288"
    }

### [GET] generate/time-series/calls

**RESPONSE**

    {
        "collect_dt": "2024-06-01 06:57:51",
        "dest": "(789)589-0677x452",
        "origin": "(345)333-4071x37091"
    },
    {
        "collect_dt": "2024-06-01 11:04:13",
        "dest": "374-606-1581x577",
        "origin": "801.515.2282x7174"
    },
    {
        "collect_dt": "2024-06-01 20:13:53",
        "dest": "(389)572-2370",
        "origin": "328.467.4208x7238"
    },
    {
        "collect_dt": "2024-05-31 13:09:43",
        "dest": "563.942.8558x8731",
        "origin": "+1-401-906-9076x96204"
    }

### [GET] generate/person

**RESPONSE**

    {
        "address": "Unit 1154 Box 8871\nDPO AP 70248",
        "birthdate": "Fri, 22 Sep 1911 00:00:00 GMT",
        "blood_group": "AB+",
        "company": "Ramirez-Williams",
        "current_location": [
            "34.134364",
            "49.816246"
        ],
        "job": "Health and safety inspector",
        "mail": "qriley@gmail.com",
        "name": "Daniel Mcdaniel",
        "residence": "PSC 2948, Box 3610\nAPO AP 81529",
        "sex": "M",
        "ssn": "882-94-0150",
        "username": "grahamanita",
        "website": [
            "https://www.moore.com/",
            "https://stewart-lamb.com/",
            "http://weiss.net/"
        ]
    }


