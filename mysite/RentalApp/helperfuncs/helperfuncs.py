colours =  ['#ffbebe', '#dcffbe', '#bec7ff', '#ff4141', '#8dff41', '#4180ff',
				'#8e3924', '#248e5c', '#79248e', '#24558e', '#808e24', '#b341ff',
				'#41ffff', '#ffcc41', '#f6beff', '#beffe9', '#ffe9be', '#dfa152'
                ]

def chartJSData(querySet, columnName, chartType="pie", maxLabels=999):
    """
    Takes queryset data and organizes it into chart js data format.
    Will only work on simple count queries
    
    querySet   - querySet - set of records from database
    columnName - string   - name of the column of querySet to use as labels
    chartType  - string   - type of chart.js chart
    maxLabels  - int      - maximum labels to display - defaults to 999
    """
    
    data = {
        'type': chartType,
        'data': {
            'labels': list(querySet.values_list(columnName, flat=True))[:maxLabels],
            'datasets': [{
                'data': list(querySet.values_list("total", flat=True))[:maxLabels],
                'backgroundColor': colours
            }]
        }
    }
    
    return data  
    
def chartJSData_dict(dict, chartType="pie", maxLabels=999):
    """
    Takes dict and organizes it into chart js data format.
    Will only work on simple count queries
    
    dict       - dict     - a python dictionary
    chartType  - string   - type of chart.js chart
    maxLabels  - int      - maximum labels to display - defaults to 999
    """
    
    data = {
        'type': chartType,
        'data': {
            'labels': list(dict.keys()),
            'datasets': [{
                'data': list(dict.values()),
                'backgroundColor': colours
            }]
        }
    }
    
    return data
    
def chartJSData_bracket(dataSource, columnName, start=0, increment=1, bracketCount = 999):
    """
    Takes a datasource, columnName, and bracket values
    Will only work on simple count queries
    
    dataSource   - django thing - must be data source of format Car.objects.all()
    columnName   - string   - the column to filter over
    start        - int      - starting value for brackets
    increment    - int      - range of each bracket
    bracketCount - int      - how many brackets to record
    """
    ranges = []
    for i in range(0, bracketCount):
        ranges.append((start + i*increment, (start-1) + (i+1)*increment))
        
    
    # Fill price dict manually 
    dict = {}
    
    for i in range(0, bracketCount):
        count = eval('ds.filter(' + columnName + '__range=(rg[i][0], rg[i][1])).count()', {'i':i, 'ds':dataSource, 'rg':ranges})
        key = str(ranges[i][0]) + '-' + str(ranges[i][1])
        dict[key] = count
    
    # delete empty entries
    for i in range(0, bracketCount):
        key = str(ranges[i][0]) + '-' + str(ranges[i][1])
        if (dict[key] == 0):
            del dict[key]

    data = chartJSData_dict(dict)

    return data