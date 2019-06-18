## greet
* greet
    - action_menu
    
## thank
* thank
    - utter_thank

## bye
* bye
    - utter_bye

## story incidents - #1
* inform{"search_type":"incidents"}
    - search_form
    - form{"name":"search_form"}
    - form{"name":"null"}
    - utter_slots_values
    - action_restart
* search_provider{"identifier":"INCH00000001"}
    - search_form
    - form{"name":"search_form"}
    - form{"name":"null"}
    - utter_slots_values
    - action_restart    
* thank
    - utter_thank

## story incidents - #2
* inform{"search_type":"changes"}
    - search_form
    - form{"name":"search_form"}
    - form{"name":"null"}
    - utter_slots_values
    - action_restart
* search_provider{"identifier":"CHKL00000001"}
    - search_form
    - form{"name":"search_form"}
    - form{"name":"null"}
    - utter_slots_values
    - action_restart    
* thank
    - utter_thank