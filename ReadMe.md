# ReadMe

## How to Test Cloud Function API

### Test using Postman

#### URL
https://us-central1-logical-app-367922.cloudfunctions.net/function-1 
#### json input
{"url":"https://storage.googleapis.com/cloud_assignment_4_model/six.jpg"}

### Testing using CURL Request

curl -m 70 -X POST https://us-central1-logical-app-367922.cloudfunctions.net/function-1 \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{"url":"https://storage.googleapis.com/cloud_assignment_4_model/six.jpg"}'

## Cloud Bucket Public Access Link
https://console.cloud.google.com/storage/browser/cloud_assignment_4_model;tab=objects?forceOnBucketsSortingFiltering=false&authuser=0&project=logical-app-367922&prefix=&forceOnObjectsSortingFiltering=false

Currently there are 5 hand written images in cloud bucket anyone can be used for testing 




 





