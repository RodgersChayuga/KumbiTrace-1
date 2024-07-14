# KumbiTrace

KumbiTrace is a citizen-centered and citizen-driven Missing Persons platform designed to address the increasing incidents of enforced disappearances, armed abductions, and the discovery of bodies in various parts of Kenya.

## Features

- **Reporting Missing Persons:** Easily report and register missing persons.
- **Email Alerts:** Receive notifications about missing persons and updates.
- **Social Media Integration:** Share missing persons reports on social media platforms.
- **Search and Filter:** Quickly find missing persons based on various criteria.
- **Data Security and Privacy:** Ensuring the safety and confidentiality of user data.
- **Community Involvement:** Engage the community in searching and reporting.
- **Interactive Map:** Visual representation of missing persons' last seen locations.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Git
- A web browser

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/KumbiTrace.git
    cd KumbiTrace
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file for environment variables:**

    ```bash
    touch .env
    ```

    Add your environment variables to the `.env` file. For example:

    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

5. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:8000/
    ```

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.