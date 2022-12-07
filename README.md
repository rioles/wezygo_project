## Wezygo
wezygo is a command application that allows you to find nearby trucks

### Description
We empower merchants to find the right way (truck and route) to transport their goods

## Getting Started
### Dependencies
+ no library is required except setuptools for package management
### Installing
clone this [repository] (https://github.com/rioles/wezygo_project)
once done, install setuptools in your local computer

### Executing program
+ In the root of the app folder, execute ./console
    + ``run echo `'create class attribute=value' | WEGO_MYSQL_USER=jose WEGO_MYSQL_PWD=jose WEGO_MYSQL_HOST=localhost WEGO_MYSQL_DB=wezygo_dev_db WEGO_TYPE_STORAGE=db ./console.py` to create an object in to the database``
    For instance, to create merchant object execute this command ``echo 'create Merchant first_name="California" surn_name="aude"' | WEGO_MYSQL_USER=jose WEGO_MYSQL_PWD=jose WEGO_MYSQL_HOST=localhost WEGO_MYSQL_DB=wezygo_dev_db WEGO_TYPE_STORAGE=db ./console.py``
    To find a random coordinate, after execute ``./console.py`` type genaretecoordinate
    to find close driver coordinate to match the preview coordinate type find_nearcab lat long
## Authors
Jean-José GBETO - [Github](https://github.com/rioles)
Martin Joseph Lubowa - [Github](https://github.com/martin-creator) 