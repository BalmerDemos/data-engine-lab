### data-engine-lab

#### Introduction: Why Docker Images Are Useful
Docker images have revolutionized the way developers build, ship, and run applications. They enable us to package applications along with all their dependencies into a portable container. This ensures consistency across different environments, reduces compatibility issues, and simplifies deployment. With two containers created in this project, one container allows access to a Python shell under the exec tab in Docker, and the other container (mongodb-eml) provides a mongosh shell for interacting with MongoDB.


### Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Folder Structure](#folder-structure)
6. [Docker Compose Configuration](#docker-compose-configuration)
7. [Known Issues](#known-issues)
8. [Contributing](#contributing)
9. [License](#license)
10. [Disclaimer](#disclaimer)

---
#### Installation
1. Clone the repository:
   ```bash
   https://github.com/BalmerDemos/data-engine-lab
   ```
2. Navigate to the project directory:
   ```bash
   cd data-engine-lab
   ```
3. Build and start the Docker image:
   ```bash
   docker-compose up --build -d
   ```
4. Stop and remove the containers when finished
   ```bash
   docker-compose down

---


#### Usage
- Launch the Prefect server using Docker Compose:
  ```bash
  docker-compose up
  ```
#### Testing the Containers

1. **data-engine-lab Container**:
   - Open the `exec` tab for the `data-engine-lab` container in Docker.
   - Run the following commands:
     ```bash
     ls
     cd scripts
     python mongo_data.py
     ```
   - **Output**:
     ```plaintext
     Inserted 15 documents into the 'movies' collection.
     ```

2. **mongodb-eml Container**:
   - Open the `exec` tab for the `mongodb-eml` container in Docker.
   - Run the following commands:
     ```bash
     ls
     mongosh
     show dbs
     use movies_data
     show collections
     db.movies.find().count()
     ```
   - **Output**:
     ```plaintext
     15
     ```



#### Features
- Pre-installed Python libraries for data engineering and machine learning:
  - `Flask`, `pandas`, `pymongo`, `pyspark`, `scikit-learn`, etc.
- Prefect flow orchestration support.
- Lightweight base image for faster builds and portability.

#### Folder Structure
```plaintext
/data-engine-lab
 |-- flows            # Prefect workflows
 |-- data             # Data files
 |-- scripts          # Custom scripts
 |-- logs             # Log files
.gitignore            # Excludes unnecessary files from version control
docker-compose.yml    # Defines multi-container setups
Dockerfile            # Docker image definition
README.md             # Project documentation

#### Docker Compose Configuration
The `docker-compose.yml` file simplifies multi-container setups:
```yaml
docker-compose:
version: '3.9'

services:
  data-engine-lab:
    image: data-engine-lab:latest
    container_name: data-engine-lab
    build:
      context: .
    depends_on:
      - mongodb
```

#### Known Issues
- **Dependency conflicts**: Ensure `requirements.txt` lists compatible library versions.
    Ref: Section Dockerfile # Install dependencies in one layer
- **Container persistence**: Data not mapped to a volume will be lost when the container stops.


#### Known Issues
- **Dependency conflicts**: Ensure dependencies listed in the Dockerfile under the installation step are compatible and tested. Ref: Dockerfile section # Install dependencies in one layer.
- **Container persistence**: Data not mapped to a volume will be lost when the container stops.

#### Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and submit a pull request.

# License

MIT License

Copyright (c) 2024 [Developed by Balmer Valencia]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

[Include any conditions you want to impose, or leave this section out for a more permissive license.]

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Contributing
Feel free to clone the repository for your own enhancements or bug fixes! Cloning allows you to create a local copy of the project, where you can experiment and make changes without affecting the original repository. If you're unsure how to clone a repository, you can follow a simple guide on the process

# Disclaimer
Please note that this project is for educational purposes only. Any use of the code or information provided is at your own risk.
--------------------------------------------------------------------------------------------------------------
Hey everyone! To all my amazing peers in the second year at Universidad Autónoma De Occidente, I’m excited to share this project with you! I hope you find it super useful and that it sparks some inspiration for your own work. Let’s learn and grow together!

If you have any questions or need assistance, feel free to reach out. Happy coding!
