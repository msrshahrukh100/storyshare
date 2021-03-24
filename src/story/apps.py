from django.apps import AppConfig


class StoryConfig(AppConfig):
    name = 'story'

    def ready(self):
        from story import signals

        _ = signals
