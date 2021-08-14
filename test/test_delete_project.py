from model.project import Project
import random

def test_add_new_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_projects_list()) == 0:
        app.project.create_new_project(Project(name="New project created", description="New description"))
    old_projects_list = app.project.get_projects_list()
    project = random.choice(old_projects_list)
    app.project.delete_project_by_id(project.id)
    new_projects_list = app.project.get_projects_list()
    old_projects_list.remove(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)