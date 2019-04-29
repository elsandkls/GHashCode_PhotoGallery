import string
import re

# Variable definitions 
# Define files for reading.   
#file_name = "solution_a.txt"  
#file_name = "solution_b.txt"   
file_name = "solution_c.txt"  
#file_name = "solution_d.txt"  
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

#slide.create_photos()
for line in file_info:  
    line = line.strip("\n")      
    testBoolean = line.isnumeric() 
    if testBoolean:
        num_images = line     
        print( "Is digit", num_images, "\n") 
        photo[0] = num_images
    else:
        #build photo array.
        photo.append(i)
        photo[i] = line
        print( "photo array: ", photo )
        
        photo_list = line.split(" ")
        for t in range(0,len(photo_list),1):
            if(t == 0):
                photo_orientation.append(photo_list[t])
            elif(t == 1): 
                photo_num_tags.append(photo_list[t])
            else: 
                for a in range(0,len(photo_tags),1):
                    if photo_list[t] == photo_tags[a]:
                        #print("match found")
                        tag_match = "yes"
                    else:
                        #print("no match found")
                        m=0                           
                if tag_match == "no":
                    photo_tags.append(photo_list[t])
                else:
                    tag_match = "no"    
                
    i = i +1;    
 
print("\n")
        
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

#add to handle verticals correctly.
pictureOne = ""
pictureTwo = ""
pictureThree = ""

# begin the actual sorting
for p1 in range(0,len(photo),1):
    if( p1< (len(photo)-1)):
        p2=p1+1
    else:        
        p2=0
    #print("working with image(",p1,") and image(", p2,") out of ", len(photo)," images.")
           
    if p1 == 0:
       gallery_photos[0] = photo[0]
       # set the gallery output to the number of photos read into the photo array.
       #print("\n")
    else:     
        for t in range(1,len(photo_tags),1):
            stringPattern = "(.)*" + photo_tags[t]+ "(.)*"
            #print (stringPattern)
            #print("start 1: ",photo_tags[t], photo[p1], re.match(stringPattern, photo[p1]))
            if re.match(stringPattern, photo[p1]): 
                #print("\t next: ",photo_tags[t], photo[p2], re.match(stringPattern, photo[p2]))
                if re.match(stringPattern, photo[p2]):
                    #the number of common tags between S i and S i+1
                    score_001 = score_001 + 1
                    #print("\t \t ", score_001,score_002,score_003)
                else:                
                    #the number of tags in S i but not in S i+1
                    score_002 = score_002 + 1
                    #print("\t \t ", score_001,score_002,score_003)   

            #print("start 2: ",photo_tags[t], photo[p2], re.match(stringPattern, photo[p2]))
            if re.match(stringPattern, photo[p2]):
                #print("\t next: ",photo_tags[t], photo[p1], re.match(stringPattern, photo[p1]))
                if re.match(stringPattern, photo[p1]):
                    score_003 = score_003 + 0
                    #print("\t \t ", score_001,score_002,score_003)
                else:   
                    #the number of tags in S i+1 but not in S i.
                    score_003 = score_003 + 1
                    #print("\t \t ", score_001,score_002,score_003)
            #print("Next:  ")
    #print("End: ")
    #print("final scores: ", score_001,score_002,score_003)
    gallery_scores.append(min(score_001,score_002,score_003)) 
    score_001 = 0
    score_002 = 0
    score_003 = 0
    #print("\n")
    
#print results  
#print("gallery_scores array", gallery_scores) 
for score_001 in range(0,len(gallery_scores),1):
    score_total = score_total + gallery_scores[score_001] 
print("\n score_total: ", score_total,"\n" ) 