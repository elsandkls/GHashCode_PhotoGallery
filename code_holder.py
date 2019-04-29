
#Sort the photos, there should be the same number of keys in the photo_array as first line of the file.
#integrity check.
if(len(photo_array) == num_images):
    for i in range(0,len(photo_array),1):
        for photo in photo_array[i]:
            photo_id = photo[0]
            photo_orientation = photo[1]
            photo_tags = photo[2] 
            # debug check contents.
            print( photo_id )
            print( photo_orientation )
            print( photo_tags)
            print( "\n" )
  
            #small time 
            print ("photo.tags")
            print ( photo_tags )    
            print( "\n" )        
            
        for i in range(0,len(photo.tags),1):
            #for i=0; in phototags:
            print ("i - " , i)
            for x in range(0,len(gallery_key),1):
                print ("\tx - " , x)
                print ("\t\t gallery_key - " , gallery_key[x])
                print ("\t\t photo_tags - " , photo_tags[i])
                if gallery_key[x] == photo_tags[i]:
                    # if exists in key add to entry index
                    print ("\t\t\t photo_id", photo_id)
                    gallery_entry[x] = gallery_entry[x] + photo_id
                else:
                    # loop until gallery_key is exhausted, then append to end.
                    max_keys = len(gallery_key)
                    print ("\t\t\t\t max_keys", max_keys)
                    if x == max_keys:
                        print ("\t\t\t\t append to arrays", max_keys)
                        gallery_key.append(photo_tags) 
                        gallery_entry.append(photo_id)
                    else: 
                        # loop until gallery_key is exhausted, then append to end.
                        print ("\t\t\t\t no match at i vs x", i, x, max_keys)
                            

print ("gallery_key")
print (gallery_key)
for y in range(0,len(gallery_key),1):
    print (gallery_key[y])
    print ("photo_array")
    for z in range(0,len(photo_array),1):
        print (photo_array[z])
            
#slide.print_photos()
for photo in self.photos:
    print("{} {} {}".format(photo.photo_id, photo.orientation, photo.tags))

# Writes the new order to the file
file_name = "solution_a.txt"
f = open(file_name, "w")
#fix me array call in a for loop
for photo in photos:
    f.write(str(photo.photo_id) + "\n")
f.close()



########################################################
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
    print("final scores: ", score_001,score_002,score_003)
    gallery_scores.append(min(score_001,score_002,score_003)) 
    score_001 = 0
    score_002 = 0
    score_003 = 0 
        
