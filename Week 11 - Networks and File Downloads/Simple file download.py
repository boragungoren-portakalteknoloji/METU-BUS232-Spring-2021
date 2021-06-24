# We will demonstrate simple ways of file downloads from the web

# A URL is the unique identifier for the location of a networked resource
# Most URL's are web URL's, they start with http:// or https://
metu_homepage_url="https://www.metu.edu.tr"
metu_logo_url="https://www.metu.edu.tr/sites/all/themes/odtu/images/odtu-logo-en.svg"

# Method 1 - Use Python 2 URL library -- https://docs.python.org/dev/library/urllib.html
# This library is somewhat raw, and also old. But it will work with minimal coding.
from urllib import request
# For simplicity let's assume 
remote_url = metu_logo_url
local_file = "logo.svg"
request.urlretrieve(remote_url, local_file)
# Note that when an existing file is retrieved, this method overwrites the file without any prompt or notification.
# So if you are downloading a file which has the same name but the content changes, you should consider if you need the older version.
# If you need older versions, you should modify the local file name each time you copy. Appending a date/time marker is the usual way to do so.

# Method 2 - Wget Python Library -- https://pypi.org/project/wget/
# You need to install this library on your system. On Thonny Tools -> Manage Packages will suffice.
# If you want to install this package or any other package for a PyPi hosted library from the command line
# Check out -- https://pypi.org/project/pypi-install/
# There is a very popular command like download app in Linux and MacOS called wget.
# This library implements its features partially
print("Download example with wget")
import wget
remote_url = metu_logo_url
# There are a number of options. First you can specify a local file name
local_file="logo-wget.svg"
wget.download(remote_url, local_file)
# Note that wget will not replace an existing file by default. So you will end up with (1), (2), etc in the file names.
# If you are OK with this behavior, just use the default version. 
# If you don't specify the original file name will be used
remote_file_name = wget.download(remote_url)
print("Downloaded file as ", remote_file_name)
# Wget first download the file with a .tmp extension.
# Once the download is verified, it will be renamed.
# Therefore wget downloads pretty much the same way your web browser downloads

# You can also display a fancy download bar
# To do that you should first define a function that includes the format for your bar.
print("Download example with bar")
def my_bar(current, total, width=80):
    # These parameters are required for wget. If you get a warning for "unused argument" discard it. 
    print("Currently downloading: %d%% [%d of %d] bytes" % (current / total * 100, current, total))
remote_file_name = wget.download(metu_logo_url, bar=my_bar)
print("Downloaded: ", remote_file_name)
# The bar makes sense when you download a larger file
# This is close to 2 GBs. Do not download it if you are on mobile connection. 
# large_file_url="https://ftp.linux.org.tr/ubuntu-releases/21.04/ubuntu-21.04-desktop-amd64.iso"
# remote_file_name = wget.download(large_file_url, bar=my_bar)
# Note that the output for this line will be MANY lines such as
# Currently downloading: 0% [21528576 of 2818738176] bytes
# Currently downloading: 0% [21536768 of 2818738176] bytes
# Currently downloading: 0% [21544960 of 2818738176] bytes
# This is normal, because the way you access the output screen is line by line.
# To have a fancy bar, you need to "update" a line on the screen. Which requires more work. 

# On the web you will occasionally see the following commented example:
# remote_file_name = wget.download(large_file_url, bar=bar_thermometer)
# This is intended to be run as a single command from the Python command line, not from inside a program
# So when you run this, it is OK to not see a bar that updates itself. 

# A better approach with wget would be to embed it in your own download function.
# This way you can add additional checks, relevant to your application. 
# Here is an example:
import os
def web_download(source, target, delete_existing=False):
    # Instead of 
    if delete_existing:
        if os.path.exists(target):
            print("Removing older version of file:", target)
            os.remove(target)
        else:
            print("Local file does not exist. No need to delete anything. ")
    if source.startswith("http"):
        # Now we can use wget
        print("Downloading from", source)
        wget.download(source,target)
    else:
        print("This is not a download from the web.")
    return

# Example URL from US Federal Reserve
print("Downloading US interest rates from FED web service.")
us_interest_rates_zip_url="https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&filetype=zip"
web_download(us_interest_rates_zip_url, "us_rates.zip", delete_existing=True)
print("Download complete.")

