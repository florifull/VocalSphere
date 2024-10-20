# VocalSphere

## Getting Started

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/<your-username>/social_media_app.git
```

Replace `<your-username>` with your GitHub username.

### Step 2: Set Up the Backend

1. **Navigate to the Backend Directory**:
   ```bash
   cd social_media_app/backend
   ```

2. **Create and Activate the Virtual Environment**:
   ```bash
   python -m venv venv
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   .\venv\Scripts\activate
   ```

3. **Install Backend Dependencies**:
   After setting up your virtual environment, you can install all the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the .env File**:
   - Create a `.env` file in the `backend` directory.

   - **Obtain Your MongoDB URI**:
     - **Contact Khang**: To access the MongoDB cluster, please contact Khang (your username or email) to receive an invitation to the cluster and the relevant connection details.
     - Once you receive the invite, go to your [MongoDB Atlas](https://cloud.mongodb.com/) account and navigate to your cluster named **VocalSphere**.
     - Click on the **"Connect"** button.
     - Follow the instructions given (select the option to connect your application).
     - Copy the connection string provided; this is your URI. It should look something like this:
       ```plaintext
       mongodb+srv://<username>:<password>@vocalsphere.4hio8.mongodb.net/social_media_app?retryWrites=true&w=majority&appName=VocalSphere
       ```
     - Replace `<username>` and `<password>` in the URI with your MongoDB username and password.

   - The `.env` file should look like this:
   ```plaintext
   MONGO_URI=mongodb+srv://<username>:<password>@vocalsphere.4hio8.mongodb.net/social_media_app?retryWrites=true&w=majority&appName=VocalSphere
   JWT_SECRET_KEY=my_super_secret_key
   ```
   Make sure to replace `<username>` and `<password>` with your actual MongoDB user details.

### Step 3: Set Up the Frontend

1. **Open a New Terminal Window** (do not close the backend server terminal).

2. **Navigate to the Frontend Directory**:
   ```bash
   cd social_media_app/frontend
   ```

3. **Install Frontend Dependencies**:
   ```bash
   npm install
   ```

4. **Create the .env File** (if you need to add any environment variables):
   - Create a `.env` file in the `frontend` directory to store environment variables. For example:
   ```plaintext
   REACT_APP_API_URL=http://localhost:5000/api
   ```

## Notes

- If you encounter any issues during setup, make sure to check that your Python and Node.js versions are compatible and that you have the correct MongoDB connection string.
- Any sensitive data should be stored in the `.env` files and should not be committed to the repository.

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes!

## License

This project is licensed under the MIT License.