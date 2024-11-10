("""import sys
import csv
from csv import reader
with open('googleplaystore.csv', mode='r') as file:
    csv_reader = csv.reader(file)
with open('AppleStore.csv', mode='r') as file:
    csv_reader = csv.reader(file)


import string
def main(input):
    # Load and process datasets here
    # Perform category analysis as per the provided script

    # Return result or filtered data for the category
    result = f"Analysis for category: {input} completed"
    print(result)

if __name__ == "__main__":
    user_category = sys.argv[1]
    main(input)

### The Google Play data set ###
opened_file = open('googleplaystore.csv' ,encoding="utf8",errors="ignore")
read_file = reader(opened_file)
android = list(read_file) ### this converts the readfile into a list list() function read all the line of the readfile and store all the leement in the list 
android_header = android[0] ### refernces colums name later 
android = android[1:] ### so we can work with acutual data rather than meta data 

### The App Store data set ###
opened_file = open('AppleStore.csv ', encoding="utf8",errors="ignore")
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]

def explore_data(dataset,start,end,rows_and_colums=False):### hee false measn the rows wont be printed unless the use call for the rows to be printed 
    dataset_slice=dataset[start:end]
    for row in dataset_slice:
        #print(row)
        #print("\n")
        if rows_and_colums:
           # print("Number of rows",len(dataset))
            print('Number of coulms', len(dataset[0]))
            
duplicate_app=[]
unique_apps=[]
for app in android:
    name=app[0]
    if name in unique_apps:
        duplicate_app.append(name)### adding element in the end of the duplicate empty crate list 
    else:
        unique_apps.append(name)

#print("NUmber of duplicate apps:",len(duplicate_app))
#print("\n")
#print("Number of duplicate_apps:",duplicate_app[:15]) 
del android[10472] 

reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

#print('Expected length:', len(android) - 1181)
#print('Actual length:', len(reviews_max))

android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block

       

###print(ios[813][1])
###print(ios[6731][1])
##print(android_clean[4412][0])
##print(android_clean[7940][0])

def is_english(string):
    
    for character in string:
        if ord(character) > 127:
            return False
    
    return True

#print(is_english('Instagram'))
#print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))

#print(is_english('Docs To Go™ Free Office Suite'))
#print(is_english('Instachat 😜'))
#print(ord('™'))
#print(ord('😜'))

def is_english(string):
    non_ascii=0
    for character in string:
      if ord(character)>127:
        non_ascii +=1
    if non_ascii>3:
       return False
    else :
       return True
    
#print(is_english('Docs To Go™ Free Office Suite'))
#print(is_english('Instachat 😜'))
       
android_final=[]
ios_final=[]

for app in android:
    price=app[7]
    if price == '0':
        android_final.append(app)

for app in ios:
    price=app[4]
    if price=='0.0':
        ios_final.append(app)
    
#print(len(android_final))
#print(len(ios_final))

def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

###display_table(ios_final,-5)
###display_table(android_final,1)
###display_table(android_final,-4)

genres_ios=freq_table(ios_final,-5)
for genre in genres_ios:
    total=0
    len_genre=0
    for app in ios_final:
        genre_app=app[-5]
        if genre_app==genre:
            n_rating=float(app[5])
            total+=n_rating
            len_genre+=1
    avg_n_rating=total/len_genre
    #print(genre,":",avg_n_rating)
    
###for app in ios_final:
    ###if app[-5] == 'Navigation':
       ### print(app[1], ':', app[5])
for app in ios_final:
    if app[-5]=="References":
        print(app[1],":",app[5])

display_table(android_final,5)

categories_android=freq_table(android_final,1)
for category in categories_android:
    total=0
    len_category=0
    for app in android_final:
        category_app=app[1]
        if category_app==category:
            n_installs=app[5]
            n_installs=n_installs.replace(",","")
            n_installs=n_installs.replace("+","")
            total+=float(n_installs)
            len_category+=1
    avg_n_installs=total/len_category
   # print(category,":",avg_n_installs)

for app in android_final:
    if app[1]=='COMMUNICATION' and (app[5]=='1,000,000,000+' or
                                    app[5]=='500,00,000+'
                                    or app[5]=='100,000,000+'):
        print(app[0],":",app[5])

under_100_m=[]
for app in android_final:
    n_installs=app[5]
    n_installs=n_installs.replace(",","")
    n_installs=n_installs.replace("+","")
    if(app[1]=="COMMUNICARION") and(float(n_installs)< 100000000):
        under_100_m.append(float(n_installs))
if len(under_100_m) > 0:
    average_installs = sum(under_100_m) / len(under_100_m)
   # print("Average installs under 100M for COMMUNICATION apps:", average_installs)
else:
    print("No COMMUNICATION apps with installs under 100M found.")

for app in android_final:
    if app[1]=='BOOKS_AND_REFERENCES':
        print(app[0],":",app[5])

for app in android_final:
    if app[1]=='BOOKS_AND_REFERNCES' and(app[5]=='1,000,000,000+' 
                                         or  app[5]=='500,000,000+'
                                         or app[5]=='100,000,000+'):
        print(app[0],":",app[5])

for app in android_final:
    if app[1]=='BOOKS_AND_REFERNCES' and(app[5]=='1,000,000+' 
                                         or  app[5]=='5,000,000+'
                                         or app[5]=='10,000,000+'
                                         or app[5]=='50,000,000+'):
        print(app[0],":",app[5])

""")
import sys
import csv
from csv import reader
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main(input_category):
    # Load datasets
    with open('googleplaystore.csv', mode='r', encoding="utf8", errors="ignore") as file:
        read_file = reader(file)
        android = list(read_file)
    android_header = android[0]
    android = android[1:]  # Exclude header

    with open('AppleStore.csv', mode='r', encoding="utf8", errors="ignore") as file:
        read_file = reader(file)
        ios = list(read_file)
    ios_header = ios[0]
    ios = ios[1:]  # Exclude header

    # Clean Android data by removing duplicates
    reviews_max = {}
    for app in android:
        name = app[0]
        n_reviews = (app[3])
        if name in reviews_max and reviews_max[name] < n_reviews:
            reviews_max[name] = n_reviews
        elif name not in reviews_max:
            reviews_max[name] = n_reviews

    android_clean = []
    already_added = []
    for app in android:
        name = app[0]
        n_reviews = (app[3])
        if (reviews_max[name] == n_reviews) and (name not in already_added):
            android_clean.append(app)
            already_added.append(name)

    # Filter apps by the input category and display analysis
    def display_filtered_analysis(dataset, category_index, target_category):
        filtered_apps = [app for app in dataset if app[category_index].lower() == target_category.lower()]
        
        if not filtered_apps:
            print(f"No apps found for category: {target_category}")
            return

        print(f"Analysis for category: {target_category}")
        
        # Display each filtered app and installs (example output for demonstration)
        for app in filtered_apps:
            print(f"{app[0]} : {app[5]} installs")

    # Example Usage:
    # Filter and display Android apps based on category
    display_filtered_analysis(android_clean, 1, input_category)

    # Filter and display iOS apps based on category
    display_filtered_analysis(ios, -5, input_category)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input= sys.argv[1]
        main(input)
    else:
        print("Please provide a category as a command-line argument.")
