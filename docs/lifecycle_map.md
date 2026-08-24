| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
|---|---|---|---|---|
| Source system |Upstream or "origin the data" | Github repository | Git | Cannot pull through if no appropriate tools/requirements|
| Ingestion/acquisition |Moves the acquired data into a "hub" to confirm successful pull | Pulling the data from the github repository|Vscode cloning from github  |No specific reference repository found |
| Storage |Ingested data is landed here in preparation for transformation|Created local repository in vscode |Vscode/Git |Did not initiate with git init|
| Processing/transformation |Data from the storage is altered or changed |Making the requirements.txt |Python dependencies |incorrect formatting could render the text unreadable in some cases|
| Data quality/validation |Evaluating the overall state and structure of the data being used |Checking for nulls and duplicates |Profile_sources.py |Duplicates can over-inflate the data, comprimising quality. |
| Delivery |An action/command triggers the signal to push data |Pushing the committed data to own repository in Github |Git Push |Cannot push if there is no repository assigned to push into. |
| Consumer |Data flow downstreams or consumed by the users/companies |Finished pipeline ready for checking |Git/Github repository |Overlooking accessibility constraints could render the pipeline as "cannot be viewed" |

Simple Diagram = 

(CSV SOURCE, JSON SOURCE, PARQUET SOURCE, REST API) ------- > A PIPELINE/PROCESS BOX -------> STORAGE/DESTINATION -------> POSTGRE SQL -------> A DOWNSTREAM ANALYST OR APPLICATION CONSUMER