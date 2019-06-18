# _*_ coding: utf-8 _*_
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Text, Dict, Any, List

from rasa_core_sdk import Action, Tracker, ActionExecutionRejection
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet

import logging
import requests

logger = logging.getLogger(__name__)

QUERY_TYPES = {
    "incidents": {
        "name": "Incidents"
    },
    "changes": {
        "name": "Changes"
    }
}

class ActionMenu(Action):
    """To display buttons for each of the query type"""

    def name(self) -> Text:
        """Unique identifier"""
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List:

        buttons = []
        for q in QUERY_TYPES:
            query_type = QUERY_TYPES[q]
            print(query_type)
            payload = "/inform{\"search_type\": \"" + query_type.get("name") + "\"}"
            print(payload)

            buttons.append({"title": "{}".format(query_type.get("name")), "payload": payload})

        dispatcher.utter_button_template("utter_greet", buttons, tracker)
        dispatcher.utter_custom_message({"message":"hello-world"})
        return []

class SearchForm(FormAction):
    """"Main form with options"""

    def name(self):

        return "search_form"

    @staticmethod
    def required_slots(tracker):

        search_type = tracker.get_slot('search_type')
        if search_type:
            if search_type.lower() == 'incidents':
                return [
                    "search_type","incident_no","application","severity"
                ]
            elif search_type.lower() == 'changes':
                return [
                    "search_type","change_no"
                ]
        return []

    def slot_mappings(self):

        """Dictionary to map required slots to entity, intent value pairs or a whole message"""

        return {
            "incident_no": [
                self.from_entity(entity='identifier'),
                self.from_entity(entity='identifier', intent=["search_provider","inform"]),
                self.from_intent(intent="deny", value="*")
            ],
            "change_no": [
                self.from_entity(entity='identifier'),
                self.from_entity(entity='identifier', intent=["search_provider","inform"]),
                self.from_intent(intent="deny", value="*")
            ],
            "application": [
                self.from_entity(entity='application'),
                self.from_entity(entity="application", intent=["inform","search_provider"]),
                self.from_intent(intent="deny", value="*"),
            ],
            "severity": [
                self.from_entity(entity='severity'),
                self.from_entity(entity="severity", intent=["inform","search_provider"]),
                self.from_intent(intent="deny", value="*"),
            ]
        }

    def request_next_slot(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):

        if tracker.get_slot('completed'):
            print(tracker.get_slot('completed'))
            return None
        else:
            for slot in self.required_slots(tracker):
                if self._should_request_slot(tracker, slot):
                    logger.debug("Request next slot '{}'".format(slot))
                    dispatcher.utter_template(
                        "utter_ask_{}".format(slot), tracker)
                    return [SlotSet(REQUESTED_SLOT, slot)]
        return None

    def validate(self, dispatcher, tracker, domain):

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
            if slot_to_fill == 'incident_no':
                if 'incident_no' in slot_values:
                    if slot_values['incident_no'] != '*':
                        slot_values.update(dict(completed=True))
                else:
                    dispatcher.utter_message("Invalid incident number. please enter again.")
                    return [SlotSet('incident_no', None)]
            elif slot_to_fill == 'change_no':
                if 'change_no' in slot_values:
                    if slot_values['change_no'] != '*':
                        slot_values.update(dict(completed=True))
                else:
                    dispatcher.utter_message("Invalid change number. please enter again.")
                    return [SlotSet('change_no', None)]

            if not slot_values:
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                                "with action {1}"
                                                "".format(slot_to_fill, self.name()))

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        dispatcher.utter_template("utter_submit", tracker)
        return []
