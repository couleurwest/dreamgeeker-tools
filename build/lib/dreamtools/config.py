


class CConfig:

    def __init__(self, project_name = None, mode="PRODUCTION"):
        """
        Configuration des parametres d'accès relatif au projet en cours
        ==============================================================

        Parametres
        -----------
        :param str app: Nom de l'application
        :param str[PROD|DEV] mode: PRDO ou DEV

        """
        import os
        from . import tools
        from . import tracker
        from dreamtools import profiler

        from dotenv import load_dotenv

        tools.APP_NAME = os.getenv('PROJECT_NAME', project_name)
        tools.PROJECT_DIR = profiler.dirproject(__file__)
        tools.APP_DIR = profiler.path_build(tools.PROJECT_DIR, tools.APP_NAME)
        tools.TMP_DIR = profiler.path_build(tools.PROJECT_DIR, 'tmp')

        load_dotenv(profiler.path_build(tools.PROJECT_DIR, '.env'))

        tracker.config(os.getenv('MODE', mode))