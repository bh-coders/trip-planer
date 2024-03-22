# Trip Planer
Mobile, Web and Rest API

## Resources and Links

- **Google Docs**: Access our project documentation on Google Docs. [View Document](https://docs.google.com/document/d/1IqmiUzFOp4TbW4GeCk5t_hnSfs0YkB154wvZao-6htY))

- **pgAdmin**: Manage and interact with our databases through pgAdmin. Access it [here](http://51.83.130.148:5002/login).

- **API Endpoint**: Utilize our REST API by connecting to [this endpoint](http://51.83.130.148:8081/).

- **API Documentation**: For detailed information about API usage and endpoints, visit our [API Documentation](http://51.83.130.148:8081/docs).

- **Web Interface** (In Progress): The web interface is currently under development. (Link will be provided when available)

# Development

## 1. Backend 
### Configuration

In our project, we use a configuration file that loads environment variables. This allows us to interact with them. The configuration file is located at:

```bash
src/web/core/configs.py
```

### Initializing Environment Variables
We can initialize environment variables using the `EXPORT` command or by creating a .env file based on the .env.template.

##### Example of initializing an environment variable:

```bash
export POSTGRES_HOST=jp2
```

#####  The .env File
To create a .env file, copy the .env.template and fill in the values:
```bash
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=

MINIO_HOST_URL=
MINIO_ACCESS_KEY=
MINIO_SECRET_KEY=
MINIO_SECURE=
```

### Start application
There are two methods to start our application:

#### 1. Using Uvicorn:
    
To start the application with Uvicorn, use the following command:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 80 --reload
```
#### 2. Using Docker-compose

Ensure you are in the root directory (e.g., trip-planner). Docker Compose can be used for rebuilding and launching the application. Execute the command below:
```bash 
docker-compose up -d --build
```


## 2. Frontend 

To run the frontend in a developer environment, you should install the following:

**For web:**
- Node.js (Specify the version according to your OS)
- React Native: `npm install react-native`

**For Android:**
All the requirements mentioned for the web, and additionally:
- Android Studio
- Android SDK
- Create an Android emulator

**For iOS:**
- Xcode: This is the IDE for iOS development. Install the latest version from the Mac App Store. Ensure your Mac is updated to a compatible OS version as required by Xcode.

To start, run the following command:
```bash
npm start
```
Then, choose the desired option from the Expo menu.

If cannot find android SDK
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

If you have error with local.properties:

android/local.properties
```bash

sdk.dir = /Users/<your_name>/Library/Android/sdk
```


