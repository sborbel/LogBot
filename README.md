# LogBot

- pysimplegui package install needed for gui
- run "python -m pip install pysimplegui" from whatever shell you use

-if you execute the LogBot.py script with no parameters (other than the the script itself) it will launch the gui

## Example Usage

    -start date/ end date: 
        ./LogBot -s 2021-02-28 -p searchtext
        ./LogBot -e 2021-03-10 -p searchtext
        ./LogBot -s 2021-02-28 -e 2021-03-10 -p searchtext
      
    -numDays:
        ./LogBot -d 10 -p searchtext
    -numHours
        ./LogBot -H 5 -p searchtext
    -pattern
        ./LogBot -p gdm
    -Category
        ./LogBot -c -p Auth
        ./LogBot -c 
    
    -Gotta test -em all
        ./LogBot -p gdm -s 2021-03-05
        
