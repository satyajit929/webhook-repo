Webhook Integration with GitHub using Flask and MongoDB

This project demonstrates how to set up a Webhook to receive GitHub events using Flask, store the data in MongoDB Atlas, and deploy it on an AWS EC2 instance.

1) Technologies Used :

   a) Python 

   b) MongoDB Atlas

   c) GitHub Webhooks

   d) AWS EC2 Instance

   e) Git & GitHub

2) Project Structure :
   
       webhook-repo/
       ├── main.py              # Flask app to receive GitHub events
       ├── requirements.txt     # Python dependencies
       ├── .github/
       │   └── workflows/
       │       └── webhook.yml  # GitHub Actions workflow

3) Setup Instructions :
   
   1. Clone the Repository -

          git clone https://github.com/your-username/webhook-repo.git
          cd webhook-repo
   2. Install Dependencies -
   
          pip install -r requirements.txt
   3. MongoDB Atlas Setup -
      
      a) Create a MongoDB Atlas account.

      b) Create a cluster and user.

      c) Replace the Mongo URI in app.py:

          uri = "mongodb+srv://<username>:<password>@cluster1.mongodb.net/?retryWrites=true&w=majority"
   4. Run Flask Server :

          python app.py
   5. Deploy to AWS EC2 :

      a) Launch an EC2 instance.

      b) EC2 instance connect.

      c) Install Python and Git.

      d) Clone the repo and run the Flask app.

      e) Open port 5000 or 80 in EC2 security group.

4) Webhook Setup in GitHub

   1. Go to your GitHub repository ➝ Settings ➝ Webhooks ➝ Add Webhook

   2. Payload URL: http://<your-ec2-public-ip>:5000/webhook/receiver

   3. Content type: application/json

   4. Events: Push, Pull Requests (or all)

   5. Click Add Webhook

5) Features

   1. Receives real-time GitHub event data.

   2. Saves event data into MongoDB.

   3. Designed for learning and demonstration purposes.

