# API

## GET /

Returns the web interface.

---

## GET /status

Returns server status.

---

## POST /chat

Input

{
    "message": "Hello"
}

Output

{
    "reply": "Hello!"
}

---

Future Endpoints

POST /chat/stream

POST /voice

POST /memory/search

POST /planner

POST /files/search