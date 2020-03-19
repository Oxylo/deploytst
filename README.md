# Deploytst
Deployment test Dash App on Azure.


Installation (local)
====================

    $ git clone https://github.com/Oxylo/deploytst.git your_project_name
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt


On localhost:8050 (works!)
==========================

    $ python app.py

with last line: app.run_server(host='0.0.0.0',debug=True, port=8050)


On localhost:8050 with Docker (works!)
======================================

    $ docker build -t dash-azure .
    $ docker run -p 8050:8050 dash-azure


On Azure with Docker (works after fixing port issue below!)
===========================================================

Create Container Registry on Azure (I called it canaryacr) and get its credentials to login:

    $ docker login canaryacr.azurecr.io

Tag and push the image:

    $ docker tag dash-azure canaryacr.azurecr.io/dash-azure:version1
    $ docker push canaryacr.azurecr.io/dash-azure:version1

Create Web App resource on Azure and deploy version1.

Do not forget to configure Azure WebApp to appropriate port (in Azure cloud shell):

    $ az webapp config appsettings set --resource-group CanaryResourceGroup --name cannnnn --settings WEBSITES_PORT=8080




