import string
import re

# Variable definitions 
# Define files for reading. 
file_name = "a_example.txt" 
#file_name = "b_lovely_landscapes.txt" 
#file_name = "b_short_lovely_landscapes2.txt" 
#file_name = "c_memorable_moments.txt" 
#file_name = "d_pet_pictures.txt"  
#file_name = "e_shiny_selfies.txt"  

# Writes the new order to the file
file_OUT_name = "solution_a.txt"  
#file_OUT_name = "solution_b.txt"   
#file_OUT_name = "solution_c.txt"  
#file_OUT_name = "solution_d.txt"  
#file_OUT_name = "solution_w.txt"       
        
#open the file
f = open(file_name, 'r')
file_info = f.readlines()
f.close()

# Variable definitions
photo_orientation = ["0"] 
photo_tags = ["0"] 
photo_num_tags = ["0"] 
photo = ["0"]   
i = 0 
tag_match = "no"
m = 0;
tracker = " "

for line in file_info:  
    line = line.strip("\n")      
    testBoolean = line.isnumeric() 
    if testBoolean:
        num_images = line     
        print( "Is digit", num_images, "\n") 
        photo[0] = num_images
    else:
        photo.append(i)
        photo[i] = line        
        photo_list = line.split(" ")
        for t in range(0,len(photo_list),1):
            if(t == 0):
                photo_orientation.append(photo_list[t])
                tracker = tracker + "."
            elif(t == 1): 
                photo_num_tags.append(photo_list[t])
                tracker = tracker + "."
            else: 
                for a in range(0,len(photo_tags),1):
                    if photo_list[t] == photo_tags[a]:
                        tag_match = "yes"
                        tracker = tracker + "."
                    else:
                        m=0                          
                if tag_match == "no":
                    photo_tags.append(photo_list[t])
                    tracker = tracker + "."
                else:
                    tag_match = "no"     
            tracker = tracker + "."        
        tracker = tracker + "."                
        print(tracker, num_images, i) 
    tracker = ""    
    i = i +1;     
print("end read :: \n") 

########################################################    
#print results   
print("photo_orientation array ", photo_orientation)  
print("photo_tags array ", photo_tags)  
print("photo_list array ", photo_list)  
print("photo array ", photo)  

########################################################
# Variable definitions
 
gallery_photos = ["0"]
gallery_scores = [0]
p1 = 0 # photo one
p2 = 0 # photo two
t = 0 # tags counter
score_001 = 0
score_002 = 0
score_003 = 0
score_total = 0
relativescore = 0
stringScore = ""
stringPattern = ""
string_FullPattern = ""
tracker= ""
r =0 
remove_photos = [0]

gallery_photos[0] = photo[0]
for t in range(1,len(photo_tags),1):
    string_FullPattern = photo_tags[t]    
    z = len(photo)
    s=0
    for s in range(1,z,1):
        print("start tag: ", t, " of ", len(photo_tags), " removed: ", s, " of ", (len(photo)), "entry: ", photo_tags[t], " entry: ", photo[s])        
        if re.findall(string_FullPattern, photo[s]):
            #gallery_photos[s] = photo[s]
            gallery_photos.append(photo[s])
            remove_photos.append(s)
            print("Matched: sorted ", string_FullPattern, " s:",s," z:", z)
            tracker= tracker + "~~"
        else:
            tracker= tracker + "--"    
            print("No Match") 
    tracker= tracker + "##"
 
    for r in range((len(remove_photos)-1),0,-1):
        print(" removed: ", r, " of ", (len(remove_photos)-1), "entry: ", remove_photos[r], " entry: ", photo[remove_photos[r]])
        photo[remove_photos[r]] = " nullified " 
        remove_photos[r] = 0       
                        
print(tracker)
tracker= ""     

print("End keyword sort")

########################################################    
#print results  
print("gallery_photos array ", gallery_photos)  


########################################################
# sort the array so that horizontal images are first.
sortingOne = ""
sortingTwo = ""
sortingThree = ""
s = 0
stringPattern = "^V" 
z = len(photo) -2
tracker= ""
for s in range(0,z,1):
    if re.match(stringPattern, photo[s]):
        tracker= tracker + "$$"
        if re.match(stringPattern, photo[s+1]): 
            tracker= tracker + "$$"
            # no sorting needed
            s = s+1
        else:    
            tracker= tracker + "^^"
            sortingOne = photo[s];
            sortingTwo = photo[s+1];
            sortingThree = photo[s+2];
            if re.match(stringPattern, photo[s+2]):
                tracker= tracker + "$$"
                photo[s] = sortingTwo
                photo[s+1] = sortingOne
                #photo[s+2] = sortingThree
                tracker= tracker + "&&" 
                s = s+2
            else:
                photo[s] = sortingTwo
                photo[s+1] = sortingThree
                photo[s+2] = sortingOne 
                s = s+1                    
    else: 
        tracker= tracker + "**"
    print(tracker,"\n")
    tracker="" 

print("End vertical vs horizontal sort")

########################################################    
#print results  
print("gallery_photos array ", gallery_photos)  

########################################################    
# begin the scorecard
for p1 in range(1,len(gallery_photos),1):
         
    if p1 == 0: 
       gallery_scores[p1] = 0
    else:     
        for t in range(1,len(photo_tags),1):
            stringPattern = photo_tags[t]  
            if re.findall(stringPattern, gallery_photos[p1]):  
                if re.findall(stringPattern, gallery_photos[p2]):
                    #the number of common tags between S i and S i+1
                    score_001 = score_001 + 1 
                else:                
                    #the number of tags in S i but not in S i+1
                    score_002 = score_002 + 1  
 
            if re.findall(stringPattern, gallery_photos[p2]): 
                if re.findall(stringPattern, gallery_photos[p1]):
                    score_003 = score_003 + 0 
                else:   
                    #the number of tags in S i+1 but not in S i.
                    score_003 = score_003 + 1  

    ## fix em, score on a is not showing up right, 0 3 0 should be 1 3 0
    print(p1, " of ", len(gallery_photos), "final scores: ", score_001,score_002,score_003)
    gallery_scores.append(min(score_001,score_002,score_003)) 
    score_001 = 0
    score_002 = 0
    score_003 = 0 

########################################################    
#print results  
print("gallery_photos array ", gallery_photos) 
print("gallery_scores array", gallery_scores) 
print("\n")

#print results  
print("gallery_scores array", gallery_scores) 
for score_001 in range(0,len(gallery_scores),1):
    score_total = score_total + gallery_scores[score_001] 
print("\n score_total: ", score_total,"\n" ) 
     
########################################################


# Writes the new order to the file 
f = open(file_OUT_name, "w")
#fix me array call in a for loop
#for new_photo in gallery_photos:
s = 0
for s in range(0,len(gallery_photos)-1,1):    
######################################################## 
    sortingOne = ""
    sortingTwo = ""
    sortingThree = "" 
    stringPattern = "^V" 
    if re.match(stringPattern, gallery_photos[s]): 
        if re.match(stringPattern, gallery_photos[s+1]):
            my_string = gallery_photos[s]
            my_list = my_string.split(' ')  
            my_string2 = gallery_photos[s+1]
            my_list2 = my_string2.split(' ')               
            f.write(str(my_list[0]) + " " + str(my_list2[0]) +"\n")
            s = s+1                  
    else:  
        my_string = gallery_photos[s]
        my_list = my_string.split(' ')  
        f.write(str(my_list[0]) + "\n")
        
f.close()    
