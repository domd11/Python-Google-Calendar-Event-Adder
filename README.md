# Python-Google-Calendar-Event-Adder

This python script utilizes the Google Calendar API to generate events within your calendar. Originally created with the "calendar" module, I personally employ it as a student to incorporate my assignments into my schedule. It can be adapted to suit various purposes, but it's crucial to follow the necessary steps for establishing a service account on the Google Cloud Console.


## Steps for creating service account on google cloud console: 

Go to the Google Cloud Console and select your project.

Go to the "IAM & Admin" page from the left sidebar.

Click on "Service Accounts".

Click on the "Create Service Account" button.

Enter a name and optional description for the service account, then click "Create".

Under "Service Account Permissions", add the necessary permissions for your service account. For example, if you want to access the Google Calendar API, add the "Calendar API" role to your service account.

Under "Grant users access to this service account", you can add any users or groups who should have access to the service account. If you want to use the service account from your own code, you can skip this step.

Click "Done" to create the service account.

Click "Manage service accounts"

Click the 3 dots under the Actions column for the servce account

Click "Manage Keys"

Click Add Key

Select Create New Key

Select "JSON" as the key type and click "Create". This will download a JSON file containing the credentials for your service account.
