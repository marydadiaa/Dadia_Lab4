<h1>Laboratory Activity #4: Advanced API Implementation </h1>

<h3>Objectives: </h3>
- Implement versioning, authentication, and proper HTTP exception handling in developing API
- Implement best practices in handling environment variables 

<h3>Instructions: </h3>
1. Following the instructions on Laboratory Activity #2, implement the same endpoints in a new version. Name the first version `apiv1` and new version `apiv2`

2. Implement HTTP exception for the following:
- If accessing a task that is not in the list (404)
- If delete a task that is not in the list (404)
- If updating a task that is not in the list (404)

Additionally, add the appropriate status code for the following
- If task is added (201)
- If task is updated (204)
- If task is deleted (204)
- If there is no tasks (204)

For the general status code of other cases that are not specified, use 200.

<h3>Importance: </h3>
<h3>Scalability </h3>
Versioning helps manage changes to your API as it grows and new features are added. By supporting multiple versions of an API, you can provide stable access to older users while rolling out new changes to others.

<h3>Security </h3>
Authentication is crucial for protecting your API. By implementing authentication mechanisms (like API keys or JWT tokens), you ensure that only authorized users can access or modify resources, safeguarding sensitive information.

<h3>User Experience </h3>
Proper error handling and clear HTTP exceptions ensure that users and developers interacting with your API receive useful feedback. This helps them understand and handle errors in their applications more effectively.

<h3>Steps: </h3>
1. Installing dependencies like, ("pip install -r requirements.txt"). <br>
2. Create .env file for storing the API KEY, ("API_KEY=your-secret-api-key"). <br>
3. Run the API using, ("uvicorn main:app --reload"). <br>
4. Perform the GET command POST, PATCH, DELETE. It has two version which is the "apiv1" and "apiv2". Each command requires an authentication using your own valid API KEY.<br>
<br>
- GET /apiv1/tasks/1 <br>
- POST /apiv1/tasks <br>
- PATCH /apiv1/tasks/1 <br>
- DELETE /apiv1/tasks/1

