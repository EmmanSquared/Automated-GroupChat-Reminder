import core

bool_node = True

while bool_node:
    if core.thirty_mins_before.chat_time > core.datetime.now():
        print(f'Minutes left before reminding: {round(core.thirty_mins_before.timeleft_till_next_reminder/60)}.')
        core.sleep(core.thirty_mins_before.timeleft_till_next_reminder)
        core.window_tasks()

    elif core.fifteen_mins_before.chat_time > core.datetime.now():
        print(f'Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        core.sleep(core.fifteen_mins_before.timeleft_till_next_reminder)
        core.window_tasks()
        core.sleep(600)
        core.window_tasks()

    elif core.meet_reminder.timeleft_till_next_reminder > core.datetime.now():
        print(f'Minutes left before reminding: {round(core.fifteen_mins_before.timeleft_till_next_reminder/60)}.')
        core.sleep(core.meet_reminder.timeleft_till_next_reminder)
        core.window_tasks()

    else:
        print('Time for meet had already passed.')
        bool_node = False