# Cloud-based File Storage System Deployment

## Description
This project sets up a Nextcloud instance using Docker and performs load testing using Locust. Nextcloud is a self-hosted file sharing and collaboration platform, and Locust is an open-source load testing tool.

## Usage
1. Clone this repository.
2. Install Docker on your system.
3. Navigate to the project directory.
4. Run the following command to start the Nextcloud instance and Locust load testing:

    ```bash
    sudo docker-compose up -d
    ```

5. Access Nextcloud via your web browser at `http://localhost:8080`.
6. Access Locust's web interface for load testing at `http://localhost:8089`.
7. Customize Locust's test scenarios by editing `locust/locustfile.py`.
8. Monitor load testing results through Locust's web interface.

## Configuration
- `docker-compose.yml`: Defines services for Nextcloud and Locust, along with their configurations
  - Nextcloud service:
    - Uses the latest Nextcloud Docker image
    - Exposes Nextcloud on port 8080
    - Sets environment variables for Nextcloud admin username, password, SQLite database name, and database directory
    - Mounts a volume for Nextcloud data persistence
    - common network nextcloud_network for container instances
  - Locust service:
    - Uses the Locust Docker image
    - Exposes Locust's web interface on port 8089
    - Specifies command-line arguments to run Locust with custom test scenarios and target host.
    - Mounts volumes for Locust test scripts and data
    - common network nextcloud_network for container instances
  - Cleanup service:
    - Uses the latest Alpine Docker image
    - cleans up periodically heavy trashbins and file versions files created with locust tests
    - Mounts a volume for script  persistence
    - common network nextcloud_network for container instances
  - Db service:
    - Uses the Mariadb Docker image
    - Used as the database backend for Nextcloud, storing user data, metadata, and application settings. 
    - Mounts volumes for db scripts and data
    - common network nextcloud_network for container instances  


## Files
- `docker-compose.yml`: Docker Compose configuration file
- `locust/locustfile.py`: Python script defining Locust test scenarios
- `create_users.sh`: Users creattion for 1-30 for nextcloud
- `cleanup.sh`: monitors the space usage inside nextcloud container and cleans up periodically heavy trashbins and file versions files created with locust tests.
- `create_testfiles.py`: test data  creation for 1kb,1mb,5mb for locust tests.Ensure the test files are created before running Locust.
- `testdata`: folder to contain images of locus tests performed


## Author
Vishal Nigam

University of Trieste

