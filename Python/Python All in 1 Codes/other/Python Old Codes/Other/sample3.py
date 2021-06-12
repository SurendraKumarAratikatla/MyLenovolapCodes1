class TimeSheet(Action):
    def name(self):
        return "Esi_TimeSheet"

    def run(self, dispatcher, tracker, domain):
        url = 'http://api.easystepin.com/ws/rest/chatbot/EmpTimesheets/'
        username = 'ESI_MI@easystepinitservicesllc-4ZNYGO'
        password = '9d611be6-d4ef-4db3-aa84-e065b498f721'
        auth_values = (username, password)
        # Empid = tracker.get_slot("empID")
        value = {
            "user": "6723",
            "approvalStatus": "approved"
        }
        response = requests.post(url, data=json.dumps(value), auth=HTTPBasicAuth(username, password))
        str1 = ""
        timeSheetVar = ""

        if response.status_code != 200:
            # This means something went wrong.
            # raise ApiError('GET /tasks/ {}'.format(response.status_code))
            print(response.status_code)
        else:
            json_data = response.json()
            timesheetcount = len(json_data)
            print("Esi_TimeSheet " + str(timesheetcount))
            print("Total number of timesheet action is working successfuly" + " Count = " + str(timesheetcount))
            timeSheetVar = timeSheetVar + str(timesheetcount)
        return [SlotSet('tscount', timesheetcount)]