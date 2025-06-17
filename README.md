# Real-Esate-Data-Extractor-for-Kolhapur-Maharashtra

## Workflow
### 1. Inspected Element – Network – All / XHR / Fetch:
1. Monitored what happens in the background when the webpage loads.
2. Spotted API calls that fetch real data (e.g., JSON).
3. These calls are usually under the XHR or Fetch filter.

### 2. Copies or Replays Requests in Postman:
4. Tested the API manually in Postman.
5. Confirmed that this endpoint returns the data we need (e.g. real estate prop datacards .).
6. Copied headers, query parameters, etc., from Postman to mimic the browser.

### 3. Used requests in VS Code:
7. Mimicked the same request programmatically in Python using the requests library.
8. Crafted own GET/POST request, replicated headers/cookies , and parsed the JSON response. 

### 4. Post getting Json response
9. For each url,  extracted raw data from json response which is dictionary or properties information.
10. Created a list from that for all properties and saved it as .pkl for further processing.
11. In next processing used that saved file so that processing happens onj local machine and data is not required to fetch again and again.

### Note: 
1. Data is extracted from magicbricks.com.
2. Data is extracted for residential properties from kolhapur maharashtra only as sample. 