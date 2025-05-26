# Tracker



**"Where Are My People?"** is a real-time tracking system for workers and their SOS devices. It manages users, their assigned devices and collects location pings sent by active devices.

---

## Setup Instructions

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # Windows PowerShell
   source .venv/bin/activate       # Linux/macOS
    ```
   
2. Install dependencies:

   ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
   
3. Run migrations:

   ```bash
    python manage.py migrate
    ```

4. Run the development server:

   ```bash
    python manage.py runserver
    ```
5. Open browser and visit:
   ```plaintext
    http://127.0.0.1:8000/api/
    ```

## API Endpoints

| Method | Endpoint               | Description                                        |
|--------|------------------------|--------------------------------------------------|
| POST   | `/devices/{id}/assign/`   | Assign a device to a user and activate it       |
| POST   | `/devices/{id}/location/` | Send a location ping from an active device      |
| GET    | `/users/{id}/location/`   | Get the last known location of a user          |
| GET    | `/map/`                   | Get latest locations of all currently assigned devices. Supports filtering by query parameters: `device_id`, `user_id` |     |
| GET    | `/devices/`               | List all devices with their assignment status          |
| POST   | `/devices/{id}/unassign/` | Unassign and deactivate a device                  |



### **If I had more time, I would...**
- Add automated tests (unit and integration tests)
- Implement user authentication and authorization
- Enhance the API documentation
- Introduce rate limiting to prevent spam
- Improve error handling with more detailed messages
- Deploy the app with a CI/CD pipeline and containerization for production

### Q&A  
**How would you prevent location spam?**

To prevent location spam on the backend, I would implement rate limiting to restrict how frequently a device can send location pings. For example, if a device starts sending pings every second instead of every few minutes, the server would reject or throttle requests exceeding the allowed frequency. Additionally, I could implement monitoring and alerting to detect abnormal patterns and temporarily block or flag suspicious devices. This ensures efficient use of resources and reliable location data.


