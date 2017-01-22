# download

download is a simple python program to download a video file from a webpage/site using just the link to the page.
It currently only supports vidzi.tv pages but I will be implementing many more in the coming weeks.
The aim is to improve my app [film_search](https://github.com/jamiejackherer/film_search) by improving/creating
modules one at a time that can be packaged together as a fully functional application for downloading films
and tv shows.

## To Use

The best way to use this repo as a download program is to run the following commands (Linux only);

```bash
# Clone this repository
git clone https://github.com/jamiejackherer/download
# Change directory into the cloned app
cd download
# Better to use sudo, or be root, with the following command
sudo cp * /usr/sbin/
# The program is now globally available to use,
# for now it will download the file into the current directory
# obviously replace the vidzi link with your own chosen vidzi link
download http://vidzi.tv/pozl9s8gs5bn.html
# The above command should output;
[+] Extracting video file link from: http://vidzi.tv/pozl9s8gs5bn.html
[+] Found video file link: http://185.45.13.130:8777/inuqirx3vq2qedz7njmbxczljyneu7mweqsbp3tcdiy55vazrsjmfmlpkngq/v.mp4
[+] Found video title thebigbangtheory1013hdtvRBB:
[+] Starting download...
100% [....................................................] 53901336 / 53901336
[+] Done!
```

# TODO
1. I will create lots of error handling.
2. Implement resume download feature.
3. Currently the title we extract has no spaces, I will fix this to replace spaces with hypens (-) or underscores (_).
4. Currently the uploaders tags will be in the title, this will soon be fixed to show only the title.
5. In dl.py we have two methods for the actual downloading of the file, a regular requests stream=True,
   and the python wget library. The default is wget but I will strive to replace this with a requests
   file stream, using parrallel/threaded downloading.

#### License [MIT]
