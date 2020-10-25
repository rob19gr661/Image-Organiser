import os
from PIL import Image, ExifTags
import shutil  # For moving files

img_folder = r"U:\organizer_test"
img_contents = os.listdir(img_folder)

name_date_storage = {}  # For storing image path and date
list_dates = []  # For temporary storage of date and time

# The following code gets the image data and stores it in a dictionary
for image in img_contents:
    try:  # If the image name starts with 'I' it's a image
        full_path = os.path.join(img_folder, image)

        # Will open up the image and extract the date and time it was created using the TAG: 36867
        pil_img = Image.open(full_path)._getexif()[36867]

        # Splits the date and time into two elements in a list
        # The date and time is separated by a dash
        list_dates = pil_img.split(" ")

        # Stores the image path as keys and dates as values
        name_date_storage.update({full_path: list_dates[0]})  # The '0' element is the date

    except IOError:  # IOError only works in Windows !!!PROBLEM!!!
        print("This might be a video: ", image)


# Stores each year in a set
empty_year_set = set()
for v in name_date_storage.values():
    year, month, day = v.split(":")
    empty_year_set.add(year)

# Creates a sub-folder inside the image folder for each year
sorted_list = sorted(empty_year_set)
os.chdir(img_folder)  # Change target folder
for years in sorted_list:
    try:
        os.mkdir(years)
    except FileExistsError:
        print("Files already created")
        quit()

# Moves the each image in the image folder to their respective sub-folder
for years in sorted_list:
    target_folder = os.path.join(img_folder, years)
    for path, dates in name_date_storage.items():
        year, month, day = dates.split(":")
        if years == year:
            shutil.move(path, target_folder)
        else:
            pass


"""
for keys, values in name_date_storage.items():
    print(keys + ": ", values)
"""