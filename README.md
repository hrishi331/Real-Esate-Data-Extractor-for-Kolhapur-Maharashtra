# Real-Esate-Data-Extractor-for-Kolhapur-Maharashtra

## Workflow
### 1. Inspected Element – Network – All / XHR / Fetch:
Monitored what happens in the background when the webpage loads.
Spotted API calls that fetch real data (e.g., JSON).
These calls are usually under the XHR or Fetch filter.

### 2. Copies or Replays Requests in Postman:
Tested the API manually in Postman.
Confirmed that this endpoint returns the data we need (e.g. real estate prop datacards .).
Copied headers, query parameters, etc., from Postman to mimic the browser.

### 3. Used requests in VS Code:
Mimicked the same request programmatically in Python using the requests library.
Crafted own GET/POST request, replicated headers/cookies , and parsed the JSON response. 

### 4. Post getting Json response
For each url,  extracted raw data from json response which is dictionary or properties information.
Created a list from that for all properties and saved it as .pkl for further processing.
In next processing used that saved file so that processing happens onj local machine and data is not required to fetch again and again.

### Note: 
Data is extracted from magicbricks.com.
Data is extracted for residential properties from kolhapur maharashtra only as sample. 