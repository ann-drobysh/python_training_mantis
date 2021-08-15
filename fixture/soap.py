from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_user_projects(self):
        web_config = self.app.config['webadmin']
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list = []
        for i in client.service.mc_projects_get_user_accessible(web_config['username'], web_config['password']):
            projects_list.append(Project(name=i.name, id=i.id))
        return projects_list

