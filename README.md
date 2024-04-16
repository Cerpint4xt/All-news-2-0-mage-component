# Mage Component DataTalksClub project  

## All-news-mage-component

This part involves the creation of a two docker containers that will handle the information from the [data source](https://components.one/datasets/all-the-news-2-news-articles-dataset) that was previously uploaded in a repository so it is accesible as a API in the [All-news-repository](https://github.com/Cerpint4xt/All_the_News_2_0_Component_One)

## Hands-On

### Starting the container

If you cloned the [main repository](https://github.com/Cerpint4xt/data-engineering-all-news-project) you will only have to get in to the folder of this module and follow the instructions

1. Navigate to the repo

```bash
cd magic-component-all-news
```

2. Rename/copy the `dev.env` to simply `.env` -- this will _ensure_ the file is not committed to Git by accident, since it will contain credentials in the future.

3. Change the `PROJECT_NAME` if necessary in the `.env` file
4. Run:

```bash
docker compose build
```

To buld the container

5. Run:

```bash
docker compose -p <container-name> up
```

To run the container
Now, navigate to <http://localhost:6789> in the browser of your preference and start running the piplines.

### Running the pipelines

Once started and getting inside Mage UI you can start navigating to two different pipelines.

1. That is the one that handles `author` information from the `dataset`
2. That is the one that handles `article` on the information, holding articles and title information from the `dataset`
You will have something like the following structure.

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
|   |   ├──── all_news_to_gcs_partitioned_article.py
|   |   ├──── all_news_to_gcs_partitioned_author.py
│   ├── data_loaders
|       ├──── load_api_data_article.py
|       ├──── load_api_data_author.py
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
|       ├──── transform_all_news_article.py
|       ├──── transform_all_news_author.py
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```

In order to run the pipelines theres a couple of requiriments.

1. Already setup a project name in the cloud and a bucket name too. <all-news-bucket-project>/<all_news_project-XXXX>

2. Setup a `service_account` in the cloud and upload/update it to the docker container and change the `io_config.yaml` as explained in the de-zoomcamp videos.

3. In each pipeline you can change the months and year your want to cover in the run. (Due to a limitation with my local environment, I only have 15Gb of memory available, had to run the pipeline many times to cover one year each run.) Changing the following in the data_loader

```python
months = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12]
years = [2020] #, 2017, 2018, 2019, 2020]
```

4. In the data_exporter files update the name of the project and bucket in order to ingest the data to the cloud.

5. Check that the data has been uploaded to the bucket.

### Details

Both of the pipelines have a trigger setup in code in order to update the data daily.
There are Terraform files in the main repository to deploy the Mage component but it has no version control configuration. So, a workaround for this matter should be to manually copy the pipelines into the Terraform deployment.
