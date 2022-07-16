# apester_project
# Apester Home Assignment
Hi :)
In this home assignment you may choose between developing an ETL with Apache Spark, Pandas or Apache Beam.

### Instructions
There are 2 input files in this assignment, taken at a specific point in time:
1. all_video_advertisers.csv - includes all video advertisers data (including the advertiser "Rubicon") on the last 7 days.
2. rubicon.json - includes only one advertiser - "Rubicon", for both display and video, on the last 7 days.

The second input, "rubicon.json", is more accurate, but sometimes delayed and may not include all up-to-date data.

Required output:
1. Aggregated daily revenue data of all advertisers - by date, advertiser and domain.
2. For each aggregated output record, use the most accurate data available in the input files.
3. Only aggregated video data. Please note that the first input has only video data. The second input needed to be filtered.
4. The output should be saved as a csv file.

#### Notes
- Please note that some of the fields are not written in the same way, but should be clear by the context (if not, don't hesitate to reach out with questions).
- The domain field should not contain "www.", "https://", "http://" and without URI and parameters.
- The first input starts at the 7th row, please ignore the rows before that.
- Please submit the assignment as a GitHub repo.
- Please include instructions for running your code locally (on a laptop, specify Linux/Mac).


#### Output Example
Date	      Advertiser Name	  Domain	                      Revenue
18/04/2022	  33across	          thjjameuspjeplj.com	          3.3333   
18/04/2022	  33across	          quetjs.thjjameuspjeplj.com	  0.0338
18/04/2022	  33across	          attackejthjjanbey.com	          0.4013
18/04/2022	  Rubicon	          sjrijnjunkijs.de	              0.99
18/04/2022	  Rubicon	          shmeep.com	                  41.94
18/04/2022	  Rubicon	          cempjtitiens.wemanswjjkly.com	  0.91
18/04/2022	  Rubicon	          barcawjlt.de	                  0.4
......

24/04/2022	  Rubicon	          kickjr.de	                      49.8831
24/04/2022	  Rubicon	          jupa.njt	                      3.3188

....


### Acceptance Criteria
- The code should work.
- Readable and efficient code.


---
If you have any questions please don't hesitate to reach out.

Good Luck!
