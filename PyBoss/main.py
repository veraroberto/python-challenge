import os
import csv

resources_file = os.path.join("employee_data.csv")
output_path = os.path.join("employee_data_converted.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    with open(resources_file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        #HEADER
        csv_header = next(csvfile)
        #print(csv_header)


        for row in csv_reader:
            #Split the names
            split_colum = row[1].split(" ")
            row[1] = split_colum[0]
            row.insert(2,split_colum[1])

            #Date
            split_date = row[3].split("-")
            #Before YYYY-MM-DD
            row[3] = split_date[1] + "/" + split_date[2] + "/" + split_date[0]    
            
            #SNN
            split_SNN = row[4].split("-")
            row[4] = "***-**-" + split_SNN[2]
            
            #State
            row[5] = us_state_abbrev[row[5]]

            #Write the File
            csvwriter.writerow(row)



    
        
    
    