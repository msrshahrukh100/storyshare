from background_task import background


@background(schedule=5)
def preprocess(story_id):
    print(story_id)