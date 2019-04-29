import string

# Variable definitions
photo = [" "] 
gallery_entry = [" "]
photo_array = [" "]
gallery_key = [" "] 
i = 0
line = unicode('  ', 'utf-8')

# Define files for reading. 
file_name = "a_example.txt"  
        
#open the file
f = open(file_name, 'r')
file_info = f.readlines()
f.close()

#slide.create_photos()
for line in file_info: 
    print line
    line.lstrip(" ")
    line.lstrip("\n")
    line.lstrip("    ")
    line.trim()
    testBoolean = line.isdigit()
    print( "Is digit", testBoolean, "\n") 
    if testBoolean:
        num_images = line     
        print( "Is digit", num_images, "\n") 
    else:
        #for l in range(0,len(file_info),1):
        photo.append(line.split(" "))
        print( photo )
        photo_array.append(photo)
        print( photo_array )
        print( "\n" )
    
#Sort the photos
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
    print "photo.tags"
    print photo_tags     
    print( "\n" )        
            
    for i in range(0,len(photo.tags),1):
    #for i=0; in phototags:
        print "i - " , i
        for x in range(0,len(gallery_key),1):
            print "\tx - " , x
            print "\t\t gallery_key - " , gallery_key[x]
            print "\t\t photo_tags - " , photo_tags[i]
            if gallery_key[x] == photo_tags[i]:
                # if exists in key add to entry index
                print "\t\t\t photo_id", photo_id
                gallery_entry[x] = gallery_entry[x] + photo_id
            else:
                # loop until gallery_key is exhausted, then append to end.
                max_keys = len(gallery_key)
                print "\t\t\t\t max_keys", max_keys
                if x == max_keys:
                    print "\t\t\t\t append to arrays", max_keys
                    gallery_key.append(photo_tags) 
                    gallery_entry.append(photo_id)
                else: 
                    # loop until phonebookkey is exhausted, then append to end.
                    print "\t\t\t\t no match at i vs x", i, x, max_keys

    print "gallery_key"
    print gallery_key
    for y in range(0,len(phone_book_key),1):
        print phone_book_entry[y]
            
    print "phone_book_entry"
    for z in range(0,len(phone_book_entry),1):
        print phone_book_entry[z]
            
                 



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