# Note that URLs from instutional web sites become complex. So you may need to construct these URLs using string manipulation
# URL construction usually starts with a static portion of the URL, which includes the domain name and the name of the
# service. It is often called the base URL
base_url="https://www.federalreserve.gov/datadownload/Output.aspx?rel="
# Then we decide on the parameters
dataset="H15"
filetype="zip"
url="https://www.federalreserve.gov/datadownload/Output.aspx?rel="+dataset+"&filetype="+filetype
# This is not very different from calling a function.
# There is an old term called "remote procedure call (RPC)"  that was used to define this type of code
print("Constructed URL:", url)
# The variable URL is the call itself, it has to be executed.
# Trying to download this particular URL triggers the call on the source site. 
print("Downloading again.")
web_download(us_interest_rates_zip_url, "us_rates.zip", delete_existing=True)
print("Download complete.")

# Method 3 - Python Requests library
# When you need to download files from complex web sources you might need more interaction.
# HTTP has a basic procedure called a "request - response cycle" for every download you conduct.
# Here is a short explanation of this cycle -- https://medium.com/@jen_strong/the-request-response-cycle-of-the-web-1b7e206e9047
# For a more detailed explanation -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Session
# Python's Requests library exposes these details to you -- https://docs.python-requests.org/en/master/
# You can work with *many* details using this library. 
import requests
url=us_interest_rates_zip_url
response = requests.get(url) # Browser: GET is clicking on a link
print("HTTP Response from FED:", url, " is: ", response)
print("The content type for the FED URL is: ", response.headers["content-type"])
# For an authenticated source which uses simple HTTP Authentication
# authentication_parameters=("username", "password")
# requests.get(url, authentication_parameters)

url=metu_homepage_url #"https://www.metu.edu.tr"
response = requests.get(url)
print("HTTP Response from METU:", url, " is: ", response)
# Let's see what the source classifies our downloaded content as. 
print("The content type for the METU URL is: ", response.headers["content-type"])
# Popular content types are documents, archives, audio/video files, audio/video streams, etc.
# For a list of content types recognized by most systems -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

# Sometimes downloading results from the web may not be very straightforward
# Add the search query at the end
print("Example for search on METU web page")
metu_search_url="https://www.metu.edu.tr/search-page?cx=011418946324636299173%3Ajgqmx6nposk&ie=utf-8&qa="
question="Business"
url=metu_search_url+question
# This one will end up with a blank page, because of Javascript based design. 
web_download(url, "metu_results.html", delete_existing=True)

print("Example for search on Google web page")
google_search_url="https://www.google.com.tr/search?q="
question="Business"
url=google_search_url+question
# This one will likely end up with an HTTP error, because Google does not like a non-browser to conduct search this way
# Google's system will throttle your responses and you will likely end up with a 403 error. -- https://en.wikipedia.org/wiki/HTTP_403
# Uncomment and see. 
# web_download(url, "google_results.html", delete_existing=True)

# Instead: Use the googlesearch package from PyPi -- https://pypi.org/project/googlesearch-python/
# There are other alternatives as well
# See -- https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4
print("Perform Google search with library.")
from googlesearch import search
results=search(question, start = 0, stop = 10, pause = 3.0)
#                                               ^ The pause is important. It will slow down your program
#                                                 but it will also prevent getting 403 errors. 
print("Google results for question:", question)
count=1
for result in results:
    print(count, ". ", result)
    count=count+1
    
# Note that this approach gives us a bunch of other URLs. So you'd have to visit them and see what they offer.
# A "crawler" is a program that explores links on web pages, practically visiting everything.
# Crawlers start from an origin, and a Google search on some keywords could very well be your origin.
# You do not need to develop a crawler for this course but you could consider using an existing crawler in the future. 

# Many institutions provide their own libraries or at least guides for developers to interact with their sites
# If an institution talks about an "API Key" then you need to have a conversation to be authorized to access through
# their programming interface.

# For example Central Bank of the Republic of Turkey -- https://evds2.tcmb.gov.tr/help/videos/EVDS_Web_Service_Usage_Guide.pdf