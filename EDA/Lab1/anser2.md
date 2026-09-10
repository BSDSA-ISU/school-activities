# Stuff

| n |   Column |                  Non Null Count |  Dtype |  
| --- |  ------ |                  -------------- |  -----   |
| 0 |   country_code |            200 non-null |    str |    
| 1 |   country_name |            200 non-null |    str |    
| 2 |   censorship_score |        200 non-null |    int64 |  
| 3 |   threat_level |            200 non-null |    str |    
| 4 |   block_rate |              200 non-null |    float64 |
| 5 |   total_measurements |      200 non-null |    int64 |  
| 6 |   blocked_measurements |    200 non-null |    int64 |  
| 7 |   web_connectivity_tests |  200 non-null |    int64 |  
| 8 |   telegram_tests |          200 non-null |    int64 |  
| 9 |   whatsapp_tests |          200 non-null |    int64 |  
| 10 |  isp_count |               200 non-null |    int64 |  
| 11 |  top_blocking_isps |       200 non-null |    object | 
| 12 |  data_source |             200 non-null |    str |    
| 13 |  last_updated |            200 non-null |    str |    
| 14 |  rank |                    200 non-null |    int64 | 

| Variable | Number of nulls |
|---|---|
| country_code | 0 |
| country_name | 0 |
| censorship_score | 0 |
| threat_level | 0 |
| block_rate | 0 |
| total_measurements | 0 |
| blocked_measurements | 0 |
| web_connectivity_tests | 0 |
| telegram_tests | 0 |
| whatsapp_tests | 0 |
| isp_count | 0 |
| top_blocking_isps | 0 |
| data_source | 0 |
| last_updated | 0 |
| rank | 0 |

| Metric | censorship_score | block_rate | total_measurements | blocked_measurements | web_connectivity_tests |
|---|---|---|---|---|---|
| count | 200.00 | 200.00 | 200.00 | 200.00 | 200.00 |
| mean | 3.90 | 0.04 | 193902.24 | 15764.50 | 180289.88 |
| std | 8.29 | 0.08 | 317353.32 | 54629.13 | 287684.48 |
| min | 0.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| 25% | 0.00 | 0.00 | 6.00 | 0.00 | 0.00 |
| 50% | 0.00 | 0.00 | 61.00 | 0.00 | 0.00 |
| 75% | 4.00 | 0.04 | 315255.75 | 10753.00 | 307590.25 |
| max | 61.00 | 0.61 | 1259865.00 | 541311.00 | 929915.00 |

| Metric | telegram_tests | whatsapp_tests | isp_count | rank |
|---|---|---|---|---|
| count | 200.00 | 200.00 | 200.00 | 200.00 |
| mean | 6774.72 | 6820.98 | 6.68 | 100.50 |
| std | 25078.75 | 25211.09 | 17.00 | 57.88 |
| min | 0.00 | 0.00 | 0.00 | 1.00 |
| 25% | 0.00 | 0.00 | 0.00 | 50.75 |
| 50% | 0.00 | 0.00 | 0.00 | 100.50 |
| 75% | 3266.75 | 3254.75 | 7.00 | 150.25 |
| max | 244253.00 | 242831.00 | 176.00 | 200.00 |