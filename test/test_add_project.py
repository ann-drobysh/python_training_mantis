from model.project import Project

def test_add_new_project(app, data_project):
    app.session.login("administrator", "root")
    old_projects_list = app.project.get_projects_list()
    new_project = data_project
    app.project.create_new_project(new_project)
    new_projects_list = app.project.get_projects_list()
    old_projects_list.append(new_project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)