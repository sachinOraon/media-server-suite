## Steps to setup PiBoard
It's a dashboard that displays the running docker containers in one place.

 1. Clone this repository and navigate to piboard directory.
    - `git clone https://github.com/sachinOraon/media-server-suite.git`
    - `cd media-server-suite/piboard`
    

 2. Create virtual environment for installing python modules[`root` permission is required].
	  - `sudo -s`
    - `virtualenv envname`
    - `source envname/bin/activate`
    - `pip3 install flask-restx flask-cors docker`
    

 3. (Optional) Change the flask's default port number(5000) by modifying [this line](https://github.com/sachinOraon/media-server-suite/blob/23e75c96653928b2d4488c542ecfed8a48bc8335/piboard/api.py#L82) For example:
    `app.run(debug=True, host='0.0.0.0', port=8080)`

 4. (Optional) Change the port number value as per step 3 by modifying [this line](https://github.com/sachinOraon/media-server-suite/blob/23e75c96653928b2d4488c542ecfed8a48bc8335/piboard/html/index.html#L102)

 5. Add your running container name in the file `piboard/Container.py` and also add the details for it as mentioned in `piboard/Description.py`

 6. Start the flask server using command `python3 api.py`

 7. Open new terminal and start the apache server using command
    `sudo docker run -d --rm --name piboard -p 80:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:latest`

