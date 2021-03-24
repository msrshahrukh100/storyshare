# Share a story

The project is live at http://3.10.227.218

### How to run the project

1. Clone the repository to your system
2. Run the command `docker-compose up`

Pre-requisistes - You must have **docker** and **docker compose** installed on your system.

### API endpoints

1. `/api/story/` is the endpoint to get all the stories and create a new story. A **GET** call to `/api/story/` gives all the stories and a post call to `/api/story/` creates a new story
2. To get the details of the story use `/api/story/<story_id>`

### Using the Project

1. Create a new story at `/api/story/` or use `/api/story/` to get list of all stories.
2. Use the admin at http://3.10.227.218/admin creadentials - root:root
3. View running background tasks at http://3.10.227.218/admin/background_task/task/


### Response format of the API

Note that the JSON reponse of this endpoint gives the process image and video links.

Sample JSON reponse 

```
    {
        "grapher_username": "root",
        "image": "http://localhost/media/images/storyimage/Peach_Circle_Wedding_Logo.png",
        "name": "The name for your story",
        "text": "Some sample text",
        "preprocessing_done": true,
        "video": "http://localhost/media/4K_Amazing_Nature_-_Samsung_Urtra_HD_Sample_Video_60fps_2160p_sPcVmPh.mp4",
        "resized_video": "http://localhost/media/4K_Amazing_Nature_-_Samsung_Urtra_HD_Sample_Video_60fps_2160p_resized.mp4"
    }

```

**grapher_username**  - The username of the user for this story.

**image** - Gives the url of the original image until the preprocessing is done. After preprocessing the reduced image file url is returned.

**name** **text** - Fields for name and text

**preprocessing_done** - Set to true after task for preprocessing is complete

**video**  **resized_video**  - Original and resized_video image url


### Project explanation

1. The story django app is used to store and manage the story details. 
2. The handler function is there in the usual https://github.com/msrshahrukh100/storyshare/blob/main/src/story/views.py file
3. Post save signal is used to call the preprocessing tasks.
4. The preprocessing task preprocesses both the image and video one by one.
5. The image processing is done via Python Image Library.
6. The video preprocessing is done via the third-party app django video encoding.
7. For the tasks django background tasks app is used. For more robust use cases celery can be used.



### Tech Stack

1. Python-Django
2. Django Rest Framework
3. Docker for containarization
4. Deployed on Amazon LightSail








