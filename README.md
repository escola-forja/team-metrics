# Team metrics

This project calculates metrics based on a set of delivered tasks.

## Dependencies
You need `Python 3.12` installed (it can work with other versions, but everything was tested in this specific version.)

Then you can install the requirements:
```commandline
pip install -r requirements.txt
```

## How to run
You can run this project with the command below:
```commandline
python -m src data/team-data-file.csv
```

## Feeding with data
In order to run this project you need a csv file with a team's tasks (1 per line) following the structure below:
```
Squad;UID;Started at;Finished at;Type
Team Billy;BLUE-47;2019-11-28 16:59:04;2019-11-28 19:33:32;BUG
Team Billy;BLUE-46;2019-11-22 13:10:47;2019-11-28 13:48:51;DISCOVERY
Team Billy;BLUE-45;2019-11-25 14:32:16;2019-11-29 14:09:22;STORY
Team Billy;BLUE-44;2019-11-07 17:29:54;2019-11-18 15:31:01;DISCOVERY
Team Billy;BLUE-43;2019-11-18 18:32:37;2019-12-04 12:14:42;STORY
```

The separator must be a **semicolon** and the header must be exactly the above. All fields are mandatory.

Sample metrics
* [Team Billy](https://files.escolaforja.com.br/tecnicas-estimativas/Team-Billy.csv)
* [Team Tommy](https://files.escolaforja.com.br/tecnicas-estimativas/Team-Tommy.csv)
* [Team Zack](https://files.escolaforja.com.br/tecnicas-estimativas/Team-Zack.csv)

The files can be wherever you want (we recommend using the `data` directory). Just make sure that the file path that you provide for the command is correct.