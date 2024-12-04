# hello-azure-ai-foundry-py

## HISTORY

### Part 1: Setup project and install SDK

[Part 1: Setup project and install SDK](https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-create-resources?tabs=linux#prerequisites)

#### Create an Azure AI Foundry

To create a project in Azure AI Foundry, follow these steps:

1. Go to the Home page of Azure AI Foundry.
1. Select + Create project.
1. Enter a name for the project. Keep all the other settings as default.
1. Projects are created in hubs. For this tutorial, create a new hub. If you see Create a new hub select it and specify a name. Then select Next. (If you don't see Create new hub, it's because a new one is being created for you.)
1. Select Customize to specify properties of the hub.
1. Use any values you want, except for Region. We recommend you use either East US2 or Sweden Central for the region for this tutorial series.
1. Select Next.
1. Select Create project.

#### Deploy models

- `gpt-4o-mini`
- `text-embedding-ada-002`

#### Create an Azure AI Search service

1. Create an Azure AI Search service in the Azure portal.
1. Select your resource group and instance details. You can see details about pricing and pricing tiers on this page.
1. Continue through the wizard and select Review + assign to create the resource.
1. Confirm the details of your Azure AI Search service, including estimated cost.
1. Select Create to create the Azure AI Search service.

#### Connect the Azure AI Search to your project

1. In Azure AI Foundry, go to your project and select Management center from the left pane.
1. In the Connected resources section, look to see if you have a connection of type Azure AI Search.
1. If you have an Azure AI Search connection, you can skip ahead to the next section.
1. Otherwise, select New connection and then Azure AI Search.
1. Find your Azure AI Search service in the options and select Add connection.
1. Use API key for Authentication.

#### Install the Azure CLI and sign in

See [`InstallAZCLIDeb.ba.sh`](./scripts/az/InstallAZCLIDeb.ba.sh)

#### Create a new Python environment

Set `.venv`

#### Install packages

See `requirements[.variant].txt` files

#### Create helper script

[See `config.py`](./src/utils/config.py)

#### Configure environment variables

Copy+paste `.env.sample` as `.env` file

### Part 2 - Build a custom knowledge retrieval (RAG) app with the Azure AI Foundry SDK

#### Create example data for your chat app

[See `products.csv`](./assets/products.csv)

#### Create a search index

[See `search.py`](./src/ai/search.py)
