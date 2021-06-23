import csv
filename = input()
fields = []
rows = []

#to store max values of each subject
maths_max=0
biology_max=0
english_max=0
physics_max=0
chemistry_max=0
hindi_max=0

#to index of max values of each subject
maths_max_index=0
biology_max_index=0
english_max_index=0
physics_max_index=0
chemistry_max_index=0
hindi_max_index=0

#to store all three ranks sum
first_max=0
second_max=0
third_max=0

#to store all three ranks index
first_max_index=0
second_max_index=0
third_max_index=0

#to count each index in rows list
index_count=0

#CSV file will be copied to list named rows
with open(filename,"r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader) #headings in csv file
    for row in csvreader:
        rows.append(row)

for row in rows:
    marks_sum=0
    for j in range(1,len(row)):
        row[j]=int(row[j])
        marks_sum=marks_sum+row[j]

        if j==1 and row[j]>maths_max:
            maths_max=row[j]
            maths_max_index=index_count

        elif j==2 and row[j]>biology_max:
            biology_max=row[j]
            biology_max_index=index_count

        elif j==3 and row[j]>english_max:
            english_max=row[j]
            english_max_index=index_count

        elif j==4 and row[j]>physics_max:
            physics_max=row[j]
            physics_max_index=index_count

        elif j==5 and row[j]>chemistry_max:
            chemistry_max=row[j]
            chemistry_max_index=index_count

        elif j==6 and row[j]>hindi_max:
            hindi_max=row[j]
            hindi_max_index=index_count

    if(marks_sum>first_max):
        third_max=second_max
        third_max_index=second_max_index
        second_max=first_max
        second_max_index=first_max_index
        first_max=marks_sum
        first_max_index=index_count

    elif(marks_sum>second_max):
        third_max=second_max
        third_max_index=second_max_index
        second_max=marks_sum
        second_max_index=index_count

    elif(marks_sum>third_max):
        third_max=marks_sum 
        third_max_index=index_count

    index_count=index_count+1

print("Topper in Maths    : ",rows[maths_max_index][0])
print("Topper in Biology  : ",rows[biology_max_index][0])
print("Topper in English  : ",rows[english_max_index][0])
print("Topper in Physics  : ",rows[physics_max_index][0])
print("Topper in Chemistry: ",rows[chemistry_max_index][0])
print("Topper in Hindi    : ",rows[hindi_max_index][0])
print("Best students in the class are  -  "+str(rows[first_max_index][0])+" : First rank,  "+str(rows[second_max_index][0])+" : Second rank,  "+str(rows[third_max_index][0])+" : third rank")
print("Time complexity of the Algorithm is : O(nm)")
