# Description 
A reusable Django starter project with a clean base (main), and each branch representing a trial feature (e.g. Celery setup, DRF config, Auth0 integration, etc.), which can be cherry-picked or merged into other projects.

## Description of other branches
1. setup-django: Basic Django setup with a clean project structure.
2. github-actions: GitHub Actions CI/CD setup for automated testing and deployment.
    - Add github actions django workflow by clicking on actions tab
    - Added pylint too and setup running pylint on local
    - to setup pylint on local, install from pip then run pylint
    - to make changes that pylint suggest, use black formatter
3. 