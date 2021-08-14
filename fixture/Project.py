from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
        #if not (wd.current_url.endswith("/manage_proj_create_page.php") and len(wd.find_element_by_xpath("(//input[@value='Add Project'])")) > 0):
            #wd.find_element_by_link_text("My view").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.projects_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_manage_projects_page()
        self.open_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_elements_by_xpath("//*[contains(text(), 'Are you sure you want to delete this project')]")
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.projects_cache = None

    def open_project_by_id(self, id):
        wd = self.app.wd
        for element in wd.find_elements_by_xpath("//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]/."):
            url_with_id = element.find_element_by_xpath("td[1]/a").get_attribute("href")
            actual_id = url_with_id.split('=')[-1]
            if actual_id == id:
                element.find_element_by_xpath("td[1]/a").click()
                break

    projects_cache = None

    def get_projects_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_manage_projects_page()
            self.projects_cache = []
            for element in wd.find_elements_by_xpath("//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]/."):
                name = element.find_element_by_xpath("td[1]").text
                description = element.find_element_by_xpath("td[5]").text
                url_with_id = element.find_element_by_xpath("td[1]/a").get_attribute("href")
                id = url_with_id.split('=')[-1]
                self.projects_cache.append(Project(name=name, id=id, description=description))
        return list(self.projects_cache)

